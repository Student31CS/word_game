# Word Game
# Name: Tyler Vickers
#  
#

from distutils.ccompiler import new_compiler
from optparse import check_builtin
import random
import string
import time

VOWELS = 'AEIOU'
CONSONANTS = 'BCDFGHJKLMNPQRSTVWXYZ'
HAND_SIZE = 7
WORDLIST_FILENAME = "words.txt"
players = []


class Player:
    def __init__(self, name, score=0, win=False):
        self.name = str(name)
        self.hand = deal_hand(HAND_SIZE)
        self.score = score
        self.win = win
        self.answer = ''
    
    def __str__(self):
        # printing instances of the class will result in 
        # the name they have chosen
        return self.name

    def make_answer(self):
        # Method for making an answer for the user
        self.answer = input('Make the best word you can:').upper()

    def check_win(self):
        '''
        First player to reach a score of 100 wins
        This method checks the score'''
        if self.score >= 100:
            self.win = True
        else:
            self.win = False


    def add_score(self):
        '''
        * Prints hand to the user

        * Runs the check_answer function (Boolean)

        * There is an option for deduction in case 
          there are no words in the hand, or if the 
          hand is difficult to solve
          
        * Prints new score on the screen'''
        print_hand(self.hand)
        tally = 0
        if check_answer(self, self.hand, word_list, 1) == True:
            for x in self.answer:
                if x in VOWELS:
                    tally += 3
                if x in CONSONANTS:
                    tally += 2
        else:
            tally -= 5

        self.score += tally

        print('\n\n\n\n\n===============================')
        print(f'Player: {self.name}')
        print(f'SCORE: {self.score}')
        print('===============================\n\n\n')
        time.sleep(2)
        # Deal a new hand
        self.hand = deal_hand(HAND_SIZE)


        



# Create each players' class


        
def make_players():
    '''
    Ask User how many players are playing.

    Store number in a variable to be used in a function, make_players(), for 
    creating each Player's class

    While loop checks if user input is valid. Only 1 - 4 Players
    '''
    x = 0
    while not(x >= 1 and x <= 4):
        try:
            x = int(input('Please enter the amount of players (1-4)'))
        except:
            print('There was an error. Try again.')

    '''
    Creates instances in Player class
    
    Loop iterates to instanciate each class

    Their name will be stored as an attribute
    '''
        
    for x in range(x):
        name = input(f'Player {x+1}, what is your name?:')
        players.append(Player(name))



# Words, hands, and word checks



def load_words():
    """
    Returns a list of valid words. a word is a string of lowercase letters.
    
    """
    print ("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print ("  ", len(wordlist), "words loaded.")
    return wordlist



def deal_hand(n):
    """
    Returns a random hand containing n lowercase letters with 3 VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    num_vowels = 3
    
    for i in range(num_vowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(num_vowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand



def print_hand(hand):
    '''
    Function for printing the hand to the screen for easy readability

    Add white space so each letter can be read clearly
    '''
    hand_list = []
    print('\n\n\n\n\nHere is your hand:\n')
    for x in hand:
        for i in range(hand.get(x)):
            print(x, '  ', end='')
    print('\n\n\n')



def check_answer(player, hand, word_list, counter):
    '''
    1) Checks for cheating by ensuring all characters exist in the player's hand
    
    2) Check the word list for validity
    
    3) Returns boolean for add score function
    '''
    
    # Checks if word is in the player's hand
    check = False
    while check == False:
        player.make_answer()
        answer = player.answer
        for i in answer:
            if i in hand:
                check = True
            else:
                print('\n\n\n\n\nThere was something wrong. Your word did not match your hand.\n\n')
                time.sleep(2)
                print_hand(hand)
                check = False
                break
        

    # Checks if word exists in word_list
    counter = counter

    if answer.lower() in word_list:
        return True
    else:
        if counter > 3:
            print('\n\n\n\n\nYou had too many attempts. 5 points will be deducted from your score.')
            return False
        else: 
            counter += 1
            print('\n\n\n\n\nThat answer was not in our dictionary. Try again\n\n\n')
            time.sleep(2)
            print_hand(hand)
            check = True
            return check_answer(player, hand, word_list, counter)

            
    
    



        


def play_hand(player, word_list):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    
    * The user may input a word.

    * An invalid word is rejected, and a message is displayed asking
      the user to choose another word.

    * When a valid word is entered, calculate the score and display the score

      hand: dictionary (string -> int)
      word_list: list of lowercase strings
    """
    # TO DO ...

    

    print('\n\n\n\n\n===============================')
    print(f'Player: {player.name}')
    print(f'SCORE: {player.score}')
    print('===============================\n\n\n')

    time.sleep(2)
    
    #Ask user to make a hand, then check hand and word list
    player.add_score()





if __name__ == '__main__':


    word_list = load_words()
    


    make_players()

    for player in players:
        play_hand(player, word_list)
        if player.check_win() == True:
            print(f'\n\n\n\n\n{player.name} WINS!!!!!\n\n\n').upper()
            time.sleep(3)
            break
   
    