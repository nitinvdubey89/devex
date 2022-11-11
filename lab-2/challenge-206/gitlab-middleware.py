from flask import Flask
from flask_restx import Resource, Api
import os
import requests, json

app = Flask(__name__)
api = Api(app)

api_basepath = "https://gitlab.com/api/v4"
# token = 'glpat-PjEjhsMR_JubUL-SVuU7'
token = os.environ.get("GITLAB_PAT")
# project = '40965663'
project = os.environ.get("GITLAB_PROJECT")

@api.route("/latestcommit/time")
class CommitTime(Resource):
    def get(self):
        ## Requirement A
        path = f"{api_basepath}/projects/{project}/repository/branches"
        ##

        ## Requirement B
        headers = {
            "Authorization": f"Bearer {token}"
        }
        response = requests.get(path, headers=headers).json()
        ##

        ## Requirement C
        return response[0]['commit']['committed_date']
        ##

@api.route("/latestcommit/message")
class CommitMessage(Resource):
    def get(self):
        pass
        ## Requirement D
        path = f"{api_basepath}/projects/{project}/repository/branches?access_token={token}"
        ##

        ## Requirement E
        response = requests.get(path).json()
        ##

        ## Requirement F
        return response[0]['commit']['message']
        ##

if __name__ == '__main__':
    app.run(debug=True)
