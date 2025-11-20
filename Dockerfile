FROM eclipse-temurin:21-jdk
WORKDIR /app
COPY . /app
RUN javac *.java
EXPOSE 83
CMD ["java","Server"]