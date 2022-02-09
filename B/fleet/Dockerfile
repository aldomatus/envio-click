FROM python:3.8.5-slim-buster

RUN apt install tzdata
RUN cp /usr/share/zoneinfo/America/Mexico_City /etc/localtime
RUN echo "America/Mexico_City" >  /etc/timezone
RUN apt-get -y update \
    && apt-get install -y \
        libffi-dev \
        libgdk-pixbuf2.0-0 \
        libpango1.0-0 \
        python-dev \
        python-lxml \
        shared-mime-info \
        libcairo2 \
        cron \
        rsyslog \
    && apt-get -y clean

WORKDIR /usr/src/app
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app

ADD events-cron /etc/cron.d/hello-cron
RUN chmod 0644 /etc/cron.d/hello-cron
RUN crontab /etc/cron.d/hello-cron
RUN touch /var/log/cron.log

RUN chmod +x /usr/src/app/entrypoint.sh

ENTRYPOINT ["/bin/sh","/usr/src/app/entrypoint.sh"]