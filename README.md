# RestDemo2
RestDemo2 is the second version of RestDemo.  RestDemo manages "snippets" ( code snippets ).  The table snippets resides in the restdemo schema.  Snippet attributes are:

id, 
created, 
title, 
code, 
linenos, 
language, 
style, 
highlighted, 
owner_id


RestDemo has one restful resource "Snippet". Snippets can be created, updated, deleted, listed. Unauthenticated users can only read snippets. Any authenticated user can read any snippet. But an authenticated user can only update and delete his own snippets. Snippets are saved in the snippets table in the restdemo schema. RestDemo relies on a postgres database. Path to list snippets is http://localhost:8002/snippets Path to list snippet with id = 1 is http://localhost:8000/snippets/1.  The port number can be dynamically set in the supervisor configuration file.


Steps to build the project:

1. Install postgres 12.1
2. Install nginx 16.1

Instructions for installing and configuring postgres, nginx, supervisor, gunicorn are located in the project folders

3. Install python 3.6.3
4. Install all dependent libraries with pip install. All libraries are listed in requirements.txt except for Supervisor, which is installed system wide with yum install.

Supervisor is a graphical tool that allows to start/stop/refresh the RestDemo application and to view logs using a graphical interface instead of command line.

5. Run the sql statements to configure postgres ( Create roles, users, privilegies, schema ) in setuprestdemo.sql, included in the project folder.

6. run the command: python manage.py migrate to build the database.
7. run the command: python manage.py runserver 
8. To run the unit tests run the command python manage.py test --keepdb
9. To run the BDD test run the command python manage.py behave --keepdb
