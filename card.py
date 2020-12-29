import random, time

class Card:
    def __init__(self, name):
        self.name = name
        self.__matrix = []
        self.c = False

    def __make_card(self):
        while not self.c:
            user_card = []
            list_of_nums = list(range(1, 90))  # список чисел которым заполняется карточка
            count = 1
            for i in range(3):
                matx = []
                for i in range(5):
                    counter = random.randint(0, len(list_of_nums) - 1)
                    num = list_of_nums[counter]
                    matx.append(num)
                    list_of_nums.remove(num)
                for i in range(4):
                    matx.append(' ')
                random.shuffle(matx)
                for i in range(9):
                    user_card.append(str(matx[i]))
            self.__matrix = user_card
            self.c = True

#показ карточки игрока
    def show_card(self):
        self.__make_card()
        print(f'Карточка принадлежит {self.name}')
        print('------------------------')
        print(' '.join(self.__matrix[:9]))
        print(' '.join(self.__matrix[9:18]))
        print(' '.join(self.__matrix[18:28]))
        print('------------------------\n')


#возврат списка номеров карточки
    def _return_matrx(self):
        self.__make_card()
        # print(type(self.__matrix))
        return self.__matrix

# проверим наличие цифр в карточке игрока
    @property
    def find_num(self):
        self.num_count = 0
        self_matx = self._return_matrx()
        for i in range(len(self_matx)):
            try:
                num = int(self_matx[i])
                self.num_count += 1
            except ValueError:
                pass
        if self.num_count > 0:
            return True
        elif self.num_count < 0:
            return False


    def if_tap_y(self, value):
        if str(value) in self.__matrix:
            self.__matrix.insert(self.__matrix.index(str(value)), ' X ')
            self.__matrix.remove(str(value))
            print('Верно! Идем дальше!')

            return True
        else:
            print("Ты совершил ошибку, такого числа у тебя на карточке нет!\nТы проиграл")
            time.sleep(3)
            print('ПОК')
            raise SystemExit

    def if_copm_tap_y(self, value):
        if str(value) in self.__matrix:
            self.__matrix.insert(self.__matrix.index(str(value)), ' X ')
            self.__matrix.remove(str(value))
            print('Компуктер прав! Идем дальше!')

            return True
        else:
            print("Компуктер ошибся, ты победил")
            time.sleep(6)
            print('ПОК')
            raise SystemExit

    def if_copm_tap_n(self, value):
        if str(value) in self.__matrix:
            print("Компуктер ошибся, ты победил")
            time.sleep(6)
            print('ПОК')
            raise SystemExit
        else:
            print("Верно! Идем дальше!")
            return True

    def if_tap_n(self, value):
        if str(value) in self.__matrix:
            print("Ты совершил ошибку, это число у тебя есть!\nТы проиграл")
            time.sleep(3)
            print('ПОК')
            raise SystemExit
        else:
            print("Верно! Идем дальше!\n")
            return True

# b=Card('bob')
# b.show_card()
# print(b._return_matrx())
# if str(39) in b._return_matrx():
#     print('yup')
# elif str(5) not in b._return_matrx():
#     print('no')