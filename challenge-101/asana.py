import requests
import click
import json

class AsanaRestApi():

    headers = {}

    def __init__(self, token):
        self.headers["Accept"] = "application/json"
        self.headers["Content-Type"] = "application/json"
        self.headers["Authorization"] = "Bearer " + token

    def get(self, api_endpoint_path):
        response = requests.get("https://app.asana.com/api/1.0" + api_endpoint_path, headers=self.headers)
        return response.json()

    def put(self, api_endpoint_path, body):
        body_json = json.dumps(body)
        response = requests.put("https://app.asana.com/api/1.0" + api_endpoint_path, headers=self.headers, data=body_json)
        return response.json()

## Requirement B

##
@click.group()
@click.pass_context
def challenge101(ctx):
    ctx.ensure_object(dict)
    config = json.load(open("config.json"))
    ctx.obj["asana"] = AsanaRestApi(config["PAT"])


## Requirement C

##
@challenge101.command()
@click.pass_obj
@click.option("--outputformat", type=click.Choice(['lines','raw']))
def listprojects(obj, outputformat):
    projects = obj["asana"].get("/projects")

    print("Projects:")

    ## Requirement D
    if outputformat == 'raw':
        for i in projects['data']:
            print(i)
    elif outputformat == 'lines':
        for i in projects['data']:
            print(f"{i['name']} GID={i['gid']}")
    ##

## Requirement E

##
@challenge101.command()
@click.pass_obj
@click.option("--project", type=int, help="Project GID", required=True)
@click.option("--showgid", "--g", is_flag=True, help="Show GID of tasks")
def listtasks(obj, project, showgid):
    print("Tasks in project:")
    tasks = obj["asana"].get(f"/tasks?project={project}")
    for task in tasks['data']:
        task_details = obj["asana"].get(f"/tasks/{task['gid']}")
    ## Requirement F

    ##
        if showgid:
            print(task_details["data"]["name"] + ", GID=" + task["gid"] + ", Completed=" + str(task_details["data"]["completed"]))
        else:
            print(task_details["data"]["name"] + ", Completed=" + str(task_details["data"]["completed"]))


## Requirement G

##
@challenge101.command()
@click.pass_obj
@click.option("--task", type=int, required=True)
@click.option("--completed/--not-completed", is_flag=True, help="Mark task as completed or not completed.")
def setstatus(obj, task, completed):
    body = {
        "data": {
            "completed": completed
        }
    }
    response = obj["asana"].put("/tasks/" + str(task), body=body)
    print(response["data"]["name"] + " is completed:" + str(response["data"]["completed"]))


## Requirement I (optional)

##
#challenge101 = click.CommandCollection(sources=[listprojects, listtasks, setstatus])


if __name__ == "__main__":
    challenge101()
