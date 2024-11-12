
# LOTTO

## Game Rules (English)

The game is played using special cards with marked numbers and chips (barrels) with numbers on them.

- Total number of barrels: 90 (with numbers from 1 to 90).
- Each card contains 3 rows with 9 cells each. Each row has 5 random numbers, and all numbers on the card are unique.

### Example of a Card
````
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
````


### Gameplay

The game consists of 2 players: the user and the computer. Each player receives a random card at the beginning.

1. A random barrel is drawn each turn, and its number is displayed on the screen along with each player's card.
2. The user is prompted to either mark the number on their card or continue without marking.

#### User Options:

- If the user chooses to **mark**:
  - If the number is on their card, it is marked off, and the game continues.
  - If the number is not on their card, the user loses, and the game ends.
  
- If the user chooses to **continue**:
  - If the number is on their card, the user loses, and the game ends.
  - If the number is not on their card, the game continues.

The winner is the first player to mark off all numbers on their card.

### Example of a Game Turn
````

New number: 70 (76 nums left)
------ User's card -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Computer's car ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Mark the number? (y/n)


---
````

## Правила игры (Русский)

Игра ведется с помощью специальных карточек, на которых отмечены числа, и фишек (бочонков) с цифрами.

- Количество бочонков: 90 (с цифрами от 1 до 90).
- Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, все числа на карточке уникальны.

### Пример карточки
````
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
````

### Ход игры

В игре участвуют 2 игрока: пользователь и компьютер. В начале каждому выдается случайная карточка.

1. Каждый ход выбирается один случайный бочонок и выводится на экран вместе с карточками игроков.
2. Пользователю предлагается либо зачеркнуть цифру на своей карточке, либо продолжить без зачеркивания.

#### Действия пользователя:

- Если игрок выбирает **зачеркнуть**:
  - Если цифра есть на карточке, она зачеркивается, и игра продолжается.
  - Если цифры на карточке нет, игрок проигрывает, и игра завершается.
  
- Если игрок выбирает **продолжить**:
  - Если цифра есть на карточке, игрок проигрывает, и игра завершается.
  - Если цифры на карточке нет, игра продолжается.

Побеждает тот, кто первым зачеркнет все числа на своей карточке.

### Пример одного хода

````

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11
      16 49    55 88    77
   15 20     -       76  -
--------------------------
Mark the number? (y/n)


---
````

