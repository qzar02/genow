import jinja2
import requests

URL_API = "http://localhost:5000"

session = requests.Session()

env = jinja2.Environment(loader=jinja2.FileSystemLoader('../../templates/'))

tables = session.get(f"{URL_API}/table").json()['_items']
relationships = session.get(f"{URL_API}/relationship").json()['_items']

render = (
    env
    .get_template('airflow/dummy/dag.jinja2')
    .render(
        tables=tables,
        relationships=relationships)
)

with open('dbdiagram.der', 'w') as f:
    f.write(render)
