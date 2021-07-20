"""
Created by samy on 19-Jul-2021
Function to define connection
"""

import pyodbc

def get_connection():
	sql_conn = None
	try:
		conn_str="DRIVER={SQL Server};SERVER=localhost;DATABASE=Springboard;Trusted_Connection=yes"
		sql_conn = pyodbc.connect(conn_str)
		#cursor = sql_conn.cursor()
	except Exception as error:
		print('Error while connecting to database', error)
	return sql_conn