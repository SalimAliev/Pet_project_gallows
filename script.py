from random import choice

# Получение списка слов
with open('words.txt', 'r', encoding='UTF-8') as file:
    words = file.read().split()

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


print('V1')
print('Приветствую тебя игрок')
user_name = input('Введи свое имя:').strip()

while len(user_name) > 10:
    user_name = input('Введено слишком длинное имя игрока, введите пожалуйста имя длиной не более 10 символов:')

if len(user_name) == 0:
    user_name = 'Анонимус'

print('Правила игры:\n'
      f'В игре загадано слово, игроку необходимо его угадать. Игрок должен укадывать буквы из загаданного слова. '
      f'При каждой невенерной букве на виселице рисуется деталь приближающая к проигрышу. У игрока есть {len(HANGMAN)} '
      f'неверных попыток.')


while True:
    game_status = input('Готовы начать игру (да/нет):').strip()

    if game_status.lower() == 'да':
        random_word = list(choice(words))
        wrong_count = 0
        max_wrong = len(HANGMAN) - 1
        hidden_word = ['-']*len(random_word)
        entered_letter = []

        while True:

            if wrong_count == max_wrong:
                print(f'К созажалению {user_name} вы проиграли, угадываемое словов {"".join(random_word)}')
                break

            elif random_word == hidden_word:
                print(f'Поздравляю {user_name} вы выиграли')
                break

            print(f'{HANGMAN[wrong_count]}\n'
                  f'Слово: {"".join(hidden_word)}\n'
                  f'Ошибок: {wrong_count}\n'
                  f'Названные буквы: {", ".join(entered_letter)}\n')
            letter = input('Введи букву: ').strip()

            if len(letter) > 1 or not letter.isalpha():
                print('Необоходимо ввести один символ авлофита')
                continue

            if letter.lower() in entered_letter:
                print('Вы уже вводили эту букву')
                continue

            entered_letter.append(letter)
            wrong_flag = False

            for index, char in enumerate(random_word):

                if char == letter.lower():
                    hidden_word[index] = letter
                    wrong_flag = True

            if not wrong_flag:
                wrong_count += 1

    elif game_status == 'нет':
        print('Завершение игры')
        break

    else:
        print('Введите да или нет')



