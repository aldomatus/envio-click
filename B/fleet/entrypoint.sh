#!/bin/bash

alembic upgrade head
newrelic-admin run-program python manage.py run -h 0.0.0.0