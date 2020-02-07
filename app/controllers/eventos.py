from app import app
from flask import render_template
from app.models.tables import Evento


@app.route("/eventos")
def listar_eventos():
    e = Evento.query.all()
    return render_template("eventos-listar.html", eventos=e)

@app.route("/eventos/<int:id>")
def detalhar_evento():
    return ""

@app.route("/eventos/novo", methods=["GET"])
def form_novo_evento():
    return ""

@app.route("/eventos/novo", methods=["POST"])
def inserir_evento():
    return ""

@app.route("/eventos/alterar", methods=["GET"])
def form_alterar_evento():
    return ""

@app.route("/eventos/alterar", methods=["POST"])
def alterar_evento():
    return ""

@app.route("/eventos/deletar/<int:id>")
def deletar_evento(id):
    return ""
