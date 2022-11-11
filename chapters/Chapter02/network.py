from flask import Flask
from flask_restx import Api, Resource, reqparse

app = Flask(__name__)
api = Api(app, doc='/doc')


inventory = {}

get_parser = reqparse.RequestParser()
get_parser.add_argument("search")

delete_parser = reqparse.RequestParser()
delete_parser.add_argument("hostname", required=True)

inventory_parser = delete_parser.copy()
inventory_parser.add_argument("type", choices = ("switch","router","firewall"), required=True)

@api.route("/network/inventory")
class Inventory(Resource):

    @api.expect(inventory_parser)
    def post(self):
        args = inventory_parser.parse_args()
        h = args.hostname
        t = args.type
        inventory[h] = t
        return f"Successfully added {h} of type {t}", 201
    
    @api.expect(get_parser)
    def get(self):
        args = get_parser.parse_args()
        retVal = []
        if args.search:
            s = args.search
            for k,v in inventory.items():
                if s in k:
                    retVal.append(f"{k}|{inventory[k]}")
        else:
            for k,v in inventory.items():
                retVal.append(f"{k}|{inventory[k]}")
        return retVal
    
    @api.expect(delete_parser)
    def delete(self):
        args = delete_parser.parse_args()
        h = args.hostname
        if h in inventory.keys():
            inventory.pop(h)
            return f"Removed {h}", 201
        else:
            return "No items removed", 201



if __name__ == "__main__":
    app.run(debug=True, port=4169)