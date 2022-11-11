from flask import Flask
from flask_restx import Api, Resource, reqparse
from random import randint

app = Flask(__name__)
api = Api(app)

@api.route("/numberbot/double/<number>")
class Numberbot(Resource):

    def get(self, number):
        return int(number)*2

random_parser = reqparse.RequestParser()
random_parser.add_argument("low", type=int)
random_parser.add_argument("high", type=int)

@api.route("/numberbot/random")
class Random(Resource):

    @api.expect(random_parser)
    def get(self):
        args = random_parser.parse_args()
        low = args.low
        high = args.high
        return randint(int(low), int(high))

if __name__ == "__main__":
    app.run(debug=True)