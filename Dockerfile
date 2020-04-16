FROM python:3.7-slim-buster

COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
RUN pip install -r requirements.txt

COPY ./app /app
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]