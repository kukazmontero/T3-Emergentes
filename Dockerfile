FROM python:alpine3.18

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask python-dotenv 
RUN pip install key_generator

RUN apk add --no-cache sqlite

EXPOSE 5000

CMD ["python", "app.py"]
