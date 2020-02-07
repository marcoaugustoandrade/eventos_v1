from app import app
from flask import render_template


@app.route("/certificados/<int:atividade_id>")
def emitir_certificado(atividade_id):
    return ""

@app.route("/certificados/validar/<int:atividade>")
def validar_certificado(atividade_id):
    return ""
