#!/bin/bash
gunicorn --workers 3 \
         --bind unix:./app.sock \
         -c conf/gunicorn/gunicorn.py \
         --worker-class=gevent \
         --worker-connections=1000 wsgi:app --daemon


nginx -g 'daemon off;'
