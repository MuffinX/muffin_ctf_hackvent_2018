#!/bin/sh

docker stop database
docker rm database

docker build -t muffin_ctf/database .

if [ $(hostname) = "muffinhouse" ]; then
  docker run -d -p 0.0.0.0:3306:3306 -e MYSQL_DATABASE=muffin_ctf -e MYSQL_ROOT_PASSWORD=e2095f3411655f735d4d8552ef8c973268d77d49d7a404eaa8b7b14525963d52 --restart always --name database muffin_ctf/database
else
  docker run -d -e MYSQL_DATABASE=muffin_ctf -e MYSQL_ROOT_PASSWORD=e2095f3411655f735d4d8552ef8c973268d77d49d7a404eaa8b7b14525963d52 --restart always --name database muffin_ctf/database
fi
