FROM ubuntu:latest
LABEL authors="Bruno Grisolia"

ENTRYPOINT ["top", "-b"]