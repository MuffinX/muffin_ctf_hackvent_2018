FROM ubuntu:latest
MAINTAINER muffinx <muffinx@openmailbox.org>

# install packages
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev libmysqlclient-dev

# install libraries
RUN pip install flask flask_sqlalchemy pycrypto mysql-python requests

# add web user
RUN groupadd checker
RUN useradd -g checker checker

# import files
ADD import/ /

# own home dir
RUN chown -R checker:checker /home/checker

# run flask
USER checker
ENTRYPOINT ["python", "/home/checker/checker.py"]
