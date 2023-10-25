# Используем базовый образ Python
FROM python:3.8

# Устанавливаем необходимые библиотеки
RUN pip install jaeger-client

# Копируем исходный код приложения в контейнер
COPY random_trace_generator.py /app/random_trace_generator.py

# Устанавливаем рабочую директорию
WORKDIR /app

# Команда для запуска приложения
CMD ["python", "random_trace_generator.py", "--jaeger.agent.host", "grafana-agent.monitoring.svc", "--jaeger.agent.port", "6831"]
