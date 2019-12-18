FROM python:3.6
RUN mkdir /workspace
WORKDIR /workspace
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
