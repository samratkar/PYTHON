import pymysql
#create a connection object conn
conn = pymysql.connect(host = 'localhost', user = 'root', passwd = 'rootpasswordgiven', db = 'information_schema')
#create a cursor object c
c = conn.cursor()
#execute a query
c.execute ("show databases;")

#fetching al the rows
all_rows = c.fetchall()

print(type(all_rows))
print(all_rows)

c.execute("select * from ENGINES")
all_rows = c.fetchall()
print(type(all_rows))
print(all_rows)
