FROM python:3.7.9-stretch

WORKDIR /app

ADD . /app

#COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

#COPY . .

#CMD [ "python", "./your-daemon-or-script.py" ]
CMD ["uwsgi", "app.ini"]