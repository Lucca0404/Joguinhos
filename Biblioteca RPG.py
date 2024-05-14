import os
import time
import random
import msvcrt
import copy

def print_attribut(attribut):
    numbers = '1234567890'
    form_word = ''
    aux_word = ''
    i = 0

    attribut = str(attribut)

    while i < len(attribut):

        sort_num = random.choice(numbers)
        form_word += sort_num
        time.sleep(0.05)
        os.system('cls')
        print(form_word)
        
        if sort_num == attribut[i]:
            aux_word += sort_num
            i += 1
            
        else:
            form_word = aux_word
            continue

def roll_dice(attribut):
    dice_result = random.randrange(1,21)
    test_result = dice_result + attribut

    print_attribut(test_result)
    if dice_result == 20:
        print('Acerto Crítico!!!')
    elif dice_result == 1:
        print('Erro crítico!!!')
    else:
        print(f'O resultado do dado foi {test_result}')
    return test_result

def print_loading(rep):
    for i in range(rep):
        print('Loading')
        time.sleep(0.5)
        os.system('cls')
        print('Loading.')
        time.sleep(0.5)
        os.system('cls')
        print('Loading..')
        time.sleep(0.5)
        os.system('cls')
        print('Loading...')
        time.sleep(0.5)
        os.system('cls')

def class_inf():
    while True:
        print('As classes de RPG.py definem o seu estilo de jogo, cada uma possui atributos, quantidade vida e ataque, e vantagens próprias ')
        print('Classes disponíveis:')
        print('- Guerreiro / Warrior')
        print('- Ladino / Rogue')
        print('- Mago / Mage')
        print('- Caçador / Hunter')
        print('- Sacerdote / Priest')
        print('- Paladino / Paladin')
        choice = input('Escolha uma classe para verificar suas informações ou aperte "S" para voltar a criação de personagem: ').lower()
        while choice != 's':
            print('Legenda: Strn = Força, Cos = Constituição, Dex = Destreza, Mag = magia, Life = Vida, Atk = Dano, Type = Tipo de dano, Heal = Cura, CA = Classe de armadura, Weak = Fraqueza')
            if choice == 'guerreiro' or choice == 'warrior':
                print('Warrior: Guerreiros são fortes e resistentes, possuem bastante vida e ataque e são ótimos para batalhas corpo-a-corpo')
                print('Status Warrior:')
                print('Strn: 3')
                print('Cos: 4')
                print('Dex: 1')
                print('Mag: 0')
                print('Life: 80-120')
                print('Atk: 50-80')
                print('CA: 16')
                print('Heal: N/A')
                print('Type: Slash')
                print('Weak: Magic')
                print('Aperte qualquer coisa para voltar')
                pause = msvcrt.getch()
                break
            elif choice == 'ladino' or choice == 'rogue':
                print('Rogue: Ladinos são ágeis e furtivos, possuem bastante destreza e dano e são ótimos enganadores')
                print('Status Rogue:')
                print('Strn: 2')
                print('Cos: 2')
                print('Dex: 4')
                print('Mag: 0')
                print('Life: 50-90')
                print('Atk: 30-70')
                print('CA: 15')
                print('Heal: N/A')
                print('Type: Piercing')
                print('Weak: Slash')
                pause = msvcrt.getch()
                break
            elif choice == 'mago' or choice == 'mage':
                print('Mage: Magos são inteligentes e sábios, possuem um alto dano mágico. Perfeito para pulverizar seu oponente')
                print('Status Mage:')
                print('Strn: 1')
                print('Cos: 1')
                print('Dex: 2')
                print('Mag: 4')
                print('Life: 30-70')
                print('Atk: 30-90')
                print('CA: 13')
                print('Heal: N/A')
                print('Type: Magic')
                print('Weak: Piercing')
                pause = msvcrt.getch()
                break
            elif choice == 'caçador' or choice == 'hunter':
                print('Hunter: Caçadores são espertos e atentos, possuem ótimas miras e sempre andam com suas armadilhas')
                print('Status Hunter:')
                print('Strn: 3')
                print('Cos: 2')
                print('Dex: 3')
                print('Mag: 0')
                print('Life: 60-100')
                print('Atk: 50-60')
                print('CA: 15')
                print('Heal: N/A')
                print('Type: Piercing')
                print('Weak: Slash')
                pause = msvcrt.getch()
                break
            elif choice == 'sacerdote' or choice == 'priest':
                print('Priest: Sacerdotes são sábios e pacientes, possuem poderes de cura incríveis e uma ótima resistência')
                print('Status Priest:')
                print('Strn: 1')
                print('Cos: 4')
                print('Dex: 0')
                print('Mag: 3')
                print('Life: 60-100')
                print('Atk: 10-40')
                print('CA: 14')
                print('Heal: 30-60')
                print('Type: Magic')
                print('Weak: Piercing')
                pause = msvcrt.getch()
                break
            elif choice == 'paladino' or choice == 'paladin':
                print('Paladin: Paladinos são fiéis e ótimos em combate, além de terem bastante dano e vida tambem conseguem se curar')
                print('Status Paladin:')
                print('Strn: 3')
                print('Cos: 3')
                print('Dex: 1')
                print('Mag: 1')
                print('Life: 90-110')
                print('Atk: 30-60')
                print('CA: 17')
                print('Heal: 10-30')
                print('Type: Slash')
                print('Weak: Magic')
                pause = msvcrt.getch()
                break
            else:
                print('Opção digitada é inválida, digite o nome de uma das classes')
                pause = msvcrt.getch()
                break
        break

def print_introduction():
    os.system('cls')
    print('Ano 16XX reino de PY',end=',')
    time.sleep(4.0)
    print(' um lugar de guerra e destruição')   
    time.sleep(4.0)
    print('Você é um morador do burgo de Flask, o maior centro comercial do reino de PY')
    time.sleep(4.0)
    print('Recentemente o mundo está presenciando a maior guerra já registrada em sua história')
    time.sleep(4.0)
    print('O exército dos guerreiros Django está dominando grande parte do continente e não vão parar até estabelerecerem a sua tirania')
    time.sleep(4.0)
    print('Em breve eles chegarão em sua cidade, e todos do exército de Flask estão preocupados com o resultado desse acontecimento')
    time.sleep(6.0)
    print('Aperte qualquer botão para prosseguir')
    pause = msvcrt.getch()
    os.system('cls')
    while True:
        print('Dia 1')
        time.sleep(5.0)
        print('São 4 horas da manhã e você acorda assustado com uma batida na porta')
        time.sleep(5)
        print('A lua está cheia lá fora, o brilho dela ilumina a sua janela')
        time.sleep(5)
        print('um silêncio quase perfeito toma conta do seu quarto')
        time.sleep(5)
        print('Ir até a porta?')
        time.sleep(1.5)
        print('\nEscolha um número referente a uma das opções abaixo:\n[1] Abrir a porta\n[2] Espiar quem está lá fora pela janela\n[3] Voltar a dormir')
        Choice = msvcrt.getch()
        if Choice.decode() == '1':
            print('Você anda cautelosamente até sua porta')
            time.sleep(5)
            print('Ao abrir a porta você olha para os lados e não vê nada muito especial')
            time.sleep(4)
            print('Porém ao olhar para baixo você enxerga uma carta em sua frente')
            time.sleep(4)
            print('Ao abrir a carta você encontra uma mensagem assinada pelo chefe do exército de Flask')
            time.sleep(5)
            print('Nela, ele ordena que todos os moradores retirem-se da cidade o mais rápido possível')
            time.sleep(5)
            print('O exercíto de Django se aproxima e logo todo o local será tomado por guerra e destruição')
            time.sleep(6)
            print('Você não parece ter muita opção...')
            time.sleep(4)
            print('Não é a primeira vez que as guerras pertubam a sua vida e nem será a última')
            time.sleep(5)
            print('Pegue seus pertences mais importantes e saia de sua casa o mais rápido possível')
            time.sleep(5)
            print('Aperte qualquer botão para prosseguir')
            pause = msvcrt.getch()
            return True
        elif Choice.decode() == '2':
            while True:
                print('Você espia pela janela e vê um ser de forma humanoide em frente a sua porta. Estranhamente a luz da lua não o ilumina')
                time.sleep(5)
                print('Não parece que ele vai sair dali tão cedo...')
                time.sleep(4)
                print('Abrir a porta?\n')
                print('[1] Abrir')
                print('[2] Voltar a dormir')
                Choice = msvcrt.getch()
                if Choice.decode() == '1':
                    print('Você anda cautelosamente até sua porta')
                    time.sleep(5)
                    print('Ao abrir a porta você olha para os lados e não vê nada muito especial')
                    time.sleep(4)
                    print('Porém ao olhar para baixo você enxerga uma carta em sua frente')
                    time.sleep(4)
                    print('Ao abrir a carta você encontra uma mensagem assinada pelo chefe do exército de Flask')
                    time.sleep(5)
                    print('Nela, ele ordena que todos os moradores retirem-se da cidade o mais rápido possível')
                    time.sleep(5)
                    print('O exercíto de Django se aproxima e logo todo o local será tomado por guerra e destruição')
                    time.sleep(6)
                    print('Você não parece ter muita opção...')
                    time.sleep(4)
                    print('Não é a primeira vez que as guerras pertubam a sua vida e nem será a última')
                    time.sleep(5)
                    print('Pegue seus pertences mais importantes e saia de sua casa o mais rápido possível')
                    time.sleep(5)
                    print('Aperte qualquer botão para prosseguir')
                    pause = msvcrt.getch()
                    return True
                elif Choice.decode() == '2':
                    print('Você ignora a batida na porta, fecha os olhos e volta para o seu sono profundo...')
                    time.sleep(4)
                    os.system('cls')
                    break
                else:
                    print('Opção inválida, escolha uma opção entre 1,2 ou 3')
                    print('Aperte qualquer botão para prosseguir')
                    pause = msvcrt.getch()
                    continue
        elif Choice.decode() == '3':
            print('Você ignora a batida na porta, fecha os olhos e volta para o seu sono profundo...')
            time.sleep(4)
            os.system('cls')
            continue
        else:
            print('Opção inválida, escolha uma opção entre 1,2 ou 3')
            print('Aperte qualquer botão para prosseguir')
            pause = msvcrt.getch()
            continue

def map(lines,collums):
    create_map = [
                '#'*collums if i == 0 or i == lines-1 else '#'+' '*(collums-2)+'#' for i in range(lines)
               ]
    return create_map
        
def change_char(string, new_char,*index):
    aux = 0
    for i in index:
        if aux == 0:
            new_string =string[:i] + new_char + string[i + 1:]
            aux+=1
        else:
            new_string = new_string[:i] + new_char + new_string[i + 1:]
    return new_string
