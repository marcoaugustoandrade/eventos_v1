from app import db


class Usuario(db.Model):
    __tablename__ = 'usuarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200))
    email = db.Column(db.String(200), index=True, unique=True)
    senha = db.Column(db.String(200))

    def __repr__(self):
        return '<Usuario %s>' % self.nome


class Evento(db.Model):
    __tablename__ = 'eventos'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200))
    instituicao = db.Column(db.String(200), nullable=False)
    local = db.Column(db.String(200), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    logotipo = db.Column(db.String(200), nullable=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)

    def __repr__(self):
        return '<Evento %s>' % self.nome


class Atividade(db.Model):
    __tablename__ = 'atividades'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(200), nullable=False)
    ministrante = db.Column(db.String(200), nullable=False)
    tipo = db.Column(db.String(200), nullable=False)
    vagas = db.Column(db.Integer, nullable=False)
    local = db.Column(db.String(200), nullable=False)
    data = db.Column(db.DateTime, nullable=False)
    evento_id = db.Column(db.Integer, db.ForeignKey('eventos.id'), nullable=False)

    def __repr__(self):
        return '<Evento %s>' % self.nome
