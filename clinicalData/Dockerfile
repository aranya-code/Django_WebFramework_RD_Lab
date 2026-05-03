FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .

# Install the system dependencies required to build mysqlclient
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        pkg-config \
        default-libmysqlclient-dev \
    # Clean up the apt cache to keep the image size small
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]




