FROM ubuntu:latest
MAINTAINER muffinx <muffinx@openmailbox.org>

# install packages
RUN apt-get update -y && \
    apt-get install -y python-pip python-dev libmysqlclient-dev

# install libraries
RUN pip install flask flask_sqlalchemy pycrypto mysql-python requests

# add web user
RUN groupadd web
RUN useradd -g web web

# import files
ADD import/ /

# own home dir
RUN chown -R web:web /home/web

# run flask
USER web
ENTRYPOINT ["python", "/home/web/web.py"]
