set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

PGPASSWORD=oPXoTh4xYnYjO5Kr2uTcNtUw70HufxrO psql -U host_test_user -h dpg-cfs9odhmbjshr9nevltg-a host_test -c 'DROP TABLE IF EXISTS django_migrations'
PGPASSWORD=oPXoTh4xYnYjO5Kr2uTcNtUw70HufxrO psql -U host_test_user -h dpg-cfs9odhmbjshr9nevltg-a host_test -c "DROP TABLE IF EXISTS django_admin_log"
PGPASSWORD=oPXoTh4xYnYjO5Kr2uTcNtUw70HufxrO psql -U host_test_user -h dpg-cfs9odhmbjshr9nevltg-a host_test -c "DROP TABLE IF EXISTS django_content_type CASCADE"
PGPASSWORD=oPXoTh4xYnYjO5Kr2uTcNtUw70HufxrO psql -U host_test_user -h dpg-cfs9odhmbjshr9nevltg-a host_test -c "DROP TABLE IF EXISTS django_session"
PGPASSWORD=oPXoTh4xYnYjO5Kr2uTcNtUw70HufxrO psql -U host_test_user -h dpg-cfs9odhmbjshr9nevltg-a host_test -c 'DROP TABLE IF EXISTS "Users_habits"'
PGPASSWORD=oPXoTh4xYnYjO5Kr2uTcNtUw70HufxrO psql -U host_test_user -h dpg-cfs9odhmbjshr9nevltg-a host_test -c 'DROP TABLE IF EXISTS "Users_rewards"'
PGPASSWORD=oPXoTh4xYnYjO5Kr2uTcNtUw70HufxrO psql -U host_test_user -h dpg-cfs9odhmbjshr9nevltg-a host_test -c 'DROP TABLE IF EXISTS "Users_person_achievements"'
PGPASSWORD=oPXoTh4xYnYjO5Kr2uTcNtUw70HufxrO psql -U host_test_user -h dpg-cfs9odhmbjshr9nevltg-a host_test -c 'DROP TABLE IF EXISTS "Users_person"'
PGPASSWORD=oPXoTh4xYnYjO5Kr2uTcNtUw70HufxrO psql -U host_test_user -h dpg-cfs9odhmbjshr9nevltg-a host_test -c 'DROP TABLE IF EXISTS "Achievements_achievements"'


python manage.py makemigrations Achievements
python manage.py makemigrations Users
python manage.py migrate

python manage.py loaddata */fixtures/*.json