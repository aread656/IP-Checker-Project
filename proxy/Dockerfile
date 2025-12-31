FROM python:3.13-slim
WORKDIR /src
COPY . /src
RUN pip install requests
EXPOSE 8080
CMD ["python","rev_proxy.py"]