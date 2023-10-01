from flask import Flask
from flask_restful import Api
from resource import PlaneCrashResource

app = Flask(__name__)
api = Api(app)


api.add_resource(PlaneCrashResource, '/crash', '/crash/<int:user_id>')

if __name__ == '__main__':
    app.run(debug=True)