import os
import time
import random
import msvcrt
from Biblioteca_RPG import print_attribut
from Biblioteca_RPG import roll_dice
from Biblioteca_RPG import print_loading
from Biblioteca_RPG import class_inf
from Biblioteca_RPG import print_introduction
from Biblioteca_RPG import map
from Biblioteca_RPG import change_char
import copy
from pygame import mixer

mixer.init()

class Character:
    def __init__(self) -> None:
        self.name = None
        self.rpg_class = None
        self.items = []

    def set_name(self,name):
        self.name = name

    def set_rpg_class(self,rpg_class):
        self.rpg_class = rpg_class

    @property
    def inf(self):
        print(f'Informações sobre {self.name}\n'
              f'Força: {self.Strn}\n'
              f'Constituição: {self.Cos}\n'
              f'Destreza: {self.Dex}\n'
              f'Magia: {self.Mag}\n'
              f'Vida: {self.Life}\n'
              f'Dano: {self.Dam}\n'
              f'Tipo de dano: {self.Type}\n'
              f'Fraqueza: {self.Weak}\n'
              f'Classe de Armadura: {self.Ca}\n')
              
    def give_attribut(self):
        match self.rpg_class:
            case 'warrior':
                self.Strn = 3
                self.Cos = 4
                self.Dex = 1
                self.Mag = 0
                self.Type = 'Slash'
                self.Weak = 'Magic'
                self.Life = random.randrange(80,121)
                self.Dam = random.randrange(50,81)
                self.Ca = 16
                self.Weapon = 'Machado'
            case 'rogue':
                self.Strn = 2
                self.Cos = 2
                self.Dex = 4
                self.Mag = 0
                self.Type = 'Piercing'
                self.Weak = 'Slash'
                self.Life = random.randrange(50,91)
                self.Dam = random.randrange(30,71)
                self.Ca = 15
                self.Weapon = 'Adaga'
            case 'mage':
                self.Strn = 1
                self.Cos = 1
                self.Dex = 2
                self.Mag = 4
                self.Type = 'Magic'
                self.Weak = 'Piercing'
                self.Life = random.randrange(30,71)
                self.Dam = random.randrange(30,91)
                self.Ca = 13
                self.Weapon = 'Cajado'
            case 'hunter':
                self.Strn = 3
                self.Cos = 2
                self.Dex = 3
                self.Mag = 0
                self.Type = 'Piercing'
                self.Weak = 'Slash'
                self.Life = random.randrange(60,101)
                self.Dam = random.randrange(50,61)
                self.Ca = 15
                self.Weapon = 'Besta'
            case 'priest':
                self.Strn = 1
                self.Cos = 4
                self.Dex = 0
                self.Mag = 3
                self.Type = 'Magic'
                self.Weak = 'Piercing'
                self.Life = random.randrange(60,101)
                self.Dam = random.randrange(10,41)
                self.Heal = random.randrange(30,61)
                self.Ca = 14
                self.Weapon = 'Pergaminhos'
            case 'paladin':
                self.Strn = 3
                self.Cos = 3
                self.Dex = 1
                self.Mag = 1
                self.Type = 'Slash'
                self.Weak = 'Magic'
                self.Life = random.randrange(90,111)
                self.Dam = random.randrange(30,61)
                self.Heal = random.randrange(10,31)
                self.Ca = 17
                self.Weapon = 'Espada'

    def show_life(self):
         print_attribut(self.Life)

    def show_damage(self):
         print_attribut(self.Dam)

    def show_heal(self):
         print_attribut(self.Heal)

class Monster(Character):

    def give_attribut(self):
        match self.rpg_class:
            case 'Slunker':
                self.Strn = 1
                self.Cos = 1
                self.Dex = 1
                self.Mag = 0
                self.Type = 'Slash'
                self.Weak = 'Magic'
                self.Life = random.randrange(30,61)
                self.Dam = random.randrange(10,31)
                self.Ca = 10
            case 'Flunker':
                self.Strn = 1
                self.Cos = 2
                self.Dex = 3
                self.Mag = 0
                self.Type = 'Piercing'
                self.Weak = 'Slash'
                self.Life = random.randrange(10,41)
                self.Dam = random.randrange(20,41)
                self.Ca = 10
            case 'Hunker':
                self.Strn = 1
                self.Cos = 3
                self.Dex = 1
                self.Mag = 1
                self.Type = 'Magic'
                self.Weak = 'Piercing'
                self.Life = random.randrange(50,81)
                self.Heal = random.randrange(20,41)
                self.Ca = 12
            case 'FireFlunker':
                self.Strn = 0
                self.Cos = 1
                self.Dex = 3
                self.Mag = 2
                self.Type = 'Magic'
                self.Weak = 'Piercing'
                self.Life = random.randrange(20,41)
                self.Dam = random.randrange(40,71)
                self.Ca = 12
            case 'BigSlunker':
                self.Strn = 3
                self.Cos = 3
                self.Dex = 0
                self.Mag = 0
                self.Type = 'Slash'
                self.Weak = 'Magic'
                self.Life = random.randrange(90,111)
                self.Dam = random.randrange(30,61)
                self.Ca = 15
            case 'BlessesHunker':
                self.Strn = 0
                self.Cos = 4
                self.Dex = 1
                self.Mag = 3
                self.Type = 'Magic'
                self.Weak = 'Piercing'
                self.Life = random.randrange(60,101)
                self.Heal = random.randrange(40,81)
                self.Ca = 16

class Battle(Character):

    def __init__(self,*fighters) -> None:
        super().__init__()
        for fighter in fighters:
            fighter.aux_dam = fighter.Dam
            fighter.aux_life = fighter.Life
    
    def Attack(self,attacker,defender):
        print(f'{attacker.name} ataca {defender.name}')
        time.sleep(3)
        res = roll_dice(attacker.Strn)
        if res == 1+attacker.Strn:
            time.sleep(3)
            print(f'{attacker.name} obteve uma falha crítica')
            time.sleep(3)
            print(f'Pelo resto da batalha {attacker.name} possuirá -5 de ataque')
            attacker.aux_dam -= 5
        elif res > 1 and res < defender.Ca:
            time.sleep(3)
            print(f'{defender.name} esquivou do ataque')
            time.sleep(3)
        elif res == 20+attacker.Strn:
            attacker.aux_dam = random.randrange(attacker.aux_dam - 20,attacker.aux_dam + 20)
            time.sleep(3)
            print(f'Uau, {attacker.name} obteve um acerto crítico')
            time.sleep(3)
            print(f'{attacker.name} ataca ferozmente {defender.name}')
            time.sleep(3)
            if attacker.Type == defender.Weak:
                print('Nossa o ataque foi super-efetivo')
                print(f'{defender.name} recebeu {attacker.aux_dam*4} de dano')
                time.sleep(3)
                defender.aux_life -= attacker.aux_dam*4
            else:
                print(f'{defender.name} recebeu {attacker.aux_dam*2} de dano')
                time.sleep(3)
                defender.aux_life -= attacker.aux_dam*2
        else:
            attacker.aux_dam = random.randrange(attacker.aux_dam - 20,attacker.aux_dam + 20)
            time.sleep(3)
            print(f'{attacker.name} acertou {defender.name}')
            time.sleep(3)
            if attacker.Type == defender.Weak:
                print('Nossa o ataque foi super-efetivo')
                print(f'{defender.name} recebeu {attacker.aux_dam*2} de dano')
                time.sleep(3)
                defender.aux_life -= attacker.aux_dam*2
            else:
                print(f'{defender.name} recebeu {attacker.aux_dam} de dano')
                time.sleep(3)
                defender.aux_life -= attacker.aux_dam
        if defender.aux_life <= 0:
            print(f'{defender.name} foi derrotado')
            time.sleep(2)
            return True
        else:
            return False
    
    def Healing(self, fighter):
        print(f'{fighter.name} tenta se curar')
        time.sleep(3)
        if hasattr(fighter,'Heal'):
            res = roll_dice(fighter.Cos)
            if res == 1+fighter.Cos:
                print(f'{fighter.name} obteve uma falha crítica')
                time.sleep(3)
                print(f'Pelo resto da batalha {fighter.name} possuirá -5 de vida')
                fighter.aux_life -= 5
            elif res > 1 and res < fighter.Ca:
                print(f'Nossa, parece que {fighter.name} falhou em se curar')
                time.sleep(3)
            elif res == 20+fighter.Cos:
                print(f'Uau, {fighter.name} obteve um acerto crítico')
                time.sleep(3)
                print(f'{fighter.name} se cura perfeitamente')
                time.sleep(3)
                print(f'{fighter.name} recuperou toda a sua vida')
                time.sleep(3)
                fighter.aux_life = fighter.Life
            else:
                if fighter.aux_life != fighter.Life:
                    fighter.Heal = random.randrange(fighter.Heal - 20,fighter.Heal + 20)
                    print(f'Ótimo, {fighter.name} conseguiu se curar')
                    time.sleep(3)
                    print(f'{fighter.name} se cura em {fighter.Heal}')
                    time.sleep(3)
                    fighter.aux_life += fighter.Heal
                    if fighter.aux_life > fighter.Life:
                        fighter.aux_life = fighter.Life
                else:
                    print(f'A vida de {fighter.name} já está cheia')
            return True
        else:
            print(f'a classe de {fighter.name} não pode se curar')
            time.sleep(5)
            return False

    def use_item(self,fighter,item):
        match item:
            case 'poção':
                print(f'{fighter.name} usou poção')
                time.sleep(3)
                print(f'{fighter.name} recuperou 50 de Vida')
                fighter.aux_life += 50
                if fighter.aux_life > fighter.Life:
                    fighter.aux_life = fighter.Life
            case 'bomba':
                print(f'{fighter.name} tomou bomba')
                time.sleep(3)
                print(f'{fighter.name} aumentou seu dano em 50')
                fighter.aux_dam += 50



    def battle_inf(self, fighter):
        print('Informações atuais de batalha: ')
        print(f'{fighter.name} possui {fighter.aux_life} de vida')
        print(f'{fighter.name} possui {fighter.aux_dam} de dano em média')
        print(f'{fighter.name} possui {fighter.Strn} de força')
        print(f'{fighter.name} possui {fighter.Dex} de destreza')
        print(f'{fighter.name} possui {fighter.Cos} de constituição')
        print(f'{fighter.name} possui {fighter.Mag} de magia')
        print(f'{fighter.name} possui {fighter.Ca} de CA')
        if hasattr(fighter,'Heal'):
            print(f'{fighter.name} possui {fighter.Heal} de cura em média')
        print('Digite qualquer coisa para prosseguir: ')
        pausa = msvcrt.getch()
        return False

def start_battle(protagonist,*fighters):

    fighters_num = 0

    fight = Battle(protagonist,*fighters)
    
    for fighter in fighters:
        
        if fighters_num:
            print(f'e {fighters[fighters_num].name}',end=' ')
            fighters_num+=1
        else:
            print(f'{protagonist.name} entrou em combate com {fighters[fighters_num].name}',end=' ')
            fighters_num+=1
    
    time.sleep(3)

    turn_order = sorted([protagonist,*fighters],key= lambda obj: obj.Dex,reverse=True)
    turn_order_name = [
        fighter.name for fighter in turn_order
    ]
    fighters_alive = turn_order.copy()
    fighters_alive.remove(protagonist)
    
    time.sleep(2)
    print(f'A ordem dos turnos será:')
    print(*turn_order_name,sep='\n')
    time.sleep(3)

    while True:
        monster_number = 0
        fighters = tuple(fighters_alive)
        for fighter in turn_order:
            if fighter == protagonist:
                while True:
                    print('Seu turno começou, qual sua ação?\n')
                    print('[1] Atacar')
                    print('[2] Curar')
                    print('[3] Ver informações de personagem')
                    print('[4] Usar um item')
                    choice = msvcrt.getch()
                    
                    if choice.decode() == '1':
                        i = 0
                        print('Escolha o seu alvo: ')
                        for fighter in fighters:
                            print(f'[{i+1}] {fighter.name}')
                            i+=1
                        target = msvcrt.getch()
                        target = int(target.decode())
                        target -= 1

                        if fight.Attack(protagonist,fighters[target]):
                            turn_order.remove(fighters[target])
                            fighters_alive.remove(fighters[target])
                            fighters = tuple(fighters_alive)
                            monster_number -=1
                        break

                    elif choice.decode() == '2':
                        fight.Healing(protagonist)
                        break
                    elif choice.decode() == '3':
                        fight.battle_inf(protagonist)
                        continue
                    elif choice.decode() == '4':
                        i = 0
                        print('Escolha o Item: ')
                        for item in protagonist.items:
                            print(f'[{i+1}] {item}')
                            i+=1
                        target = msvcrt.getch()
                        target = int(target.decode())
                        target -= 1
                        fight.use_item(protagonist,protagonist.items[target])
                        break
                    else:
                        print('Ação inválida, tente novamente')
                        time.sleep(3)
                        continue
                if len(turn_order) == 1:
                    os.system('cls')
                    print('Todos os inimigos foram derrotados')
                    time.sleep(3)
                    print('Parabéns você venceu')
                    pause = msvcrt.getch()
                    return True
            else:
                if hasattr(fighters[monster_number],'Heal') and fighters[monster_number].Life < fighters[monster_number].Life/4:
                    fight.Healing(fighters[monster_number])
                else:
                    if fight.Attack(fighters[monster_number],protagonist):
                        os.system('cls')
                        print('GAME OVER, Você foi derrotado <o>')
                        exit()
                    monster_number += 1

#funções que contam a história:

def create_protagonist():
    Rpg_classes = ['mage','warrior','rogue','priest','paladin','hunter']
    global protagonist
    protagonist = Character()
    print('Crie seu personagem')
    while True:
        Name = input('Escolha o seu nome: ')
        print(f'Tem certeza que seu nome será {Name}?')
        print('Aperte "E" para confirmar ou outro botão para voltar')
        Choice = msvcrt.getch().lower()
        if Choice.decode() != 'e':
            continue
        protagonist.set_name(Name)
        while True:
            print('Para ver as classes de RPG.py digite "inf"')
            Rpg_class = input('Escolha a sua classe: ').lower()
            if Rpg_class == 'inf':
                class_inf()
                os.system('cls')
                continue
            elif Rpg_class not in Rpg_classes:
                print('A classe digitada não existe, lembre de escrever a classe em inglês')
                continue
            print(f'Tem certeza que sua classe será {Rpg_class}?')
            print('Aperte "E" para confirmar ou outro botão para voltar')
            Choice = msvcrt.getch().lower()
            if Choice.decode() != 'e':
                continue
            protagonist.set_rpg_class(Rpg_class)
            protagonist.give_attribut()
            return True

def def_att(char):
    if hasattr(char,'Heal'):
        print('Agora vamos definir a sua vida, cura e o seu ataque')
        time.sleep(2)
        print('Primerio vamos definir a sua vida')
        time.sleep(2)
        char.show_life()
        print(f'Pronto, sua vida é {char.Life}')
        time.sleep(2)
        print('Beleza, próximo passo é definir o seu ataque')
        time.sleep(2)
        char.show_damage()
        print(f'Ok, seu ataque é {char.Dam}')
        time.sleep(2)
        print('Por fim vamos definir a sua cura')
        time.sleep(2)
        char.show_heal()
        print(f'Pronto, sua cura é {char.Heal}')
        time.sleep(2)
        print('Feito, todos os seus atributos já foram definidos')
        return True
    else: 
        print('Agora vamos definir a sua vida e o seu ataque')
        time.sleep(2)
        print('Primerio vamos definir a sua vida')
        time.sleep(2)
        char.show_life()
        print(f'Pronto, sua vida é {char.Life}')
        time.sleep(2)
        print('Próximo passo é definir o seu ataque')
        time.sleep(2)
        char.show_damage()
        print(f'Ok, seu ataque é {char.Dam}')
        time.sleep(2)
        print('Feito, todos os seus atributos já foram definidos')
        return True
    
def print_logo():
    mixer.music.load('C:\\Programando\\Programação\\Python\\Projeto_Daniel\\Menu_projeto.wav')
    mixer.music.play(-1)
    os.system('cls')
    time.sleep(4)
    print('      #########')
    print('    ###   #   ###')
    print('   ##    ###    ##')
    print('    ###   #   ###')
    print('      #########')
    time.sleep(4)
    print('\nLucca Games presents.')
    time.sleep(5)
    os.system('cls')

def print_menu():
    print('##### ##### #####    ##### ## ##    #####   #####')
    print('#   # #   # #        #   #  ###    ##   ## ##   ##')
    print('##### ##### #  ##    #####   #    ##     ###     ##')
    print('#  #  #     #   #    #       #     ##   ## ##   ##')
    print('#   # #     #####  # #       #      #####   #####')
    print('\nO enigma de PY\n\n')
    print('Aperte "S" para iniciar o jogo')
    print('Aperte "Q" para fechar o jogo')

def chapter_one_map():

    player_char = '8'
    item_char = '!'
    player_x = 5
    player_y = 2
    interact = 0
    map_number = 0

    house_high = 5
    house_large = 11
    house = map(house_high,house_large)
    house[0] = change_char(house[0],' ',4,5,6)
    house[3] = change_char(house[3],item_char,9)
    aux_house = copy.deepcopy(house)
    
    while map_number == 0:
        house = copy.deepcopy(aux_house)
        house[player_y] = change_char(house[player_y],player_char,player_x)
        print('Aperte "I" para interagir com o cenário')
        print(*house, sep='\n')
        move = msvcrt.getch().lower()

        match move.decode():
            case'w':
                if house[player_y-1][player_x] == ' ':
                    player_y-=1
            case's':
                if house[player_y+1][player_x] == ' ':
                    player_y+=1
            case'd':
                if house[player_y][player_x+1] == ' ':
                    player_x+=1
            case'a':
                if house[player_y][player_x-1] == ' ':
                    player_x-=1
            case'i':
                interact = 1

        if player_x == 4 and player_y == 0 or player_x == 5 and player_y == 0 \
        or player_x == 6 and player_y == 0:
            map_number+=1

        if (player_x == 8 and player_y == 3 or player_x == 9 and player_y == 2) and interact == 1:
            print(f'Você achou uma poção')
            protagonist.items.append('poção')
            pause = msvcrt.getch()
            aux_house[3] = change_char(aux_house[3],' ',9)
            
        
        interact = 0
        os.system('cls')

    map_one_high = 15
    map_one_large = 101
    map_one = map(map_one_high,map_one_large)

    for draw in range(1,14):
        if draw == 4 or draw == 10:
            map_one[draw] = change_char(map_one[draw],'*',21,22,23,24,25,26,27,28,29,41,42,43,44,45,46,47,48,49,61,62,63,64,65,66,67,68,69)
        if draw == 5 or draw == 9:
            map_one[draw] = change_char(map_one[draw],'*',1,2,3,4,5,6,7,8,9)
            map_one[draw] = change_char(map_one[draw],'(',95)
        elif draw == 6 or draw == 7 or draw == 8:
            map_one[draw] = change_char(map_one[draw],'-',1,2,3,4,5,6,7,8)
            map_one[draw] = change_char(map_one[draw],'*',9)
            if draw != 7:
                map_one[draw] = change_char(map_one[draw],'=',94,95,96,97,98,99)
        else:
            map_one[draw] = change_char(map_one[draw],'*',21,29,41,49,61,69)
            map_one[draw] = change_char(map_one[draw],'(',95)

    map_one[2] = change_char(map_one[2],item_char,2)
    map_one[12] = change_char(map_one[12],item_char,55)

    enemy_char = 'm'
    strong_enemy_char = 'M'
    aux_map_one = copy.deepcopy(map_one)
    player_x = 11
    player_y = 7
    enemy_x = 50
    enemy_y = 7
    strong_enemy_x = 80
    strong_enemy_y = 3
    not_shift = 1
    Goblin = Monster()
    Goblin.set_name('Goblin')
    Goblin.set_rpg_class('Slunker')
    Goblin.give_attribut()
    Skull = Monster()
    Skull.set_name('Skull')
    Skull.set_rpg_class('FireFlunker')
    Skull.give_attribut()
    Imp = Monster()
    Imp.set_name('Diabrete')
    Imp.set_rpg_class('FireFlunker')
    Imp.give_attribut()

    while map_number == 1:
        map_one = copy.deepcopy(aux_map_one)
        map_one[player_y] = change_char(map_one[player_y],player_char,player_x)
        map_one[enemy_y] = change_char(map_one[enemy_y],enemy_char,enemy_x)
        map_one[strong_enemy_y] = change_char(map_one[strong_enemy_y],strong_enemy_char,strong_enemy_x)
        if not_shift:
            print('Aperte shift para correr')
        print('Objetivo: Vá até a ponte')
        print(*map_one, sep='\n')

        move = msvcrt.getch()
        enemy_move = random.randrange(0,4)
        strong_enemy_move = random.randrange(0,2)

        match move.decode():
            case'w':
                if map_one[player_y-1][player_x] == ' ':
                    player_y-=1
            case's':
                if map_one[player_y+1][player_x] == ' ':
                    player_y+=1
            case'd':
                if map_one[player_y][player_x+1] == ' ':
                    player_x+=1
            case'a':
                if map_one[player_y][player_x-1] == ' ':
                    player_x-=1
            case'i':
                interact = 1
            case'W':
                not_shift = 0
                if map_one[player_y-2][player_x] == ' ' and map_one[player_y-1][player_x] == ' ':
                    player_y-=2
            case'S':
                not_shift = 0
                if map_one[player_y+2][player_x] == ' ' and map_one[player_y+1][player_x] == ' ':
                    player_y+=2
            case'D':
                not_shift = 0
                if map_one[player_y][player_x+2] == ' ' and map_one[player_y][player_x+1] == ' ':
                    player_x+=2
            case'A':
                not_shift = 0
                if map_one[player_y][player_x-2] == ' ' and map_one[player_y][player_x-1] == ' ':
                    player_x-=2
            case'I':
                interact = 1

        match enemy_move:
            case 0:
                if map_one[enemy_y-1][enemy_x] == ' ' or map_one[enemy_y-1][enemy_x] == player_char:
                    enemy_y-=1
            case 1:
                if map_one[enemy_y+1][enemy_x] == ' ' or map_one[enemy_y+1][enemy_x] == player_char:
                    enemy_y+=1
            case 2:
                if map_one[enemy_y][enemy_x+1] == ' ' or map_one[enemy_y][enemy_x+1] == player_char:
                    enemy_x+=1
            case 3:
                if map_one[enemy_y][enemy_x-1] == ' ' or map_one[enemy_y][enemy_x-1] == player_char:
                    enemy_x-=1

        match strong_enemy_move:
            case 0:
                if player_y < strong_enemy_y:
                    if map_one[strong_enemy_y-1][strong_enemy_x] == ' ' or map_one[enemy_y-1][enemy_x] == player_char:
                        strong_enemy_y-=1
                else:
                    if map_one[strong_enemy_y+1][strong_enemy_x] == ' ' or map_one[enemy_y+1][enemy_x] == player_char:
                        strong_enemy_y+=1
            case 1:
                if player_x > strong_enemy_x:
                    if map_one[strong_enemy_y][strong_enemy_x+1] == ' ' or map_one[enemy_y][enemy_x+1] == player_char:
                        strong_enemy_x+=1
                else:
                    if map_one[strong_enemy_y][strong_enemy_x-1] == ' ' or map_one[enemy_y][enemy_x-1] == player_char:
                        strong_enemy_x-=1

        if (player_x == 3 and player_y == 2 or player_x == 2 and player_y == 3 or player_x == 2 and player_y == 1 or player_x == 1 and player_y == 2) and interact == 1:
            print(f'Você achou uma bomba')
            protagonist.items.append('bomba')
            pause = msvcrt.getch()
            aux_map_one[2] = change_char(aux_map_one[2],' ',2)

        if (player_x == 56 and player_y == 12 or player_x == 54 and player_y == 12 or player_x == 55 and player_y == 13 or player_x == 55 and player_y == 11) and interact == 1:
            print(f'Você achou uma poção')
            protagonist.items.append('poção')
            pause = msvcrt.getch()
            aux_map_one[12] = change_char(aux_map_one[12],' ',55)

        if player_x == enemy_x and player_y == enemy_y:
            start_battle(protagonist,Goblin)
            enemy_x = 1
            enemy_y = 7
            enemy_char = '-'
        
        if player_x == strong_enemy_x and player_y == strong_enemy_y:
            start_battle(protagonist,Imp,Skull)
            strong_enemy_x = 2
            strong_enemy_y = 7
            strong_enemy_char = '-'

        if player_x == 99 and player_y == 7:
            return True
        interact = 0
        os.system('cls')
        
def chapter_one():
    print('Você arruma sua mochila com suprimentos suficientes para a próxima semana')
    time.sleep(4)
    print('Além disso, talvez seja inteligente levar uma arma com você')
    time.sleep(3)
    print(f'{protagonist.name} obteve {protagonist.Weapon}')
    time.sleep(3)
    print('Você sente o peso da mochila em suas costas')
    time.sleep(4)
    print('Provavelmente em pouco tempo sua casa será destrúida')
    time.sleep(4)
    print('Você lembra que trabalhou duro para tê-la')
    time.sleep(3)
    print('Abdicou de passar tempo com sua família e amigos')
    time.sleep(3)
    print('Tudo para ter um teto em cima de sua cabeça')
    time.sleep(3)
    print('Ter uma casa deveria ser o mínimo que você merece por se esforçar tanto')
    time.sleep(4)
    os.system('cls')
    print('Então por que você está nessa situação?')
    time.sleep(4)
    print('Isso é culpa sua?')
    time.sleep(3)
    print('Não tem como ser')
    time.sleep(3)
    os.system('cls')
    print('Não tem como ser.')
    time.sleep(3)
    os.system('cls')
    print('Não tem como ser..')
    time.sleep(3)
    os.system('cls')
    print('Não tem como ser...')
    time.sleep(3)
    os.system('cls')
    print('já está quase amanhecendo')
    time.sleep(3)
    print('Você decide que é melhor já ir andando...')
    chapter_one_map()
    print('Você venceu, o resto ainda está em desenvolvimento')
    return True

print_logo()

while True:
    print_menu()
    player_input = msvcrt.getch()
    if player_input.decode() == 'q':
        mixer.music.pause()
        break
    elif player_input.decode() == 's':
        mixer.music.pause()
        print_loading(2)
        print('Gostaria de ver a introdução do jogo?')
        print('Aperte "E" para ver, ou outra coisa para pular')
        choice = msvcrt.getch().lower()
        if choice.decode() == 'e':
            print_loading(2)
            print_introduction()
        print_loading(2)
        create_protagonist()
        os.system('cls')
        def_att(protagonist)
        time.sleep(4)
        print('Voltando a história...')
        time.sleep(4)
        print_loading(1)
        chapter_one()
        break
    else:
        os.system('cls')
        print('Opção inválida')
        continue

print('Jogo finalizado com sucesso, volte sempre!')
