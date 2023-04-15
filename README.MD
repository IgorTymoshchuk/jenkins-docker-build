#### This repository contains:

**main.py** - python code file that does request to EC2 via AWS api using boto3 in order to get information which instance is running

**requirements.txt** - list of requirements that are needed to run python code from main.py

**dockerfile** - describes how to create an image with the main.py

**Jenkinsfile** - pipeline jenkins file that describes all building process of the image

**JenkinsfileRunner** - pipeline jenkins file that runs the built image every 5 min and displays in run log python output
