import os
from pathlib import Path
#in_loc= r"C:\\Users\\samy8\\Desktop\\Work Lab\\SpringBoard\\github\\uNIT15.3_Pipeline Mini-Project Event Ticket System\\data\\"

path = Path(__file__).parent.parent
in_loc= str(path)+'\\data\\'

def load_third_party(conn, file_path_csv):
# Iterate through the CSV file and execute insert statement
	cursor = conn.cursor()
	with open(in_loc+file_path_csv,"r") as f:
		for line in f:
			t=tuple(line.split(','))
			cursor.execute("INSERT INTO Springboard.dbo.third_party_sales VALUES (?,?,?,?,?,?,?,?,?,?)", (int(t[0]),t[1],int(t[2]),t[3],t[4],t[5],t[6],int(t[7]),t[8],int(t[9])))
		conn.commit()
		cursor.close()


def query_popular_tickets(conn):
# Get the most popular ticket in the past month
	cursor = conn.cursor()
	sql_statement = "select a.event_name from (select event_name, sum(num_tickets) nt from third_party_sales where month(event_date) = 9  group by event_name ) a order by nt desc "
	cursor.execute(sql_statement)
	records = cursor.fetchall()
	cursor.close()
	return records