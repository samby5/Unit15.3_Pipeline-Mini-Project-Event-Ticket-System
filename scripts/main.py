import dataConnections
import sql_functions

sf=sql_functions
dc= dataConnections.get_connection()

sf.load_third_party(dc,"third_party_sales_1.csv")
print("Here are the most popular tickets in the past month:")
for i in sf.query_popular_tickets(dc):
	print('-'+str(i[0]))
