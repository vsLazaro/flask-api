from flask import Flask
from flask_restful import Api
from models import db
from resources.plane_crash_resource import PlaneCrashResource
import config

app = Flask(__name__)
api = Api(app)

# Configuração da aplicação
app.config.from_object(config.Config)

# Inicialização de extensões
db.init_app(app)

# Rota para o recurso
api.add_resource(PlaneCrashResource, '/plane_crash', '/plane_crash/<string:crash_id>')

if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run()