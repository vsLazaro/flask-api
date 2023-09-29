from flask import request, jsonify
from flask_restful import Resource
from models import db, PlaneCrash

class PlaneCrashResource(Resource):

    @staticmethod
    def crash_to_dict(crash):
        return {
            'id': crash.id,
            'date': crash.date,
            'time': crash.time,
            'location': crash.location,
            'operator': crash.operator,
            'flight_number': crash.flight_number,
            'route': crash.route,
            'ac_type': crash.ac_type,
            'registration': crash.registration,
            'cn_ln': crash.cn_ln,
            'aboard': crash.aboard,
            'fatalities': crash.fatalities,
            'ground': crash.ground,
            'summary': crash.summary
        }

    def get(self, crash_id=None):
        if crash_id:
            crash = PlaneCrash.query.get_or_404(crash_id)
            return jsonify(self.crash_to_dict(crash))
        crashes = PlaneCrash.query.all()
        return jsonify([self.crash_to_dict(crash) for crash in crashes])

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