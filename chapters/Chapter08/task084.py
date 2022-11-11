from jinja2 import Template
import yaml

template = Template(open("task084.j2").read())
vars = yaml.safe_load(open('task084.yml','r'))
print(template.render(vars))