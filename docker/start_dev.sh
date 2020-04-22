#!/bin/bash
bundle install --path vendor/bundle
bundle exec jekyll serve --force-polling -H 0.0.0.0 --incremental
