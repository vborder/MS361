import os
from dotenv import load_dotenv

load_dotenv('.env')


class Config(object):
    APP_ID = os.environ.get('APP_ID')
    ENDPOINT = os.environ.get('ENDPOINT')
