#!/usr/bin/env python

import configparser
import csv
import datetime
import io
import json
import logging
import os
import sys
from pathlib import Path
import yaml
import geopandas as gpd
import pandas as pd

from github import Github
from lxml import html
from shapely.geometry import Point

# Configure logger to print log message to stdout
logformat = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=logformat)
logger = logging.getLogger('github2CSV')

CSV_COLUMN_NAMES = ["url", "id", "updated_at", "created_at", "title", "lat", "lon", "regione", "provincia", "labels", "milestone", "image", "data", "body", "state"]

# Program arguments
CSVFILE = sys.argv[1]
try:
    JSONFILE = sys.argv[2]
    jwr = io.open(JSONFILE, "r", encoding="utf-8")
except:
    jwr = None

try:
    GEOJSONFILE = sys.argv[3]
    gjwr = io.open(GEOJSONFILE, "r", encoding="utf-8")
except:
    gjwr = None

LIMITIPATH = sys.argv[4]

try:
    ACCETTATOLABEL = sys.argv[5]
except:
    ACCETTATOLABEL = "Accettato"

FILTER_LABELS = ("Accettato", "accepted")
POSIZIONE_NAMES = ("posizione", "Posizione", "position", "Position", "location", "Location")

TMPCSVFILE = './issues_temp.csv'
TMPJSONFILE = './issuesjson_temp.json'
TMPGEOJSONFILE = './issues_temp.geojson'

REPO_NAME = 'covid19italia_segnalazioni'
ORG = 'emergenzeHack'
TOKEN = os.environ.get('GITHUB_TOKEN')

# Default values for repository name and Github organization
# They are used if an error occurred while reading values
# from configuration file
def get_github_client():
    if TOKEN:
        return Github(TOKEN)

    try:
        config = configparser.RawConfigParser()
        config.read('.github.cfg')

        PASS = config.get('GitHub', 'TOKEN')
        USER = config.get('GitHub', 'USER')
        REPO_NAME = config.get('GitHub', 'REPO_NAME')
        ORG = config.get('GitHub', 'ORG')
    except:
        PASS = os.environ.get('GITHUB_PASSWORD')
        USER = os.environ.get('GITHUB_USERNAME')

    if not PASS:
        logger.error("Need a PASS")
        sys.exit(1)

    if not USER:
        logger.error("Need a USER")
        sys.exit(1)

    if not REPO_NAME:
        logger.error("Need a REPO_NAME")
        sys.exit(1)

    if not ORG:
        logger.error("Need a ORG")
        sys.exit(1)
    
    return Github(USER, PASS)


def get_latest_timestamp(csvfile):
    df = pd.read_csv(csvfile, index_col='id', names=CSV_COLUMN_NAMES, header=None, sep=',')
    # sort rows by updated_at timestamp and parse it, in order to return a datetime instance
    data = df.sort_values(by='updated_at', ascending=False)

    if not data['updated_at'][1:-1].empty:
        max_updated_at = max(data['updated_at'][1:-1]) + "+00:00"
        return datetime.datetime.strptime(max_updated_at, '%Y-%m-%d %H:%M:%S%z')
    return datetime.datetime(2000, 1, 1)

def write_output_files(issues):
    write_csv_file(issues)
    if jwr:
        write_json_file(issues)
    if gjwr:
        write_geojson_file(issues)

def write_csv_file(issues):
    with open(CSVFILE, "r") as current_file, open(TMPCSVFILE, "w+") as output_file:
        csvwriter = csv.writer(output_file, quotechar='"')
        csvreader = csv.reader(current_file)
        next(csvreader, None)   # skip the header

        csvwriter.writerow(tuple(CSV_COLUMN_NAMES)) # write CSV header columns
        logger.info("[CSV] Updating issues (if any)...")
        total_rows = 0
        for line in csvreader:
            issue_id = int(line[1])
            # if the issue is in the dictionary (thus has been updated), skip it for the moment.
            if not issue_id in issues:
                csvwriter.writerow(line)
                total_rows += 1
            else:
                logger.info("[CSV] Issue '%d' updated.", issue_id)
            
        logger.info("[CSV] Writing new issues...")
        for issue_id in issues: # append the remaining new issues
            issue = issues[issue_id]
            gh_issue = issue["issue"] # Github issue instance
            row = get_csv_issue(issue, gh_issue)
            csvwriter.writerow(row)
            total_rows += 1

    logger.info("[CSV] Total issues: %d", total_rows)
    # move temp file to final one
    Path(TMPCSVFILE).rename(CSVFILE)

def write_json_file(issues):
    jsonarray = []
    with open(TMPJSONFILE, "w+") as output_file:
        data = json.load(jwr)
        logger.info("[JSON] Updating issues (if any)...")
        for row in data:
            issue_id = row["issue"]["id"]
            # if the issue is in the dictionary (thus has been updated), skip it for the moment.
            if not issue_id in issues:
                jsonarray.append(row)
            else:
                logger.info("[JSON] Issue '%d' updated.", issue_id)

        logger.info("[JSON] Writing new issues...")
        for issue_id in issues: # append the remaining new issues
            issue = issues[issue_id]
            gh_issue = issue["issue"]
            jsonarray.append(get_json_issue(issue, gh_issue))

        logger.info("[JSON] Total issues: %d", len(jsonarray))
        output_file.write(json.dumps(jsonarray, ensure_ascii=False, sort_keys=True))
    # move temp file to final one
    Path(TMPJSONFILE).rename(JSONFILE)

def write_geojson_file(issues):
    geojsonarray = []
    with open(TMPGEOJSONFILE, "w+") as output_file:
        data = json.load(gjwr)
        logger.info("[GeoJSON] Updating issues (if any)...")
        if 'features' in data:
            for row in data["features"]:
                issue_id = row["properties"]["id"]
                # if the issue is in the dictionary (thus has been updated), skip it for the moment.
                if not issue_id in issues:
                    geojsonarray.append(row)
                else:
                    logger.info("[GeoJSON] Issue '%d' updated.", issue_id)

        logger.info("[GeoJSON] Writing new issues...")
        for issue_id in issues: # append the remaining new issues
            issue = issues[issue_id]
            gh_issue = issue["issue"]
            geojsonarray.append(get_geojson_issue(issue, gh_issue))

        logger.info("[GeoJSON] Total issues: %d", len(geojsonarray))
        output_file.write(str('{ "type": "FeatureCollection", "features": '))
        output_file.write(json.dumps(geojsonarray, ensure_ascii=False, sort_keys=True) + "}")
    # move temp file to final one
    Path(TMPGEOJSONFILE).rename(GEOJSONFILE)

def get_csv_issue(issue, gh_issue):
    return (
        gh_issue.html_url, gh_issue.id, gh_issue.updated_at, gh_issue.created_at,
        issue["title"], issue["lat"], issue["lon"], issue["regioneIssue"], issue["provinciaIssue"],
        issue["labels"], gh_issue.milestone, issue["image"], json.dumps(issue["data"], sort_keys=True),
        gh_issue.body, gh_issue.state
    )

def get_json_issue(issue, gh_issue):
    return {
        "title":gh_issue.title,
        "number":gh_issue.number,
        "state":gh_issue.state,
        "issue":{
            "url":gh_issue.html_url,
            "id":gh_issue.id,
            "updated_at":gh_issue.updated_at.isoformat() + "+00:00",
            "created_at":gh_issue.created_at.isoformat() + "+00:00",
            "title":issue["title"],
            "lat":issue["lat"],
            "lon":issue["lon"],
            "regione":issue["regioneIssue"],
            "provincia":issue["provinciaIssue"],
            "labels":issue["labels"],
            "milestone":gh_issue.milestone.title if gh_issue.milestone else None,
            "image":issue["image"],
            "data":issue["data"],
            "body":gh_issue.body}
    }

def get_geojson_issue(issue, gh_issue):
    return {
        "type":"Feature",
        "geometry":{
            "type":"Point",
            "coordinates":[issue["lon"], issue["lat"]]},
            "properties": {
                "title": gh_issue.title,
                "number": gh_issue.number,
                "state": gh_issue.state,
                "url": gh_issue.html_url,
                "id": gh_issue.id,
                "updated_at": gh_issue.updated_at.isoformat() + "+00:00",
                "created_at": gh_issue.created_at.isoformat() + "+00:00",
                "labels": eval(issue["labels"]) if issue["labels"] else None,
                "milestone": gh_issue.milestone.title if gh_issue.milestone else None,
                "image": image,
                "data": issue["data"],
                "body": gh_issue.body,
                "regione": issue["regioneIssue"],
                "provincia": issue["provinciaIssue"]
            }
        }

if __name__ == "__main__":
    logger.info("Reading 'regioni' geo data file...")
    regioni = gpd.read_file(LIMITIPATH + "/Limiti01012019_g/Reg01012019_g/Reg01012019_g_WGS84.shp")

    regioni = gpd.GeoDataFrame(regioni)
    regioni.crs = 'epsg:23032'
    regioni = regioni.to_crs('epsg:4326')

    logger.info("Reading 'province' geo data file...")
    province = gpd.read_file(LIMITIPATH + "/Limiti01012019_g/ProvCM01012019_g/ProvCM01012019_g_WGS84.shp")

    province = gpd.GeoDataFrame(province)
    province.crs = 'epsg:23032'
    province = province.to_crs('epsg:4326')

    logger.info("Reading Github configration...")
    g = get_github_client()

    org = g.get_organization(ORG)
    r = org.get_repo(REPO_NAME)

    # Retrieve filter labels from Github repository
    filter_labels = []
    for l in FILTER_LABELS:
        try:
            ghlabel = r.get_label(l)
            filter_labels.append(ghlabel)
        except:
            pass

    logger.info("Retrieving latest updated_at timestamp from our issues file (%s)...", CSVFILE)
    latest_timestamp = get_latest_timestamp(CSVFILE)
    # we need to add one second to the latest timestamp in our issue file
    # to avoid retrieving the "last" issue we already have (in the issues file)
    last_time = latest_timestamp + datetime.timedelta(seconds=1)

    logger.info("Retrieving issues from Github (since %s)...", last_time)
    issues = r.get_issues(since=last_time, labels=filter_labels, state='all', sort='updated')
    logger.info("%d issues retrieved...", issues.totalCount)

    issuedict = {}
    geojsonarray = []

    for issue in issues:
        labels = json.dumps([l.name for l in issue.labels])
        data = {}
        lat = lon = image = regioneIssue = provinciaIssue = None

        try:
            tree = html.fromstring(issue.body)

            try:
                dataRaw = tree.xpath("//data/text()")
                dataStr = dataRaw[0] if len(dataRaw) > 0 else None
                data = json.loads(dataStr)
            except:
                pass

            try:
                yamldataRaw = tree.xpath("//yamldata/text()")
                yamldataStr = yamldataRaw[0] if len(yamldataRaw) > 0 else None
                data = yaml.safe_load(yamldataStr)
            except:
                pass
        except:
            pass

        if not data:
            logger.info("Data not found for issue %s.", issue)
            continue

        for posName in POSIZIONE_NAMES:
            if posName in data:
                try:
                    (lat, lon) = data[posName].split(" ")[:2]
                    p = Point(float(lon), float(lat))
                    for i, regione in regioni.iterrows():
                        if regione['geometry'].contains(p):
                            regioneIssue = regione["DEN_REG"]
                            break

                    for i, provincia in province.iterrows():
                        if provincia['geometry'].contains(p):
                            provinciaIssue = provincia["DEN_UTS"]
                            break

                except Exception as e:
                    logger.error("Exception: %s", e)
                break

        if "regione_manuale" in data:
            regioneIssue = data["regione_manuale"]

        if "provincia_manuale" in data:
            provinciaIssue = data["provincia_manuale"]

        if "immagine" in data:
            image = data['immagine']

        title = issue.title

        issuedict[issue.id] = {
            "issue": issue,
            "title": title,
            "lat": lat,
            "lon": lon,
            "regioneIssue": regioneIssue,
            "provinciaIssue": provinciaIssue,
            "labels": labels,
            "image": image,
            "data": data
        }
        
    write_output_files(issuedict)
    logger.info("Done.")
