import json

import requests
import yaml

URL_API = "http://localhost:5000"

session = requests.Session()
with open('dw.yaml') as demo_dw:
    dw_model = yaml.load(demo_dw.read())

for table in dw_model.get('tables'):
    r = session.post(
        f"{URL_API}/table",
        data=json.dumps(table),
        headers={'content-type': 'application/json'})
    print(r.json())

for relation in dw_model.get('relationships'):
    r = session.post(
        f"{URL_API}/relationship",
        data=json.dumps(relation),
        headers={'content-type': 'application/json'})
    print(r.json())
