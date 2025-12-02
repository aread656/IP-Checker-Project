FROM python:3.13-slim
WORKDIR /app
COPY . /app/
EXPOSE 86
CMD ["python","csv_saving.py"]