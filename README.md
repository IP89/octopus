# Octopus Test


## Install

Go into _tornado-1.2.1_ and run:
**python setup.py install**
**python setup.py build**

Then you can go to the root and run:
**sudo pip install BeautifulSoup4**
**sudo pip install mysqlclient**



## SETUP DB
run **mysql** and then
**CREATE DATABASE octupus_sql;**
**use octupus_sql;**
**CREATE TABLE words_list (id VARCHAR(128) NOT NULL, word VARCHAR(64) NOT NULL, count INT NOT NULL, PRIMARY KEY (id));**


## RUN THE APP
from the root just run **python main.py**
Access the main page at **localhost:8888** and the admin page at **localhost:8888/html**