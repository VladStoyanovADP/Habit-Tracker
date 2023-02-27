set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

PGPASSWORD=oPXoTh4xYnYjO5Kr2uTcNtUw70HufxrO psql -h dpg-cfs9odhmbjshr9nevltg-a.frankfurt-postgres.render.com -U host_test_user -c "DROP DATABASE IF EXISTS host_test"
PGPASSWORD=oPXoTh4xYnYjO5Kr2uTcNtUw70HufxrO psql -h dpg-cfs9odhmbjshr9nevltg-a.frankfurt-postgres.render.com -U host_test_user -c "CREATE DATABASE host_test"

python manage.py makemigrations Achievements
python manage.py makemigrations Users
python manage.py migrate

python manage.py loaddata */fixtures/*.json