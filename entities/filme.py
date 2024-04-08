class Filme:
    def __init__(self, titulo, ano_lancamento, classificacao, sinopse, diretor):
        self.titulo = titulo
        self.ano_lancamento = ano_lancamento
        self.classificacao = classificacao
        self.sinopse = sinopse
        self.diretor = diretor

    def convert(filme_dict):
        return Filme(filme_dict['Title'],
                      filme_dict['Released'],
                      filme_dict['Rated'],
                      filme_dict['Plot'],
                      filme_dict['Director'])
        
        return filme
    
    def exibir(self):
        print()
        print(f"Titulo: {self.titulo}")
        print(f"Ano de Lançamento: {self.ano_lancamento}")
        print(f"Classificação: {self.classificacao}")
        print(f"Sinopse: {self.sinopse}")
        print(f"Diretor: {self.diretor}")
        print()
