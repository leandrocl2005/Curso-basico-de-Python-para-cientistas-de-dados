class Pessoa(object):

    def __init__(self, nome, idade, sexo=None, escolaridade=None):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.escolaridade = escolaridade
        
    def fazAniversario(self):
        self.idade = self.idade + 1
        
    def comparaIdade(self,other):
        if self.idade > other.idade:
            return str(self.nome) + ' é mais velho'
        elif self.idade < other.idade:
            return str(other.nome) + ' é mais velho'
        else:
            return 'Mesma idade!'
        
class Atleta(Pessoa):
    
    def __init__(self, nome, idade, modalidade=None, num_ouros=0):
        Pessoa.__init__(self, nome, idade)
        self.modalidade = modalidade
        self.num_ouros = num_ouros
        
    def ganhaOuro(self):
        self.num_ouros = self.num_ouros + 1

def somaIdades(pessoa1,pessoa2):
    return pessoa1.idade + pessoa2.idade
