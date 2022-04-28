#! /bin/bash
source path/to/folder/CSPB-Pathways/venv/bin/activate
# sql database not set up yet
# export DATABASE_URL="postgresql://localhost/kinsey
# python3 -m venv venv
cd path/to/folder/CSPB-Pathways
source venv/bin/activate
export FLASK_APP=planner.py
export FLASK_DEBUG=1
flask run

# flask db init
# flask db migrate
# flask db upgrade

# https://cspb-pathways.herokuapp.com/ | https://git.heroku.com/cspb-pathways.git
# heroku addons:add heroku-postgresql:hobby-dev
# Created postgresql-defined-50899 as DATABASE_URL
# Use heroku addons:docs heroku-postgresql to view documentation
# tutorial for heroku: https://medium.com/@gitaumoses4/deploying-a-flask-application-on-heroku-e509e5c76524