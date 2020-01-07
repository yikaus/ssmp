FROM alpine:3

RUN echo "@testing http://dl-cdn.alpinelinux.org/alpine/edge/testing" >> /etc/apk/repositories \
    && apk add --no-cache py3-pandas@testing \
    && pip3 install ssmp==0.0.6

ENTRYPOINT ["ssmp"]
