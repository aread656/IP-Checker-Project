FROM python:3.13-slim
WORKDIR /src
COPY . /src
RUN pip install json http.server urllib requests
CMD ["python","rev_proxy.py"]