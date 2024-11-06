FROM python:3.12-bookworm

WORKDIR /app

COPY pwd.csv pwd.csv
COPY req.txt req.txt
RUN pip install -r req.txt

COPY send.py send.py

COPY .env .env

CMD ["python3", "send.py"]