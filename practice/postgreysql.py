import psycopg2

# con = connect
con = psycopg2.connect(
	database = "example",
	user = "postgres",
	password = "cp12345",
	host = "localhost",
	port = '5432'
	)
cursor_obj = con.cursor()
cursor_obj.execute("SELECT *FROM bike_details")
result = cursor_obj.fetchall()
print("Result Set: ", "\n", result)

