#!/bin/sh

docker stop api
docker rm api

docker build -t muffin_ctf/api .

docker run -d -p 0.0.0.0:9180:9180 -p 0.0.0.0:9181:9181 -p 0.0.0.0:9182:9182 --link database --restart always --name api muffin_ctf/api
