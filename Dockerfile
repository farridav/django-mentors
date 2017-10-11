FROM alpine:3.1

RUN apk add --update python py-pip
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD . /app

EXPOSE 8000

CMD ["/app/start.sh"]
