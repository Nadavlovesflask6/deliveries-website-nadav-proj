FROM python:3.10-slim

WORKDIR /Deliveries-Website

RUN pip install Flask flask_sqlalchemy flask_login psycopg2-binary

COPY . . 

CMD python server.py

# Flask_RESTful
# Flask_Cors