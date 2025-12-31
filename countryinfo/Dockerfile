FROM ubuntu:24.04
RUN apt-get update
RUN apt-get install -y g++
WORKDIR /app
COPY server.cpp .
COPY countryinfo.h .
COPY countryinfo.cpp .
COPY httplib.h .
RUN g++ -std=c++17 -O2 server.cpp countryinfo.cpp -o server
EXPOSE 84
CMD ["./server"]