# gunicorn_conf.py
bind = "0.0.0.0:8000"
workers = 4
worker_class = "uvicorn.workers.UvicornWorker"
loglevel = "info"
accesslog = "-"  # Log to stdout
errorlog = "-"   # Log to stdout
