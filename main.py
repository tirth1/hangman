import random
from hangman_art import logo,stages

from hangman import random_word,guess_char,screen_clear,show_word_l,check_win,check_lose,play_again


def main():
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
            print(logo[0])
            print(stages[lives])
            show_word_l(word_l)
            print("\n\n Misses: ", end='')
            show_word_l(misses)
            ch = input("\n\n Select character: ").lower()
        
            if guess_char(word_l, ch, word)==False:
                misses += ch
                if check_lose(lives, word) == True:
                    if play_again() == False:
                        game_on = False
                    break
                lives -= 1

            else: 
                if check_win(word_l,word) == True:
                    if play_again() == False:
                        game_on = False
                    break
                
                    
            


if __name__ == '__main__':
    main()