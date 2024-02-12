ARG PYTHON_VERSION=3.11.8-alpine3.19

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies.
RUN apk add --no-cache libpq-dev gcc && \
    mkdir -p /code

WORKDIR /code
COPY . /code/
RUN pip install --upgrade pip && \
    pip install -r requirements.txt

ENV SECRET_KEY "1imTIXLDALLwpt3nSZqdlqXDC1TN0Hbb3Qwgt2ddbmJ9VvFFRw"
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "norns.wsgi"]
