SQL_DATABASE = input('Please enter SQL_DATABASE: ')
SQL_USER = input('Please enter SQL_USER: ')
SQL_PASSWORD = input('Please enter SQL_PASSWORD: ')
#SQL_HOST = input('Please enter SQL_HOST: ')
#SQL_PORT = input('Please enter SQL_PORT: ')

with open('.env', 'w') as file:
    file.writelines('SQL_ENGINE=django.db.backends.postgresql\n')
    file.writelines(f'SQL_DATABASE={SQL_DATABASE}\n')
    file.writelines(f'SQL_USER={SQL_USER}\n')
    file.writelines(f'SQL_PASSWORD={SQL_PASSWORD}\n')
    file.writelines(f'SQL_HOST=db\n')
    file.writelines(f'SQL_PORT=5432\n')
    file.close()

with open('Dockerfile', 'w') as file:
    file.writelines(f'''
FROM python:3.10.10-alpine
#FROM ubuntu:22.04

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV SQL_ENGINE django.db.backends.postgresql
ENV SQL_DATABASE {SQL_DATABASE}
ENV SQL_USER {SQL_USER}
ENV SQL_PASSWORD {SQL_PASSWORD}
ENV SQL_HOST db
ENV SQL_PORT 5432


#RUN apk add alpine-sdk
#RUN apk add gcc

RUN pip install --upgrade pip

COPY ./requirements.txt .

RUN pip install -r requirements.txt

# copy project
COPY . .
''')
    file.close()



with open('docker-compose.yml', 'w') as file:
    file.writelines(f'''
version: '3.10'

services:
  db:
    container_name: hhtask_db
    image: postgres:14.7-alpine
    networks:
      - hhtask_net
    volumes:
      - postgres_data:/var/lib/postgresql/data/
    environment:
      - POSTGRES_DB={SQL_DATABASE}
      - POSTGRES_USER={SQL_USER}
      - POSTGRES_PASSWORD={SQL_PASSWORD}
    ports:
      - '0.0.0.0:5455:5432'
  
  
  web:
    container_name: hhtask_django
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/usr/src/app
    networks:
      - hhtask_net
    ports:
      - '8080:8000'
    env_file:
      - .env
    depends_on:
      - db


volumes:
  postgres_data:


networks:
  hhtask_net:
''')
    file.close()
    
    