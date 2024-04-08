import api.filmes_api as filmes_api
from entities.filme import Filme
import json

print("Seja bem vindo ao seu catálogo de filmes!")

sair = False

def adicionar_filme_aos_favoritos(filme):
    filmes_api.adicionar_aos_favoritos(filme)
    print(f"{Filme.convert(filme).titulo} foi adicionado aos favoritos com sucesso!")

while not sair:
    print("\nO que você deseja?")

    print("Digite 0 para finalizar o programa")
    print("Digite 1 para pesquisar um filme por título")
    print("Digite 2 para adicionar um filme aos favoritos")
    print("Digite 3 para listar os seus favoritos")

    comando = int(input())

    match comando:
        case 0:
            sair = True
        case 1:
            titulo = input("Qual o título do filme que você deseja pesquisar? ")
            filme = filmes_api.obter_por_titulo(titulo)[0]

            if not filme:
                print(f"O filme com o título {titulo} não foi encontrado")
            else:
                Filme.convert(filme).exibir()

                adicionar_aos_favoritos = input(f"Deseja adicionar o filme aos favoritos (S/N)? ")
                if adicionar_aos_favoritos.upper() == 'S':
                    adicionar_filme_aos_favoritos(filme)
        case 2:
            titulo = input(
                "Qual o título do filme você deseja adicionar aos favoritos? ")
            filme = filmes_api.obter_por_titulo(titulo)[0]

            if not filme:
                print(f"O filme com o título {titulo} não foi encontrado.")
            else:
                adicionar_filme_aos_favoritos(filme)
        case 3:
            favoritos = filmes_api.obter_favoritos()[0]

            if favoritos == []:
                print("Você não possui nenhum filme nos favoritos")
            else:
                for filme_dict in favoritos:
                    Filme.convert(filme_dict).exibir()