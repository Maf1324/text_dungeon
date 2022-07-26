"""
Classe Stats:
    - Atributos:
        * Hp, será avaliado para setar o atributo "current_hp" ao iniciar uma
        rodada de dungeon;
        * Atk, será avaliado na hora de calcular o dano de um ataque;
        * Def, será avaliado na hora de calcular o dano de um ataque;
        * Spd, será avaliado na hora de calcular a ordem de ataque no turno;
        * Current HP, será avaliado durante batalhas, se Hp <= 0 a batalha será
        encerrada.

    - Metodos:
        * Reduce / increase _hp, serão usados para alterar o "current_hp" do
        personagem sem alterar o status "Hp" base;
        * set_current_Hp, vai ser usada ao iniciar a dungeon para setar o valor
        de "current_hp";
        * Handle_level_up, é chamado pela classe Player para atualizar os stats
        do mesmo;
        * Creat_new_stats, retorna um dict que será usado para somar os novos
        pontos de stats do Player. Ela itera pelos valores de stats e solicita
        o valor a ser adicionado aos mesmo. Ao final da iteração, o total deve
        ser N == 5 -> True, ou será iniciada uma nova iteração dos valores.
"""

from typing import Dict

from utils import get_int_input, row_print


class Stats:
    def __init__(self, Hp=10, Atk=1, Def=1, Spd=1) -> None:
        self.__base_stats = {
            'base_Hp': Hp,
            'base_Atk': Atk,
            'base_Def': Def,
            'base_Spd': Spd
        }
        # self.Hp = Hp
        # self.Atk = Atk
        # self.Def = Def
        # self.Spd = Spd
        self.current_hp = None

    @property
    def Hp(self):
        return self.__base_stats['base_Hp']

    @property
    def Def(self):
        return self.__base_stats['base_Def']

    @property
    def Atk(self):
        return self.__base_stats['base_Atk']

    @property
    def Spd(self):
        return self.__base_stats['base_Spd']

    @classmethod
    def new_enemy_stat(cls, Hp, Atk, Def, Spd):
        return cls(Hp, Atk, Def, Spd)

    def set_current_Hp(self):
        self.current_hp = self.__base_stats['base_Hp']

    def reduce_hp(self, amount):
        print(self, type(amount))
        self.current_hp -= amount

    def increase_hp(self, amount):
        self.current_hp += amount

    def handle_level_up(self):
        new_stats = self.creat_new_stats()
        for x in new_stats.keys():
            self.__base_stats[x] += new_stats[x]

    def creat_new_stats(self) -> Dict:
        new_stats = {}
        total = 0
        for key in self.__base_stats.keys():
            value = get_int_input(key.replace('base_', ''))
            new_stats[key] = value
            total += value
            if total > 5:
                row_print('Set only 5 points on your stats...')
                return self.creat_new_stats()
            if total == 5:
                break

        if total < 5:
            row_print(f'You still have {5-total} points left to use')
            return self.creat_new_stats()

        new_stats['base_Hp'] *= 5 if new_stats['base_Hp'] is not None else 0
        return new_stats
