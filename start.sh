#! /bin/bash
source path/to/folder/CSPB-Pathways/venv/bin/activate
# sql database not set up yet
# export DATABASE_URL="postgresql://localhost/kinsey
cd path/to/folder/CSPB-Pathways
source venv/bin/activate
export FLASK_APP=planner.py
export FLASK_DEBUG=1
flask run

# flask db init
# flask db migrate
# flask db upgrade