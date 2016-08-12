FROM alpine:3.3

RUN apk update && apk add coreutils python3
RUN python3 -m ensurepip --upgrade
RUN pip3 install websockets==3.1

COPY app.py /app.py

CMD ["python3", "-u", "/app.py"]
