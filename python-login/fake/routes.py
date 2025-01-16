from fake import app
from flask import render_template, url_for, redirect, request

@app.route("/login", methods=["GET", "POST"])
def login():
    return render_template("login.html")

@app.route("/tabela", methods=["GET", "POST"])
def tabela():
    return render_template("tabela.html")

