#!/usr/loca/bin/python3
from time import sleep

FILE = "/home/file.txt"
#FILE = "/home/ubuntu/docker-exercises/new-python-docker/file.txt"

num = 1
while True:
    with open(FILE, 'a') as myfile:
        line = "Line number " + str(num) + "\n"
        myfile.write(line)
    num += 1
    sleep(2)
