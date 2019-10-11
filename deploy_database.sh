#!/bin/sh

scp -r container_database/ muffinx@whale.hacking-lab.com:/home/muffinx/

# ssh -t muffinx@whale.hacking-lab.com '/bin/sh -c "sudo /home/muffinx/container_database/start.sh"'
