FROM python:latest

COPY requirements.txt /src/

WORKDIR /src

RUN pip install -U pip
RUN pip install -r requirements.txt

COPY . /src/

EXPOSE 8000

CMD [ "fastapi", "run", "./App/application.py" ]