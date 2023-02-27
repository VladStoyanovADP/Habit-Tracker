set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

export PGPASSWORD = oPXoTh4xYnYjO5Kr2uTcNtUw70HufxrO
psql -U host_test_user -h dpg-cfs9odhmbjshr9nevltg-a -c "DROP DATABASE IF EXISTS host_test"
psql -U host_test_user -h dpg-cfs9odhmbjshr9nevltg-a -c "CREATE DATABASE host_test"

python manage.py makemigrations Achievements
python manage.py makemigrations Users
python manage.py migrate

python manage.py loaddata */fixtures/*.json