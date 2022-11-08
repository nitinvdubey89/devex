from flask import Flask
from flask_restx import Resource, Api, reqparse, fields

app = Flask(__name__)
api = Api(app)

hof_data = {
    "20220001": {
        "name": "Hank Preston",
        "date": "2022-05-02",
        "company": "cisco"
    },
    "20220002": {
        "name": "Ramses Smeyers",
        "date": "2022-05-02",
        "company": "cisco"
    },
    "20220003": {
        "name": "Joe Clarke",
        "date": "2022-05-02",
        "company": "cisco"
    },
    "20220004": {
        "name": "Dmitry Figol",
        "date": "2022-05-02",
        "company": "cisco"
    },
    "20220005": {
        "name": "Stuart Clark",
        "date": "2022-05-02",
        "company": "cisco"
    },
    "20220006": {
        "name": "Andreas Baekdahl",
        "date": "2022-07-19",
        "company": "wingmen"
    }
}


hof_parser = reqparse.RequestParser()
## Requirement A
hof_parser.add_argument('company', type=str, help='Company name')
##


@api.route('/hof')
class HallOfFame(Resource):
    @api.expect(hof_parser)
    def get(self):
        args = hof_parser.parse_args()

        if args.company == "all":
            return hof_data

        else:
            result = {}
            ## Requirement B

            ##
            return result

individual_parser_get = reqparse.RequestParser()
individual_parser_get.add_argument('number', type=int, help='Certification number')

## Requirement C

##

individual_parser_delete = individual_parser_get.copy()



class CertificationNotFound(Exception):
    pass


individual_fields = api.model('Individual', {
    'name': fields.String,
    'company': fields.String,
    'date': fields.String
})

@api.route('/individual')
class CertifiedIndividual(Resource):

    @api.expect(individual_parser_get)
    @api.marshal_with(individual_fields, as_list=False)
    def get(self):
        args = individual_parser_get.parse_args()

        ## Requirement D

        ##

    @api.expect(individual_parser_post)
    def post(self):
        args = individual_parser_post.parse_args()

        number = str(args.number)

        ## Requirement E

        ##

        return {}, 201

    @api.expect(individual_parser_delete)
    def delete(self):
        args = individual_parser_delete.parse_args()

        ## Requirement F
        hof_data.pop(str(args.number))

        if args.number in hof_data:
            return {}, 204
        else:
            return {}, 204
        ##

if __name__ == '__main__':
    app.run(debug=True)
