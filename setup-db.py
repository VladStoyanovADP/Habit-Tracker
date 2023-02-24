import psycopg2
import os

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

# Change directory to Django project directory
# os.chdir('./Habit_Tracker')

# Run migrations
os.system('python manage.py makemigrations Achievements')
os.system('python manage.py makemigrations Users')
os.system('python manage.py migrate')

# Load data from fixtures
os.system('python manage.py loaddata */fixtures/*.json')
