1] git clone https://github.com/kevinabadromero/transfer_db_project.git

2]cd to transfer_db_project

First, you need to solve install all dependencies
      * pip install django
      * pip install bs4
      * pip install requests_html
      * pip install os
      
      
      
in terminal or mysql console (i'm using mariadb) type this
--> CREATE DATABASE phpbb;
--> CONNECT phpbb;
--> source ./file/path/to/aphpbb.sql
--> it's all for mysql

#Note: the aphpbb.sql is on root of project

you have to configure your Database settings, in it model i'm using mysql and my credentials for connnect django to mysql are :
    * kevin <-- username
    * localhost <-- host
    * hola123 <-- password
    * phpbb <-- Database Name

#Note: you can change this credentials in project-folder/app_rama/settings.py at the line 83 -to- 91
once configured, you don't need to do anything more.

to see the album output, take a look to localhost:8000

to see the forum scrapping output, take a look to localhost:8000/forum

for start a clean webscrap of the web site you have to run, | py injection.py (it cleans the table named Article)

For do the web srapping, you have to run | py webscrap.py

it script will go to every post in website and clone it in db, you have to be pacient for it to end
