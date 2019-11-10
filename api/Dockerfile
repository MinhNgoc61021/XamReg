FROM python:3.7.4
WORKDIR /app
ADD  requirements.txt /app
RUN pip install -r /app/requirements.txt
ADD . /app
#CMD [ "uwsgi", "app.ini" ]
