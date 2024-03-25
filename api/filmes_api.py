from flask import Flask, jsonify, request
from repositories.filmes_repository import FilmesRepository 
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
def obter_favoritos():
    return FilmesRepository.obter_todos(), status['OK']


@app.get(rota_obter_por_titulo)
def obter_por_titulo(titulo):
    parametro = 'titulo'
    valor_padrao_parametro = ''

    if not titulo:
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

    return r.json(), status['OK']


@app.post(rota_adicionar_aos_favoritos)
def adicionar_aos_favoritos(filme):
    if not filme:
        filme = request.get_json()
    
    FilmesRepository.adicionar_aos_favoritos(filme)
    
    mensagem_sucesso = "Success"
    return mensagem_sucesso, status['CREATED']
