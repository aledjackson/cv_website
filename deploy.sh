export DOMAIN="enter your domain here"
export DJANGO_DEBUG=false
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py collectstatic
python3 manage.py check --deploy