from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

# Configuração do banco de dados para MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/dbname'
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
    ground = db.Column(db.String)
    summary = db.Column(db.String)

class PlaneCrashResource(Resource):
    def get(self, crash_id=None):
        if crash_id:
            crash = PlaneCrash.query.get_or_404(crash_id)
            return jsonify({
                'id': crash.id,
                'date': crash.date,
                'time': crash.time,
                'location': crash.location,
                'operator': crash.operator,
                'flight-number': crash.flight_number,
                'route': crash.route,
                'ac_type': crash.ac_type,
                'registration': crash.registration,
                'cn_ln': crash.cn_ln,
                'aboard': crash.aboard,
                'fatalities': crash.fatalities,
                'ground': crash.ground,
                'summary': crash.summary
            })
        crashes = PlaneCrash.query.all()
        return jsonify([{
            'id': crash.id,
            'date': crash.date,
            'time': crash.time,
            'location': crash.location,
            'operator': crash.operator,
            'flight-number': crash.flight_number,
            'route': crash.route,
            'ac_type': crash.ac_type,
            'registration': crash.registration,
            'cn_ln': crash.cn_ln,
            'aboard': crash.aboard,
            'fatalities': crash.fatalities,
            'ground': crash.ground,
            'summary': crash.summary
        } for crash in crashes])

    def post(self):
        args = request.get_json()
        new_crash = PlaneCrash(**args)
        db.session.add(new_crash)
        db.session.commit()
        return {'id': new_crash.id}, 201

    def put(self, crash_id):
        crash = PlaneCrash.query.get_or_404(crash_id)
        args = request.get_json()
        for key, value in args.items():
            setattr(crash, key, value)
        db.session.commit()
        return {'message': f'Crash {crash_id} updated successfully.'}
    
    def delete(self, crash_id):
        crash = PlaneCrash.query.get_or_404(crash_id)
        db.session.delete(crash)
        db.session.commit()
        return {'message': f'Crash {crash_id} deleted successfully.'}, 204

# Rota para o recurso
api.add_resource(PlaneCrashResource, '/plane_crash', '/plane_crash/<int:crash_id>')

# Cria o banco de dados e inicia o aplicativo
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)