
import sys
import random
from collections import OrderedDict


def choose_difficulty():
    difficulty = input('Choose a difficulty level: 1 (Easy), 2 (Hard) ')
    lives = 0
    if difficulty == '1':
        lives = 8
    elif difficulty == '2':
        lives = 6
    elif difficulty != '1' and difficulty != '2':
        print('Wrong input, the options are right there')
        choose_difficulty()
    return lives


def choose_random_word(filename):
    f = open(filename, "r")
    file_content = f.readlines()
    f.close() 
    chosen_line = random.choice(file_content)
    chosen_word = chosen_line.split("|")[1]
    return chosen_word.upper().strip()


def print_unguessed_word(guessed_letters, word):
    for y in word:
        if y not in guessed_letters:
            print('_', end=' ')
        else:
            print(y, end=' ')
    print('\n')
               

def get_letter():
    letter = input("Please insert letter:").upper()
    if letter.isalpha():
        return letter
    else:
        print("Invalid input")
        get_letter()


def is_the_letter_word_quit(letter):
    if letter == 'quit'.upper():
        return True


def is_letter_already_tried(letter, guessed_letters):
    if len(letter) == 1 and letter.isalpha():
        if letter in guessed_letters:
            return True
        else:
            return False 


def is_letter_part_of_word(letter, word):
    flag = 0
    for y in word:
        if letter == y:
            flag = 1
            return True
    if flag == 0:
        return False      
    

def display_hangman(lives):
    stages = [
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
               
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
               
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
               
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
               
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """]
    return stages[lives]


def is_game_lost(lives):
    if lives == 0:
        return True
    else:
        return False 


def is_game_won(guess_word, word):
    for letter in word:
        if letter not in guess_word:
            return False
    return True


def play(word, lives):
    guessed_letters = []
    print_unguessed_word(guessed_letters, word)
    
    word_1 = ''
    res = list(OrderedDict.fromkeys(word))
    while((sorted(guessed_letters) is not sorted(res)) or lives > 0):
      
        letter = get_letter()
        if is_the_letter_word_quit(letter):
            sys.exit(0)
        elif is_letter_already_tried(letter, guessed_letters):
            print("letter already tried" + letter)
        elif is_letter_part_of_word(letter, word):
            guessed_letters.append(letter)
            print_unguessed_word(guessed_letters, word)
        else:
            guessed_letters.append(letter)
            lives -= 1
            if lives > 6:
                print('You have '+str(lives)+' tries left')
            else:
                print(display_hangman(lives))
        if is_game_lost(lives):
            print('Game Over')  
            break
        elif is_game_won(word_1.join(guessed_letters), word):
            print('You win')
            break


if __name__ == "__main__":
    guessed_letters = []
    lives = choose_difficulty()
    word = choose_random_word("countries-and-capitals.txt")
    play(word, lives)
