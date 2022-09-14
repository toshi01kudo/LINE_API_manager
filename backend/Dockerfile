FROM python:3.10-alpine
RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt /app/

RUN pip install -r requirements.txt
ENTRYPOINT ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "19251"]
