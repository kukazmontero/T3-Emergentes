FROM python:3.8-slim-buster

EXPOSE 5000

WORKDIR /app

COPY . .

RUN pip install flask \
pip install flask_httpauth \
pip install jsonify \
pip install key-generator


ENTRYPOINT [ "python3" ]

CMD [ "app.py"]