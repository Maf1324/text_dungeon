""""
A classe Char:
    - Métodos gerais:
        * Atacar, utilizado durante as batalhas tanto pelo jogador quanto por
        inimigos;
        * Recebe dano,

    - Atributos:
        * Status do personagem, objeto da classe Stats com atributos que seram
        lidos durante batalhas;
        * Nível, que será lido para criação de dungeons;

    - Metodos abstratos:
        * Mostrar status, acessa objeto status e exibe para o jogador;
        * Morrer, irá setar o atributo "alive" para False;
"""


from abc import ABC, abstractmethod

from classes.status import Stats


class Char(ABC):
    def __init__(self) -> None:
        super().__init__()
        self.__alive = True
        self.level = 1
        self.__status = Stats()

    @property
    def status(self):
        return self.__status

    @abstractmethod
    def show_status(self):
        pass

    @abstractmethod
    def die(self):
        pass

    def attack(self, enemy):
        print(f'{self.name} attacked {enemy.name}')
        damage = self.status.Atk - enemy.status.Def if self.status.Atk - \
            enemy.status.Def > 0 else 1
        enemy.take_damage(damage)

    def take_damage(self, damage):
        self.status.reduce_hp(damage)
        print(f'{self.name} took {damage} damage!')
