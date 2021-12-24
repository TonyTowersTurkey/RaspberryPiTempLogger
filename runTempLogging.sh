#!/bin/bash


echo starting python now
source /home/pi/dev/tempLogging/tempLogger/bin/activate 
echo activated venv
sudo /home/pi/dev/tempLogging/tempLogger/bin/python3 /home/pi/dev/tempLogging/tempLogging.py &
#sudo python3 /home/pi/path.py &
