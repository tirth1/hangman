import random
import os

words = ['cow', 'boy', 'charusat']

stages = ['''
 +---+
 |   |
 0   |
/|\  |
/ \  |
     |
--------
--------

''','''
 +---+
 |   |
 0   |
/|\  |
/    |
     |
--------
--------

''','''
 +---+
 |   |
 0   |
/|\  |
     |
     |
--------
--------

''','''
 +---+
 |   |
 0   |
/|   |
     |
     |
--------
--------

''','''
 +---+
 |   |
 0   |
 |   |
     |
     |
--------
--------

''','''
 +---+
 |   |
 0   |
     |
     |
     |
--------
--------

''','''
 +---+
 |   |
     |
     |
     |
     |
--------
--------

''',]

def screen_clear():
   # for mac and linux(here, os.name is 'posix')
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      # for windows platfrom
      _ = os.system('cls')


def random_word():
    return random.choice(words)
    
def show_word_l(word_l):
    for i in word_l:
        print(i, end=' ')


def guess_char(word_l, ch):
    if ch in word:
        for i in range(len(word)):
            if word[i] == ch:
                word_l[i] = ch
        return True
    
    
    return False


game_on = True
while game_on:
    word = random_word()
    lives = 6
    word_l = []
    misses = []
    

    for i in range(len(word)):
        word_l += '_'

    for i in range(int(len(word)/3)):
        n = random.randint(0, len(word)-1)
        word_l[n] = word[n]
    
    while lives>0 or '_' in word_l:
        screen_clear()
        
        print(stages[lives])
        show_word_l(word_l)
        print("\n\nMisses: ", end='')
        show_word_l(misses)
        ch = input("\n\nSelect character: ").lower()
       
        if guess_char(word_l, ch)==False:
            misses += ch
            print(stages[lives])
            lives -= 1
            if lives == 0:
                screen_clear()
                print(stages[lives])
                print(f'Correct word is: {word}\n')
                play = input("You Lose !... Do you want to play again? y/n   ").lower()
                if play == 'n':
                    game_on = False
                    break
                else:
                    break
            
        if not '_' in word_l:
            print(f'Correct word is {word}')
            print('Yupp! You win!')
            play = input('Do you want to play again? y/n   ').lower()
            if play == 'n':
                game_on = False
                break
            else:
                break