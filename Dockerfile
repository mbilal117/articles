FROM python:3.8
RUN apt-get update && apt-get install -y gettext

# set the working directory
WORKDIR /app
# copy the repository files to it
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt
RUN python manage.py collectstatic --noinput

EXPOSE 80

CMD gunicorn --bind=0.0.0.0:80 --forwarded-allow-ips="*" articles.wsgi