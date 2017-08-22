FROM python:2-alpine
WORKDIR /opt/sf-web
COPY sf-web/ .
COPY requirements.txt ./
RUN apk -U upgrade --no-cache
RUN apk --update add build-base libffi-dev openssl-dev python-dev py-pip
RUN pip install --no-cache-dir -r requirements.txt
ENV FLASK_APP=/opt/sf-web/sf-web.py
EXPOSE 5000
CMD ["flask", "run", "--host=0.0.0.0"]
