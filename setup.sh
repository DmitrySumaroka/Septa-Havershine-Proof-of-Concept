#!/bin/bash
sudo rm -rf venv;
sudo pip3 install virtualenv;
sudo chown -R $USER .
virtualenv --no-site-packages -p python3 venv;
source ./venv/bin/activate;
pip3 install -r reqs.txt;
python3 run.py ;
