FROM python:3.13-slim
WORKDIR /src
COPY . /src
RUN pip install flask flask-cors
CMD ["python","server.py"]