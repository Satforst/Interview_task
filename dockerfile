FROM alpine:3.12

# set working directory
WORKDIR /app/

# copy all files into working dir
COPY / .

# Install python/pip and requirements
ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install -r requirements.txt

# run application
CMD ["python3", "main.py"]