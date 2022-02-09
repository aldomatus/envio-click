#!/bin/bash

alembic upgrade head

#cron
set -m
printenv | sed 's/^\(.*\)$/export \1/g' > /root/project_env_tmp.sh && sed -e 's/=/="/g; s/$/"/g' /root/project_env_tmp.sh > /root/project_env.sh
chmod +x /root/project_env.sh
service rsyslog start
service cron start
newrelic-admin run-program python manage.py run -h 0.0.0.0