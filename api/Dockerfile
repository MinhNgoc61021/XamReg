FROM python:3.7.4
WORKDIR /usr/src/app
COPY  requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
#CMD [ "uwsgi", "app.ini" ]
