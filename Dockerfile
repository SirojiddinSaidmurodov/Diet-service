FROM ubuntu
RUN apt update
RUN apt install -y python3
RUN apt install -y python3-pip
RUN apt install swi-prolog -y

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .

