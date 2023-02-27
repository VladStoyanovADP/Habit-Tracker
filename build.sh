set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

python << EOF
import psycopg2
import os

dbname = os.environ.get('host_test')
dbuser = os.environ.get('host_test_user')
dbpassword = os.environ.get('oPXoTh4xYnYjO5Kr2uTcNtUw70HufxrO')
dbhost = os.environ.get('dpg-cfs9odhmbjshr9nevltg-a')

conn = psycopg2.connect(
    dbname=dbname, user=dbuser, password=dbpassword, host=dbhost, port='5432'
)
conn.autocommit = True

cursor = conn.cursor()
cursor.execute("DROP DATABASE IF EXISTS habit_tracker_db")

sql = '''CREATE DATABASE habit_tracker_db''';

cursor.execute(sql)
print("Database created successfully......")

conn.close()
EOF

python manage.py makemigrations Achievements
python manage.py makemigrations Users
python manage.py migrate

python manage.py loaddata */fixtures/*.json