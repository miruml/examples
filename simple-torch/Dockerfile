FROM nvcr.io/nvidia/l4t-pytorch:r35.2.1-pth2.0-py3

WORKDIR /app

RUN pip install pytz 

COPY app.py .

CMD ["python3", "-u", "app.py"]
