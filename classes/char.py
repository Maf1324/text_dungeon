""""
A classe Char:
    - Métodos gerais:
        * Atacar, utilizado durante as batalhas tanto pelo jogador quanto por
        inimigos;

    - Atributos:
        * Status do personagem, objeto da classe Stats com atributos que seram
        lidos durante batalhas;
        * Nível, que será lido para criação de dungeons;

    - Metodos abstratos:
        * Mostrar status, acessa objeto status e exibe para o jogador;
        * Morrer, irá setar o atributo "alive" para False;
"""


from abc import ABC, abstractmethod


class Char(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.__alive = True
        self.level = 1
        # TODO criar classe status
        self.__status = 'Vou criar a classe Status ainda'

    @abstractmethod
    def show_status(self):
        pass

    @abstractmethod
    def die(self):
        pass

    def attack(self, enemy):
        print(f'{self.name} attacked {enemy.name}')
