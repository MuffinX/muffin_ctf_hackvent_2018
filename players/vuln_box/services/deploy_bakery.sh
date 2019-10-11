#!/bin/sh


scp -r bakery/* bakery@vuln.local:/home/bakery

scp -r "bakery/.../" bakery@vuln.local:/home/bakery
