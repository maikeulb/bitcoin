#!/bin/sh
echo executing gunicorn
gunicorn -b :5000 --access-logfile - --error-logfile - bitcoin_challenge:app --timeout 120
