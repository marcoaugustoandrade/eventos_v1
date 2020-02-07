from app import app
from flask import render_template

# Lista todas as atividades de um evento
@app.route("/atividades/<int:evento_id>")
def listar_atividades(evento_id):
    return ""


@app.route("/atividades/novo", methods=["GET"])
def form_nova_atividade():
    return ""

@app.route("/atividades/novo", methods=["POST"])
def inserir_atividade():
    return ""

@app.route("/atividades/alterar", methods=["GET"])
def form_alterar_atividade():
    return ""

@app.route("/atividades/alterar", methods=["POST"])
def alterar_atividade():
    return ""

@app.route("/atividades/deletar/<int:id>")
def deletar_atividade(id):
    return ""
