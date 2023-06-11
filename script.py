from random import choice

# Список слов для игры
words = ['машина', 'самолет', 'велосипед']

HANGMAN = (
    """
     ------
     |    |
     |
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |
     |
     |
     |
    ----------
    """,
    """
     ------
     |    |
     |    O
     |    |
     | 
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |   
     |   
     |   
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   
     |   
     |     
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   /
     |   
     |    
    ----------
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |   
     |   
    ----------
    """
)



print('Приветствую тебя игрок')
user_name = input('Введи свое имя:')

while len(user_name) > 10:
    user_name = input('Введено слишком длинное имя игрока, введите пожалуйста имя длиной не более 10 символов:')

if len(user_name) == 0:
    user_name = 'Анонимус'

print('Правила игры:\n'
      f'В игре загадано слово, игроку необходимо его угадать. Игрок должен укадывать буквы из загаданного слова. '
      f'При каждой невенерной букве на виселице рисуется деталь приближающая к проигрышу. У игрока есть {max_wrong} '
      f'неверных попыток.')


while True:
    game_status = input('Готовы начать игру (да/нет):')

    if game_status == 'да':
        random_word = list(choice(words))
        wrong_count = 0
        max_wrong = len(HANGMAN) - 1
        hidden_word = ['-']*len(random_word)
        entered_letter = []

        while wrong_count < max_wrong:

            if wrong_count == max_wrong:
                print(f'К созажалению {user_name} вы проиграли')
                break

            elif random_word == hidden_word:
                print(f'Поздравляю {user_name} вы выиграли')
                break

            print(f'{HANGMAN[wrong_count]}\n'
                  f'Слово: {"".join(hidden_word)}\n'
                  f'Ошибок: {wrong_count}\n'
                  f'Названные буквы: {", ".join(entered_letter)}')
            letter = input('Введи букву: ')

            if len(letter) > 1 and letter.isalnum():
                print('Необоходимо ввести один символ авлофита')
                continue

            entered_letter.append(letter)
            wrong_flag = False

            for index, char in enumerate(random_word):

                if char == letter.lower():
                    hidden_word[index] = letter
                    wrong_flag = True

            if wrong_flag == False:
                wrong_count += 1

    elif game_status == 'нет':
        print('Завершение игры')
        break

    else:
        print('Введите да или нет')



