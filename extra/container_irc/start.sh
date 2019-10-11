#!/bin/sh

docker stop irc
docker rm irc

docker build -t muffin_ctf/irc .

docker run -p 0.0.0.0:6667:6667 --ulimit nproc=512 -d --restart always --name irc muffin_ctf/irc
