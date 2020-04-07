FROM python:3.7.6

ENV PORT 8081

COPY ./requirements.txt /app/requirements.txt

COPY ./app/templates /app/templates

WORKDIR /app

RUN pip install -r requirements.txt

ENTRYPOINT [ "python" ]
CMD [ "app.py" ]