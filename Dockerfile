FROM python:3.6

MAINTAINER Your Name "ak@gmail.com"

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

WORKDIR /app

COPY . /app

RUN pip3 --no-cache-dir install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python3"]
CMD ["app.py"]
