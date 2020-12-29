import random

class Bag:
    def __init__(self, count=1):
        self.__keg = list(range(1, 91))
        # self.__count = count

    # вытаскиваем боченок с номером
    @property
    def get_keg(self, count=1):
        if len(self.__keg) and count == 1:
            value = self.__keg[random.randint(0, len(self.__keg) - 1)]
            self.__keg.remove(value)
            count = 0
            return value
        else:
            return 'bag is empty'

    @property
    def lets_see_bag(self):
        print(self.__keg)