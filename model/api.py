from eve import Eve
import yaml

with open('domain.yaml') as domain:
    settings = yaml.load(domain)

app = Eve(settings=settings)
app.run()