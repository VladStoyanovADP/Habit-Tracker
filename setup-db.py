import psycopg2

#establishing the connection
conn = psycopg2.connect(
   database="postgres", user='', password='', host='localhost', port= '5432'
)
conn.autocommit = True

#Creating a cursor object using the cursor() method
cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS habit_tracker_db")
#Preparing query to create a database
sql = '''CREATE database habit_tracker_db''';

#Creating a database
cursor.execute(sql)
print("Database created successfully........")

#Closing the connection

conn.close()