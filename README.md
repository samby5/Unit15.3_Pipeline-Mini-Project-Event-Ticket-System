# Events Tickets System
Load Events Tickets System from CSV into SQL Server Table and output the result of opular events on-Screen

## Scripts
Below is list of scripts needed for running the python based application
- connect.py
- dataConnections.py
- main.py
- sql_functions.py
## Steps to run
The main entry point to the application is through the main.py. It calls other sql functions through the module 
listed in the sql_functions.py
1. Copy the folder structure to your local
2. Execute the sql script located in /scripts/third_party_sales.sql in sql server to create the table third_party_sales in Springboard.dbo schema. If the DB.Schema doesnt exist, create it your db server 
3. copy the folders /scripts and /data to your local environment. The script uses relative path to traverse folders.
4. Open Python IDE(ex: VS Code) and run the execute main.py to load the data into sql server table and display the popular events by finding the most top-selling tickets for the
past month.


