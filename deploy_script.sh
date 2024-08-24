#!/bin/bash

cd /path/to/your/project
git pull origin main
source antigikes/bin/activate
pip install -r requirements.txt
bash start
