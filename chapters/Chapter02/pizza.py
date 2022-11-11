from flask import Flask
from flask_restx import Api, Resource, reqparse
from flask_restx.inputs import int_range

app = Flask(__name__)
api = Api(app, doc='/doc')

sales_history = dict(
    margherita=0,
    pepperoni=0,
    hawaii=0
)

pizza_parser = reqparse.RequestParser()
pizza_parser.add_argument("variant", required=True, choices = ('margherita', 'pepperoni', 'hawaii'))
pizza_parser.add_argument("quantity", type=int_range(0, 50), required=True)

@api.route("/pizzeria/sale")
class Pizza(Resource):

    @api.expect(pizza_parser)
    def post(self):
        args = pizza_parser.parse_args()
        variant = args.variant
        quantity = args.quantity
        sales_history[variant] += quantity
        return f"Added {quantity} order(s) of {variant}.", 201
    
    def get(self):
        return sales_history

if __name__ == "__main__":
    app.run(debug=True)