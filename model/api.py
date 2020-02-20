import yaml
from eve import Eve

with open('domain.yaml') as fdomain:
    domain = yaml.load(fdomain)

app = Eve(settings={
    'MONGO_HOST': 'localhost',
    'MONGO_PORT': 27017,
    'MONGO_DBNAME': 'genow',
    'DOMAIN': domain
})

app.run()
