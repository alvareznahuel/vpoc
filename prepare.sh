#!/bin/sh
virtualenv venv
pip3 install requests[security]
pip3 install flask
pip3 install gunicorn
pip3 install Flask-RESTful
pip3 install Flask-SQLAlchemy
pip3 freeze > requirements.txt 