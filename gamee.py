from card import Card
import random
import time
from bag import Bag

def game():

    user = Card((input('            ПРИВЕТСВУЮ В ИГРЕ ЮЗЕР,\n'
                       'ДЛЯ ТОГО ЧОБЫ НАЧАТЬ ИГРАТЬ В ЛОТТО ВВЕДИ СВОЕ ИМЯ: ')))
    comp = Card('Я_Компуктер')
    # time.sleep(1)
    user.show_card()
    print(" Взгляни на свою карточку и возрадуйся :)")
    time.sleep(6)
    print('\nКраткие правила:\nКомпьютер достает первый бочёнок с номером!\n'
          'Eсли на твоей карточке есть клетка с номером выпавшего бочёнка,\n'
          'то ты должен нажать "Y", если нет, в таком случае нажимай "N"')
    time.sleep(9)
    # toss2 = int(random.randint(0,1))
    # toss = input('\nДля начала давай проведём жеребьёвку, кто ходит первый'
    #       '\nВыбери цифру  1 или 0 и введи её: ')
    # time.sleep(1)
    # if int(toss) == int(toss2):
    #     print('\nПоздравляю, удача на твоей стороне, ты ходишь первым\n ГОТОВЬСЯ')
    #     toss = 1
    #     # если она равна единице, то первым ходит юзер, если нет соотвественно комп
    # else:
    #     print('\nИзвини, но тебе не повезло, ты ходишь вторым.\n ГОТОВЬСЯ')
    #     toss = 2
    print('ГОТОВЬСЯ')
    time.sleep(1)
    print('     1')
    time.sleep(2)
    print('     2')
    time.sleep(2)
    print('     3')

    print('\nИГРА НАЧАЛАСЬ\n\n')
    bag = Bag()
    for i in range(1, 91):
        if user.find_num == True and comp.find_num == True:
            # print(f'Вытаскиваем бочёнок номер {i}')
            #time.sleep(1)
            # print(f'{i}-ый бочёнок имеет номер :')
            # x = bag.get_keg
            # print(x)
            # # bag.lets_see_bag
            toss = 1
            if toss == 1:
                time.sleep(2)
                print('----------------------------------------------------')
                print('Трясем мешок')
                time.sleep(3)
                x = bag.get_keg
                print(f'Вытаскиваем бочёнок номер {x}\n')
                time.sleep(3)
                comp.show_card()
                user.show_card()
                print('Компуктер, есть ли у тебя такая цифра или нет?(Y or N)')
                time.sleep(3)
                comp_chance = random.randint(0, 101)
                if comp_chance < 95:
                    if str(x) in comp._return_matrx():
                        comp_input = 'Y'
                        print(comp_input)
                    else:
                        comp_input = 'N'
                        print(comp_input)
                else:
                    if str(x) in comp._return_matrx():
                        comp_input = 'N'
                        print(comp_input)
                    else:
                        comp_input = 'Y'
                        print(comp_input)
                if comp_input == 'Y':
                    comp.if_copm_tap_y(x)
                    if comp.find_num == True:
                        time.sleep(2)
                        toss = 2
                    else:
                        print('у compuctera нет чисел в карточке, но игра идет дальше, видимо где-то произошел сбой')
                        raise SystemExit
                elif comp_input == 'N':
                    comp.if_copm_tap_n(x)
                    toss = 2
                user_input = input('Есть ли у тебя такая цифра??(Y or N)')
                if user_input == 'y' or user_input == 'Y':
                    user.if_copm_tap_y(x)
                    if user.find_num == True:
                        time.sleep(3)
                        print('Хорошо!')
                        toss = 2
                    else:
                        print('у тебя нет чисел в карточке, но игра идет дальше, видимо где-то произошел сбой')
                        raise SystemExit
                elif user_input == 'n' or user_input == 'N':
                    user.if_tap_n(x)
                    toss = 2
                else:
                    print('Вероятно вы ошиблись! Вы должны ответить да(Y), либо нет(N)')
                print('----------------------------------------------------')



game()


