from flask import Flask
from flask_restx import Api,Resource

app = Flask(__name__)
api = Api(app, doc='/doc')

@api.route('/address')
class PeerAddresses(Resource):

    def get(self):
        return "Hi"

@api.route('/address/<peeraddress>')
class PeerAddresses(Resource):

    def get(self, peeraddress):
        return f"Hi, {peeraddress}"

@api.route('/asn')
class PeerAsn(Resource):

    def get(self):
        return "Hi"


if __name__ == "__main__":
    app.run(debug=True)