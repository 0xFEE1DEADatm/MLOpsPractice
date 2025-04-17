# Используем официальный Python 3.10 slim образ как базовый
FROM python:3.10-slim

# Устанавливаем рабочую директорию в контейнере
WORKDIR /app

# Копируем локальные файлы в контейнер
COPY . /app/

# Обновляем пакеты и устанавливаем необходимые библиотеки для компиляции
RUN apt-get update && apt-get install -y \
    libpq-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Открываем порт 8000 для работы FastAPI
EXPOSE 8000

# Запускаем FastAPI сервер через uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
