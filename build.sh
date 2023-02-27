set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

PGPASSWORD=oPXoTh4xYnYjO5Kr2uTcNtUw70HufxrO psql -U host_test_user -h dpg-cfs9odhmbjshr9nevltg-a host_test -c 'DROP SCHEMA public CASCADE;'



python manage.py makemigrations Achievements
python manage.py makemigrations Users
python manage.py migrate

python manage.py loaddata */fixtures/*.json