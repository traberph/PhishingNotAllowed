import requests
from fake_useragent import UserAgent
import faker
import csv
import random
import os
from dotenv import load_dotenv


load_dotenv()
URL = os.getenv('URL')
UNI = os.getenv('UNI')
PASS_FIELD = os.getenv('PASS_FIELD', 'Password')
USR_FIELD = os.getenv('USR_FIELD', 'Username')



ua = UserAgent()
fake = faker.Faker(['de_DE', 'en_US'])

# load password list
with open('pwd.csv') as f:
    reader = csv.reader(f)
    pwd_list = list(reader)


# send request
def send():
    header = {'User-Agent': str(ua.random)}
    form_data = {
        USR_FIELD: get_email(),
        PASS_FIELD: get_password()
    }
    response = requests.post(URL, data=form_data, headers=header)


    # prospone console output if MUTE is set
    if os.getenv('MUTE') is None:
        print(f'send: {response.request.body}, received: {response.status_code}', flush=True)

    return response.status_code


# fake emails
def get_email():
    fst = fake.first_name().lower()
    sec = fake.last_name().lower()
    return f'{fst}.{sec}@{UNI}'


# fake passwords
def get_from_list():
    return random.choice(pwd_list)[1]
def generate():
    return fake.password(random.randint(10, 26))
def get_password():
    return generate() if random.choice([True, False, False, False]) else get_from_list()
  


# main loop
result = {}
counter = 0
print(f'this program will send requests to {URL}', flush=True)
while True:
    try:
        code = send()
    except Exception as e:
        print(e)
        code = -1
    result[code] = result.get(code, 0) + 1
    counter += 1

    if counter >= 25:
        print('---')
        print(result)
        print('---')
        counter = 0