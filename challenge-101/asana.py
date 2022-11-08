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
def challenge101(ctx):
    ctx.ensure_object(dict)
    config = json.load(open("config.json"))
    ctx.obj["asana"] = AsanaRestApi(config["PAT"])


## Requirement C

##
def listprojects(obj, outputformat):
    projects = obj["asana"].get("/projects")

    print("Projects:")

    ## Requirement D

    ##

## Requirement E

##
def listtasks(obj, project, showgid):
    print("Tasks in project:")
    ## Requirement F

    ##
        if showgid:
            print(task_details["data"]["name"] + ", GID=" + task["gid"] + ", Completed=" + str(task_details["data"]["completed"]))
        else:
            print(task_details["data"]["name"] + ", Completed=" + str(task_details["data"]["completed"]))


## Requirement G

##
def setstatus(obj, task, completed):
    body = {
        ## Requirement H

        ##
    }
    response = obj["asana"].put("/tasks/" + str(task), body=body)
    print(response["data"]["name"] + " is completed:" + str(response["data"]["completed"]))


## Requirement I (optional)

##


if __name__ == "__main__":
    challenge101()
