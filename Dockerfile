# pull official base image
FROM python:3.11.7-alpine3.19

# set work directory
WORKDIR /usr/src/app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy project
COPY . .

# copy entrypoint.sh
RUN \
 pip install --upgrade pip \
 && pip install -r requirements.txt \
 && pip install -r requirements-server.txt \
 && sed -i 's/\r$//g' /usr/src/app/entrypoint.sh \
 && chmod +x /usr/src/app/entrypoint.sh

# expose port
EXPOSE 8080/TCP

# run entrypoint.sh
ENTRYPOINT ["/usr/src/app/entrypoint.sh"]
