################################
#### CLASSES E CONSTRUTORES ####
################################

# METODOS

# Quando criar uma classe

class Carro:
    
    # Metodo inicializador ou construtor que recebe um parametro padrao self.
    # O def dentro da classe é chamado de metodo e nao funcao.
    # Quando instanciar essa classe eu vou ter que passar esse atributos.

	def __init__(self):  


# Executo para aparecer o print

from carro import Carro

carro1 = Carro()

carro1

# Entendimento do Self

class Carro:
    
	def __init__(self):
            print('Este eh o self {}'.format(self))



###################
#### ATRIBUTOS ####
###################

class Carro:
    
    def __init__(self, marca, modelo, cor, cc):
        self.marca = marca
        self.modelo = modelo
        self.cor = cor
        self.cc = cc


# Executando os atributos.
# Sempre entrar e sair para zerar os imports do temrinal.

from carro import Carro

carro1 = Carro('Fiat','Punto', 'Vermelho', 130)

carro1

carro1.cc