from jinja2 import Template
import yaml

template = Template(open("task081.j2").read())
vars = yaml.safe_load(open('task081.yml','r'))
print(template.render(vars))