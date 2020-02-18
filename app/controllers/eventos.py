from app import app
from app import db
from flask import render_template
from flask import request, redirect
from datetime import datetime as dt
import uuid
import os.path
from app.models.tables import Evento


@app.route("/eventos")
def listar_eventos():
    nome = request.args.get('nome')
    if nome:
        nome = "%{}%".format(nome)
        e = Evento.query.filter(Evento.nome.like(nome)).all()
    else:
        e = Evento.query.all()
    return render_template("eventos-listar.html", eventos=e)


@app.route("/eventos/<int:id>")
def detalhar_evento(id):
    e = Evento.query.filter_by(id=id).first()
    e.logotipo = 'assets/images/eventos/' + e.logotipo
    return render_template("eventos-detalhe.html", evento=e)


@app.route("/eventos/novo", methods=["GET"])
def form_novo_evento():
    tipo = "inserir"
    return render_template("eventos-formulario.html", tipo=tipo)


# TODO: capturar usuário logado
@app.route("/eventos/novo", methods=["POST"])
def inserir_evento():

    arquivo = request.files['logotipo']
    arquivo.filename = str(uuid.uuid4()) + os.path.splitext(arquivo.filename)[1]
    arquivo.save(app.config['UPLOAD_PATH'] + arquivo.filename)

    data = dt.strptime(request.form['data'], '%Y-%m-%d')

    e = Evento(nome=request.form['nome'], descricao=request.form['descricao'],
               instituicao=request.form['instituicao'], local=request.form['local'],
               data=data, logotipo=arquivo.filename, usuario_id="1")
    db.session.add(e)
    db.session.commit()
    return redirect("/eventos")


@app.route("/eventos/alterar/<int:id>", methods=["GET"])
def form_alterar_evento(id):
    tipo = "alterar"
    e = Evento.query.filter_by(id=id).first()
    e.data = f"{e.data:%Y}" + "-" + f"{e.data:%m}" + "-" + f"{e.data:%d}"
    e.logotipo = 'assets/images/eventos/' + e.logotipo
    return render_template("eventos-formulario.html", tipo=tipo, evento=e)


@app.route("/eventos/alterar", methods=["POST"])
def alterar_evento():
    return redirect("/eventos")


# TODO: mensagem caso não possa deletar
@app.route("/eventos/deletar/<int:id>")
def deletar_evento(id):
    e = Evento.query.filter_by(id=id).first()
    db.session.delete(e)
    db.session.commit()
    return redirect("/eventos")
