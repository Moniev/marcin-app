FROM python:latest
WORKDIR /app

COPY . /app

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 3000
CMD python ./main.py