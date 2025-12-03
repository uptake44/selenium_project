FROM python:3.13-slim

RUN apt-get update && apt-get install -y chromium --no-install-recommends \
    && apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["pytest"]
CMD ["tests/frontend/"]
