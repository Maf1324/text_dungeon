""""
A classe Player:
    - Metodos gerais herdados da classe Char:
        * Atacar

    - Atributos herdados da classe Char:
        * Status do personagem
        * Nível

    - Métodos abstratos herdados da classe Char:
        * Mostrar status;
        * Morrer;

    - Atributos:
        * Nome do personagem;
        * Exp, valor que irá definir o nivel do personagem;
        * Inventario, que será um objeto da classe Inventario;
        * Equipamento, serão os itens equipados do personagem e objeto da
         classe Inventario;

    - Métodos:
        * Passar de nível, vai chamar objeto Status para altera-lo;
        * Usar item, acessa o inventario para utilização de um dos itens;
        * Equipar item, acessa objeto inventario e equipamento de suas devidas
         classes;
"""


from classes.char import Char


class Player(Char):
    def __init__(self) -> None:
        super().__init__()
        self.name = input('Choose the name of your character --> ').title()

    def show_status(self):
        pass

    def die(self):
        print(self.name + ' died')
        self.__alive = False

    def show_itens(self):
        print('Listing itens')

    def level_up(self):
        self.level += 1
        self.status.handle_level_up()
