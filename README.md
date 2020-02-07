# SQL Alchemy

pip3 install Flask
pip3 install flask-sqlalchemy
pip3 install pymysql

## Criando a estrutura
```
from app import db
db.create_all()
```

## Criando um objeto
```
from app.models.tables import Usuario
u1 = Usuario(nome='marco', email='marco.andrade@ifro.edu.br', senha='Suporte99')
db.session.add(u1)
db.session.commit()
```

## Buscando dados
```
User.query.all()
```

