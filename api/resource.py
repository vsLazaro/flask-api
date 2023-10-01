from flask import request, jsonify
from flask_restful import Resource
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from model import PlaneCrash, Base


engine = create_engine('mysql+mysqlconnector://root:example@localhost:3306/flask')

Session = sessionmaker(bind=engine)
session = Session()

inspector = inspect(engine)

if not inspector.has_table(PlaneCrash.__tablename__):
    Base.metadata.create_all(engine)

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
          crash = session.query.query(PlaneCrash).filter_by(id=crash_id).first()
          if crash:
            return self.crash_to_dict(crash)
          else:
            return {'mensagem': 'Registro de acidente não encontrado'}, 404
      crashes = session.query(PlaneCrash).all()
      if crashes:
          return [self.crash_to_dict(crash) for crash in crashes]
      else:
          return {'mensagem': 'Não existem registro de acidentes'}, 404
    
    def put(self, crash_id):
        crash = session.query(PlaneCrash).filter_by(id=crash_id).first()
        data = request.get_json()
        if crash:
            PlaneCrash.date = data['date']
            PlaneCrash.time = data['time']
            PlaneCrash.location = data['location']
            PlaneCrash.operator = data['operator']
            PlaneCrash.flight_number = data['flight_number']
            PlaneCrash.route = data['route']
            PlaneCrash.ac_type = data['ac_type']
            PlaneCrash.registration = data['registration']
            PlaneCrash.cn_ln = data['cn_ln']
            PlaneCrash.aboard = data['aboard']
            PlaneCrash.fatalities = data['fatalities']
            PlaneCrash.ground = data['ground']
            PlaneCrash.summary = data['summary']
            
            session.commit()
            return {'mensagem': 'Registro de acidente de avião atualizado com sucesso'}
        else:
            return {'mensagem': 'Registro de acidente de avião não encontrado'}, 404
    
    def delete(self, crash_id):
        crash = PlaneCrash.query.get_or_404(crash_id)
        if crash:
            session.delete(crash)
            session.commit()
            return {'mensagem': 'Registro de acidente excluído com sucesso'}
        else:
            return {'mensagem': 'Registro de acidente não encontrado'}, 404
    
    def post(self):
        data = request.get_json()
        novo_plane_crash = PlaneCrash(
            date=data['date'],
            time=data['time'],
            location=data['location'],
            operator=data['operator'],
            flight_number=data['flight_number'],
            route=data['route'],
            ac_type=data['ac_type'],
            registration=data['registration'],
            cn_ln=data['cn_ln'],
            aboard=data['aboard'],
            fatalities=data['fatalities'],
            ground=data['ground'],
            summary=data['summary']
        )
        session.add(novo_plane_crash)
        session.commit()
        return {'mensagem': 'Novo registro de acidente de avião criado com sucesso', 'id': novo_plane_crash.id}, 201


