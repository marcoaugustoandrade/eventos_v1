from app import db
from datetime import datetime as dt


# Usuarios
from app.models.tables import Usuario
u1 = Usuario(nome='Suporte', email='suporte@gmail.com', senha='Suporte99')
db.session.add(u1)
db.session.commit()

# Eventos
from app.models.tables import Evento
e1 = Evento(nome='Semana ADS', descricao="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam", instituicao='IFRO', local="Campus Vilhena", data=dt.now(), logotipo="conect.png", usuario_id='1')
e2 = Evento(nome='Semana ADS', descricao="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam", instituicao='IFRO', local="Campus Vilhena", data=dt.now(), logotipo="conect.png", usuario_id='1')
db.session.add(e1)
db.session.add(e2)
db.session.commit()

# Atividades dos eventos
from app.models.tables import Atividade
a1 = Atividade(nome="Oficina GitHub", ministrante="José de Oliveira", tipo="oficina", vagas="20", local="Lab 1", data=dt.now(), evento_id="1")
a2 = Atividade(nome="Oficina Jekyll", ministrante="Maria da Silva", tipo="oficina", vagas="25", local="Lab 2", data=dt.now(), evento_id="1")
a3 = Atividade(nome="Oficina Docker", ministrante="Tereza Souza", tipo="oficina", vagas="20", local="Lab 3", data=dt.now(), evento_id="2")
db.session.add(a1)
db.session.add(a2)
db.session.add(a3)
db.session.commit()
