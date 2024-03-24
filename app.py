from flask import Flask, jsonify, request
import requests
import json
import os

app = Flask(__name__)


rota_adicionar_aos_favoritos = "/"
rota_obter_favoritos = "/filmes/favoritos"
rota_obter_por_titulo = "/filmes"
nome_arquivo_memoria = "filmes.json"
url_omdb = 'https://www.omdbapi.com/'
status = {'OK': 200, 'CREATED': 201, 'INTERNAL_SERVER_ERROR': 500}


@app.get(rota_obter_favoritos)
def obter_todos():
    operacao_arquivo = "r"
    with open(nome_arquivo_memoria, operacao_arquivo) as file:
        filmes = json.load(file)

    return filmes


@app.get(rota_obter_por_titulo)
def obter_por_titulo():
    parametro = 'titulo'
    valor_padrao_parametro = ''

    titulo = request.args.get(
        parametro, default=valor_padrao_parametro, type=str)

    parametro_api_key = 'apiKey'
    parametro_titulo = 't'
    api_key = os.environ[parametro_api_key]

    parametros = {parametro_api_key: api_key, parametro_titulo: titulo}

    r = requests.get(url_omdb, params=parametros)

    if r.status_code != status['OK']:
        nome_erro = "error"
        mensagem_erro = f"Erro ao acessar a API do OMDb: {r.status_code}"
        return jsonify({f"{nome_erro}:{mensagem_erro}"}), status['INTERNAL_SERVER_ERROR']

    return r.json()


@app.post(rota_adicionar_aos_favoritos)
def adicionar_aos_favoritos():
    filme = request.get_json()

    try:
        operacao_arquivo = "r"
        with open(nome_arquivo_memoria, operacao_arquivo) as file:
            filmes = json.load(file)
    except FileNotFoundError:
        filmes = []

    filmes.append(filme)

    operacao_arquivo = "w"
    with open(nome_arquivo_memoria, operacao_arquivo) as file:
        json.dump(filmes, file)

    mensagem_sucesso = "Success"
    return mensagem_sucesso, status['CREATED']


app.run(port=5000, host='localhost', debug=True)
