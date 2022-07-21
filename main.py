from classes.player import Player
from utils import handle_choice, row_print

# Lista de afazeres
# TODO Criar classe Status
# TODO Criar classe Inimigos
# TODO Criar classe Batalha

"""
A classe Game:
    - Atributos:
        * player, objeto de jogador usando a classe Player;
        * Playing, irá controlar o loop principal do jogo;
        * menu_choices, são as opções de interação para o jogador escolher.

    - Metodos:
        * Jogar, inicia o loop principal do jogo;
        * criar dungeon, irá iniciar uma rodada da classe Dungeon;
        * Salvar jogo;
        * Sair do jogo.

O loop principal:
    - Irá rodar enquanto o atributo self.alive == True;
    - Irá mostrar as opções que o usuario poderá escolher:
        * Dungeon, utiliza metodo criar dungeon;
        * Itens, utiliza metodo mostrar itens da classe Player
        * Save, salva o jogo;
        * Quit, encerra o jogo.
"""


class Game:
    def __init__(self) -> None:
        self._player = Player()
        self.__playing = True
        self.__menu_choices = {
            '1': self.run_dungeon,
            '2': self._player.show_itens,
            '3': self.save_game,
            '4': self.quit_game,
        }

    def play(self) -> None:
        while self.__playing:
            row_print('1 - Dungeon', '2 - Itens', '3 - Save', '4 - Quit',)
            choice = input()
            action = handle_choice(choice, self.__menu_choices)
            action()

    def run_dungeon(self) -> None:
        row_print('Dungeon running')

    def save_game(self) -> None:
        print('Game Saved')

    def quit_game(self) -> None:
        self.__playing = False
        print('Game finished')


if __name__ == '__main__':
    Game().play()
