python env_setup.py
docker build -t hhtask .
docker run hhtask
docker-compose build
docker-compose run web python manage.py migrate
docker-compose up