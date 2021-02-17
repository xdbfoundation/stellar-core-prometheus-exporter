FROM python

WORKDIR /app

COPY . .

RUN pip install --upgrade cloudsmith-cli wheel sdist prometheus_client