FROM ubuntu:latest
RUN apt-get update
RUN apt-get install -y build-essential git ruby-full ruby-bundler zlib1g-dev curl
VOLUME ["/opt"]
WORKDIR /opt
CMD [ "bundle", "install", "--path", "vendor/bundle" ]
CMD [ "bundle", "exec", "jekyll", "serve", "--force_polling", "-H", "0.0.0.0", "-P", "4000" ]