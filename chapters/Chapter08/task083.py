from jinja2 import Template
import yaml

template = Template(open("task083.j2").read())
vars = yaml.safe_load(open('task083.yml','r'))
print(template.render(vars))