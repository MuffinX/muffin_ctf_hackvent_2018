#!/bin/sh

docker stop hackvent_simulation
docker rm hackvent_simulation

docker build -t muffin_ctf/hackvent_simulation .

docker run -d -p 0.0.0.0:1337:80 --restart always --name hackvent_simulation muffin_ctf/hackvent_simulation
