1] git clone https://github.com/kevinabadromero/transfer_db_project.git

2]cd to transfer_db_project

First, you need to solve install all dependencies

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

#Note: you can change this credentials in project-folder/app_rama/settings.py at the line 
