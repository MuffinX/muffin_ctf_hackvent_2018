#!/bin/sh

scp -r container_web/ muffinx@whale.hacking-lab.com:/home/muffinx/

# ssh -t muffinx@whale.hacking-lab.com '/bin/sh -c "sudo /home/muffinx/container_web/start.sh"'
