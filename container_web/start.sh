#!/bin/sh

docker stop web
docker rm web

docker build -t muffin_ctf/web .


docker run -d -p 0.0.0.0:9280:9280 --link api --link database --restart always --name web muffin_ctf/web
