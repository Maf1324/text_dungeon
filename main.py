from utils import handle_choice, row_print

# Lista de afazeres
# TODO criar classe Player

"""
A classe Game:
    - Inicia o objeto jogo
    - Cria um objeto de jogador usando a classe Player
    - Inicia o loop principal do jogo
    Tera as funções:
        - criar dungeon


O loop principal:
    Terá uma variavel que vai controlar o loop "playing"
    Ira mostrar as opções que o usuario poderá escolher:
        - Dungeon
        - Itens --> Função será criada dentro do objeto de personagem
        - Save
        - Quit

"""


class Game:

    def __init__(self) -> None:
        self._player = 'Will creat a player'  # TODO criar classe Player
        self.__playing = True
        self.__menu_choices = {
            '1': self.run_dungeon,
            '2': 'Show itens',  # TODO criar função na classe Player
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
