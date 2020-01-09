FROM python:3.7.4
WORKDIR /usr/src/app
ADD  requirements.txt ./
RUN pip install -r requirements.txt
ADD . .
#CMD [ "uwsgi", "app.ini" ]
