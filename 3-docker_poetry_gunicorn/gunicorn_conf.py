import multiprocessing

# Базовые настройки
bind = "0.0.0.0:8000"
workers = multiprocessing.cpu_count() * 2 + 1
threads = 2
worker_class = "uvicorn.workers.UvicornWorker"

# Настройки производительности
timeout = 120
keepalive = 5

# Настройки логирования
accesslog = "-"
errorlog = "-"
loglevel = "info"

# Дополнительные параметры
reload = False
preload = True

# Обработка сигналов
graceful_timeout = 30

# Ограничения
limit_request_line = 4094
limit_request_fields = 100
limit_request_field_size = 8190