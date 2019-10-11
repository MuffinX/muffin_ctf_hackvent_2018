#!/bin/sh

docker stop checker
docker rm checker

docker build -t muffin_ctf/checker .

docker run -d --link api --link database --restart always --name checker muffin_ctf/checker
