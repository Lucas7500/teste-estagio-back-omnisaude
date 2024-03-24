from flask import Flask, jsonify, request
import requests
import json
import os

app = Flask(__name__)


@app.get("/filmes/favoritos")
def obter_todos():
    with open("filmes.json", "r") as file:
        filmes = json.load(file)

    return filmes


@app.route("/filmes", methods=['GET'])
def obter_por_titulo():
    titulo = request.args.get('titulo', default='', type=str)
    apiKey = os.environ['apiKey']
    parametros = {'apiKey': apiKey, 't': titulo}
    r = requests.get('https://www.omdbapi.com/', params=parametros)

    if r.status_code != 200:
        return jsonify({"error": f"Erro ao acessar a API do OMDb: {r.status_code}"}), 500

    return r.json()


@app.post("/")
def adicionar_aos_favoritos():
    filme = request.get_json()
    filename = "filmes.json"

    try:
        with open(filename, "r") as file:
            filmes = json.load(file)
    except FileNotFoundError:
        filmes = []

    filmes.append(filme)

    with open(filename, "w") as file:
        json.dump(filmes, file)

    return "Success", 201


app.run(port=5000, host='localhost', debug=True)
