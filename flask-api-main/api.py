from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# Configuração do banco de dados
# Por exemplo, usar SQLite para desenvolvimento
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class PlaneCrash(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.String)
    time = db.Column(db.String)
    location = db.Column(db.String)
    operator = db.Column(db.String)
    flight_number = db.Column(db.String)
    route = db.Column(db.String)
    ac_type = db.Column(db.String)
    registration = db.Column(db.String)
    cn_ln = db.Column(db.String)
    aboard = db.Column(db.String)
    fatalities = db.Column(db.String)
    ground = db.Column(db.Integer)
    summary = db.Column(db.Text)

class PlaneCrashResource(Resource):
    def get(self, crash_id):
        crash = PlaneCrash.query.get_or_404(crash_id)
        return {
            'id': crash.id,
            'date': crash.date,
            'time': crash.time,
            # Adicionar as outras colunas
        }

    def post(self):
        args = request.get_json()
        new_crash = PlaneCrash(**args)
        db.session.add(new_crash)
        db.session.commit()
        return {'id': new_crash.id}, 201

    # Implementar os métodos PUT e DELETE

# Rota para o recurso
api.add_resource(PlaneCrashResource, '/plane_crash', '/plane_crash/<int:crash_id>')

# Cria o banco de dados e inicia o aplicativo
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)