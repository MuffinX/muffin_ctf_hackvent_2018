FROM ubuntu:latest
MAINTAINER muffinx <muffinx@openmailbox.org>

# install packages
RUN apt-get update -y && \
    apt-get install -y python3 python3-pip python3-dev libmysqlclient-dev

# install libraries
RUN pip3 install flask flask_sqlalchemy pycrypto mysqlclient tornado requests

# add api user
RUN groupadd api
RUN useradd -g api api

# import files
ADD import/ /

# own home dir
RUN chown -R api:api /home/api

# run api
USER api
ENTRYPOINT ["python3", "/home/api/api.py"]
