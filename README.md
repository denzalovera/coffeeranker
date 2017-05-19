# README #

## CoffeeRanker WebApp ##

A Simple CMS Built with Flask.

### What is this repository for? ###

* Quick summary
* Version 0.1

### How do I get set up? ###

* install dependencies listed in requirements.txt
* db setup:
    * create instance directory
    * Database configuration
        * create `config.py` script
        * format: `mysql://username:password@localhost/db_name`
    * for mysql-python using windows platform install:
        * `pip install misc/MySQL_python-1.2.5-cp27-none-win32.whl`
    * on server (using vagrant):
        * update `etc/mysql/my.conf`
        * comment out `bind-address`
    * open `mysql` using root access and run query:
        * `USE database_of_app`
        * `'GRANT ALL ON *.* to root@'%' IDENTIFIED BY 'pass''`
        * `FLUSH PRIVILEGES`
* execute script ./runner.sh to start server

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact