FROM ubuntu:22.04

ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Europe/Warsaw

RUN apt-get update && \
    apt-get install -y software-properties-common && \
    add-apt-repository ppa:deadsnakes/ppa

RUN apt-get update && \
    apt-get install -y python3.8 

RUN apt-get update && \
    apt-get install -y \
    openjdk-8-jdk \
    kotlin

RUN apt-get update && \
    apt-get install -y curl 

RUN curl -L https://services.gradle.org/distributions/gradle-7.4-bin.zip -o /tmp/gradle-7.4-bin.zip && \
    unzip -d /opt/gradle /tmp/gradle-7.4-bin.zip && \
    rm /tmp/gradle-7.4-bin.zip

ENV GRADLE_HOME=/opt/gradle/gradle-7.4
ENV PATH=$PATH:$GRADLE_HOME/bin

WORKDIR /app

COPY build.gradle /app/

RUN gradle build --no-daemon

COPY HelloWorld.java /app/
RUN javac HelloWorld.java

CMD ["java", "HelloWorld"]