import random
import os
from quotes import lose,win
from hangman_art import logo,stages
from words import words



def screen_clear():
   if os.name == 'posix':
      _ = os.system('clear')
   else:
      _ = os.system('cls')


def random_word():
    return random.choice(words)
    
def show_word_l(word_l):
    print(' ', end=' ')
    for i in word_l:
        print(i, end=' ')


def guess_char(word_l, ch, word):
    if ch in word:
        for i in range(len(word)):
            if word[i] == ch:
                word_l[i] = ch
        return True
    
    
    return False


def check_win(word_l,word):
    if not '_' in word_l:
        screen_clear()
        print(logo[0])
        print(f' Correct word is {word}\n')
        print(' '+random.choice(win)+'\n')
        return True
    return False
        
def check_lose(lives, word):
    if lives == 1:
        screen_clear()
        print(logo[0])
        print(stages[0])
        print(f' Correct word is: {word}\n')
        print(' '+random.choice(lose)+'\n')
        return True
    
    return False

def play_again():
    play = input(' Do you want to play again? y/n   ').lower()
    if play == 'n':
        return False
    
    return True


