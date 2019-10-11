#!/bin/sh

scp -r container_api/ muffinx@whale.hacking-lab.com:/home/muffinx/

# ssh -t muffinx@whale.hacking-lab.com '/bin/sh -c "sudo /home/muffinx/container_api/start.sh"'
