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

#Note: you can change this credentials in project-folder/app_rama/settings.py at the line 83 -to- 91
once configured, you don't need to do anything more.

to see the album output, take a look to localhost:8000

to see the forum scrapping output, take a look to localhost:8000/forum

for start a clean webscrap of the web site you have to run, | py injection.py (it cleans the table named Article)

For do the web srapping, you have to know the specific number on post finish, if in your forum, the last topic are in url represented as 

http://www.naczyniaki.pl/viewtopic.php?t=6000 

as example, cause i don't know which is the last topic...

you have to go 
