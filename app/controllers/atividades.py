from app import app
from app import db
from flask import render_template, redirect
from app.models.tables import Evento, Atividade


# Lista todas as atividades de um evento
@app.route("/atividades/<int:evento_id>")
def listar_atividades(evento_id):
    a = Atividade.query.all()
    e = Evento.query.filter_by(id=evento_id).first()
    return render_template("atividades-listar.html", atividades=a, evento=e)


@app.route("/atividades/novo", methods=["GET"])
def form_nova_atividade():
    tipo = "inserir"
    return render_template("atividades-formulario.html", tipo=tipo)


@app.route("/atividades/novo", methods=["POST"])
def inserir_atividade(evento_id):
    return redirect("/atividades/" + evento_id)


@app.route("/atividades/alterar", methods=["GET"])
def form_alterar_atividade():
    tipo = "alterar"
    return render_template("atividades-formulario.html", tipo=tipo)


@app.route("/atividades/alterar", methods=["POST"])
def alterar_atividade():
    return ""


@app.route("/atividades/deletar/<int:id>")
def deletar_atividade(id):
    return ""
