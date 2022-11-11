from jinja2 import Template
import yaml

template = Template(open("task082.j2").read())
vars = yaml.safe_load(open('task082.yml','r'))
print(template.render(vars))