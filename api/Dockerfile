FROM python:3.7.4
WORKDIR ./api
COPY  requirements.txt ./
RUN pip install -r requirements.txt
COPY . .
CMD ["gunicorn", "run"]
