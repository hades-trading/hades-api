GUNICORN_CMD_ARGS="--timeout 600 --access-logfile /tmp/app_access.log --error-logfile /tmp/app_error.log -c /opt/startup/gunicorn.conf.py --chdir=$APP_PATH --workers 4 --worker-class uvicorn.workers.UvicornWorker" gunicorn main:app

