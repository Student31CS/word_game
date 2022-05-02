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
winner = False


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
        if self.score >= 50:
            self.win = True
        else:
            self.win = False
        return self.win


    def play_hand(self):
        '''
            Allows the user to play the given hand, as follows:

        * The hand is displayed.
        
        * The user may input a word.

        * Runs the check_answer function (Boolean)

        * An invalid word is rejected, and a message is displayed asking
        the user to choose another word.

        * When a valid word is entered, calculate the score and display the score

        hand: dictionary (string -> int)
        word_list: list of lowercase strings

        * There is an option for deduction in case 
          there are no words in the hand, or if the 
          hand is difficult to solve
          
        * Prints new score on the screen
        '''

        print('\n\n\n\n\n===============================')
        print(f'Player: {self.name}')
        print(f'SCORE: {self.score}')
        print('===============================\n\n\n')

        time.sleep(2)

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
    * Checks for cheating by ensuring all characters exist in the player's hand
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
        

    '''
    * Check the word list for validity 
    
    * Returns boolean for use in the Player class .play_hand method'''
    counter = counter

    if answer.lower() in word_list:
        return True
    else:
        if counter > 3:
            print('\n\n\n\n\nYou had too many attempts. 5 points will be deducted from your score.')
            time.sleep(2)
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
    player.play_hand()

def play_game(winner, players):
    '''
    Prints a series of text to briefly explain the rules
    
    While loop plays through each instance of Player, until
    a player has reached a score of 50.'''

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n===============================')
    print('WELCOME TO TYLER\'S WORDGAME')
    print('===============================\n\n\n')
    input('Press Enter')

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nThis is a 1 - 4 Player Game')
    print('\nThe game ends once a player reaches a score of 50')
    input('\n\n\nPress Enter')

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nEach player will be dealt 3 Vowels and 4 Consonants.')
    print('\nMake the best word you can to get the highest score')
    print('\nVowels are worth 3 points and Consonants are worth 2 points')
    input('\n\nPress Enter when you are ready to play')

    make_players()

    while winner == False:
        for player in players:
            player.play_hand()
            winner = player.check_win()
            if winner == True:
                time.sleep(2)
                print(f'{player} WINS!!!\n\n\n')
                break
            

if __name__ == '__main__':
    word_list = load_words()
    play_game(winner, players)
            