## :satellite: Python_Object_Relational_Mapping

This project demonstrates the use of SQLAlchemy, a powerful Object-Relational Mapping (ORM) library for Python. The project focuses on creating a script that lists all State and corresponding City objects from a MySQL database.
The main purpose of this project is to showcase how SQLAlchemy can be used to interact with a database and perform ORM operations. The script retrieves State and City objects from the database, establishes relationships between them, and displays the results.

## :file_folder: To install and activate venv use:
```
$ sudo apt-get install python3.8-venv
$ python3 -m venv venv
$ source venv/bin/activate
```
## :file_folder: To install MySQLdb module use:
Fo installing MySQLdb, you need to have MySQL installed.
```
$ sudo apt-get install python3-dev
$ sudo apt-get install libmysqlclient-dev
$ sudo apt-get install zlib1g-dev
$ sudo pip3 install mysqlclient
$ python3
>>> import MySQLdb
>>> MySQLdb.version_info
(2, 0, 3, 'final', 0)
```
## :file_folder: To Install SQLAlchemy module use:
```
$ sudo pip3 install SQLAlchemy
$ python3
>>> import sqlalchemy
>>> sqlalchemy.__version__
'1.4.22'
```
