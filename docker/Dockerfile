FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y build-essential git ruby-full ruby-bundler zlib1g-dev curl
RUN gem install bundler -v 1.17.3
VOLUME ["/opt"]
WORKDIR /opt
COPY start_dev.sh /bin/start_dev.sh
RUN chmod +x /bin/start_dev.sh
CMD [ "start_dev.sh" ]