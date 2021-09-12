import time
import requests
import os

BASE_URL = os.environ.get('BASE_URL_OF_BOT', None)
if len(BASE_URL) == 0:
    BASE_URL = None

IS_VPS = os.environ.get('IS_VPS', 'False')
IS_VPS = IS_VPS.lower() == 'true'
if not IS_VPS and BASE_URL is not None:
    while True:
        time.sleep(600)
        status = requests.get(BASE_URL).status_code
