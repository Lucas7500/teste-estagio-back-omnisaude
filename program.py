import api.filmes_api as filmes_api
from entities.filme import Filme
import json

print("Seja bem vindo ao seu catálogo de filmes!")

sair = False

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
            titulo = input(
                "Qual o título do filme que você deseja pesquisar? ")
            filme_json = str(filmes_api.obter_por_titulo(titulo)[0])
            for char in filme_json:
                if char == "'":
                    filme_json

            print(filme_json)
            break
            if not filme_json:
                print(f"O filme com o título {titulo} não foi encontrado")
            else:
                filme_dict = json.loads(filme_json)
                filme = Filme.convert(filme_dict)
                filme.exibir()

                adicionar_aos_favoritos = input(
                    f"Deseja adicionar o filme aos favoritos (S/N)? ")
                if adicionar_aos_favoritos.upper() == 'S':
                    filmes_api.adicionar_aos_favoritos(filme)
                    print(f"{titulo} foi adicionado aos favoritos com sucesso!")

        case 2:
            titulo = input(
                "Qual o título do filme você deseja adicionar aos favoritos? ")
            filme_json = str(filmes_api.obter_por_titulo(titulo)[0])

            if not filme_json:
                print(f"O filme com o título {titulo} não foi encontrado.")
            else:
                filmes_api.adicionar_aos_favoritos(filme)
                print(f"{titulo} foi adicionado aos favoritos com sucesso!")
        case 3:
            favoritos = filmes_api.obter_favoritos()
            if favoritos == []:
                print("Você não possui nenhum filme nos favoritos")
            else:
                filmes = json.load(favoritos)

                for filme in filmes:
                    filme.exibir()
