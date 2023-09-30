import multiprocessing

print("Loading Gunicorn Configuration")
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count()
worker_class = "gthread"
threads = 2