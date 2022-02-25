#! /bin/bash
source path/to/folder/CSPB-Pathways/venv/bin/activate
# sql database not set up yet
# export DATABASE_URL="postgresql://localhost/kinsey
cd path/to/folder/CSPB-Pathways
export FLASK_APP=project.py
export FLASK_DEBUG=1
flask run
