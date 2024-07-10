FROM python:3.11

WORKDIR /app

RUN pip install pytz torch

COPY app.py .

CMD ["python3", "-u", "app.py"]
