FROM nvcr.io/nvidia/l4t-pytorch:r35.2.1-pth2.0-py3 

WORKDIR /app

COPY app.py .

# Command to run the demo.py script
CMD ["python3", "demo.py"]
