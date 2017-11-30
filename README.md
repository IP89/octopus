# Octopus Test


## Install

Go into _tornado-1.2.1_ and run:

* **python setup.py install**
* **python setup.py build**


Then you can go to the root and run:

* **sudo pip install BeautifulSoup4**
* **sudo pip install mysqlclient**




## SETUP DB

run **mysql** and then:

* **CREATE DATABASE octupus_sql;**
* **use octupus_sql;**
* **CREATE TABLE words_list (id VARCHAR(128) NOT NULL, word VARCHAR(64) NOT NULL, count INT NOT NULL, PRIMARY KEY (id));**



## RUN THE APP

* from the root just run **python main.py**
* Access the main page at **localhost:8888** and the admin page at **localhost:8888/html**



## Problems found

* Regarding _ The word itself is saved in a column that has asymmetrical encryption, and you are saving the encrypted version of the word._ I didn't get how/why using and RSA type authentication would be a good thing interacting with the DB. I ended up using a simple BASE64 authentication just because, I guess the point is to not have raw data (although this is clearly a less safe way).

* About the hosting this on the cloud, I tried google cloud but when setting up the trial period google doesn't let me change the account type to Individual (only Company) and because of that I can't use it. If you have any ideas on what's happening I'm more than welcome to set it up there.