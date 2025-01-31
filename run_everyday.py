import requests
import os
print(requests.post("https://swdc.pythonanywhere.com/action/run-function", json = {"secret_key": os.getenv('RUN_FUNCTION_PWD')}).text)