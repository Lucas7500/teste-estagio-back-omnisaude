import json
import os


class FilmesRepository:
    path_db = os.path.join("db");
    path_filmes_favoritos = os.path.join("db", "filmes_favoritos.json")

    def obter_todos():
        filmes = []
        if not os.path.exists(FilmesRepository.path_filmes_favoritos):
            FilmesRepository.criar_banco_em_memoria()

        with open(FilmesRepository.path_filmes_favoritos, "r") as arquivo:
            filmes = json.load(arquivo)

        return filmes

    def adicionar_aos_favoritos(filme):
        if not os.path.exists(FilmesRepository.path_filmes_favoritos):
            FilmesRepository.criar_banco_em_memoria()
        
        operacao_arquivo = "r"
        with open(FilmesRepository.path_filmes_favoritos, operacao_arquivo) as arquivo:
            filmes = json.load(arquivo)

        filmes.append(filme)

        operacao_arquivo = "w"
        with open(FilmesRepository.path_filmes_favoritos, operacao_arquivo) as arquivo:
            json.dump(filmes, arquivo)

    def criar_banco_em_memoria():
        if not os.path.exists(FilmesRepository.path_db):
            os.mkdir(FilmesRepository.path_db)
        
        with open(FilmesRepository.path_filmes_favoritos, "w") as arquivo:
            json.dump([], arquivo)
