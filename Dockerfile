FROM python:3.8
RUN apt-get update && apt-get install -y gettext

# set the working directory
WORKDIR /app
# copy the repository files to it
COPY . /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

CMD gunicorn --bind=0.0.0.0:8080 --forwarded-allow-ips="*" articles.wsgi