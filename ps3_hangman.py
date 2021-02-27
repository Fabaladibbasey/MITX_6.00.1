# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "/home/suspect-0/.config/spyder-py3/words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE...
    
    for letterInSecretWord in secretWord:
        if(not letterInSecretWord in lettersGuessed):
            return False
    return True



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE...
    
    word = ''
    for letterInSecretWord in secretWord:
        if(not letterInSecretWord in lettersGuessed):
           word += '_ '
        else:
            word += letterInSecretWord
    return word



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    alphabetList = list(string.ascii_lowercase)
    for letterInletterGuessed in lettersGuessed:
        if letterInletterGuessed in alphabetList:
            alphabetList.remove(letterInletterGuessed)
    return "".join(alphabetList)
    
    

def guess_status(secretWord, letter):
    if letter in secretWord:
        return True
    else:
        return False
    
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE...
    print("Welcome to the game Hangman!\nI am thinking of a word that is", len(secretWord))
    numberGuess = 8
    lettersGuessedList = []
    availableLetters = getAvailableLetters([])
    words_so_far = ''
    while numberGuess > 0:
        print("------------")
        print('You have', numberGuess, 'guesses left.')
        print("Available letters:", availableLetters)
        inputLetter = input("Please guess a letter: ")
        inputLetter = inputLetter.lower()
        lettersGuessedList.append(inputLetter)
        words_so_far = getGuessedWord(secretWord, lettersGuessedList)
        guessedStatus = guess_status(secretWord, inputLetter)
        if not inputLetter in availableLetters:
            print("Oops! You've already guessed that letter:", words_so_far)
        elif guessedStatus:
            print('Good guess:', words_so_far)
            
        else:
            print('Oops! That letter is not in my word:', words_so_far)
            numberGuess -= 1
	
        wordGuessedCorrectly = isWordGuessed(secretWord, lettersGuessedList)
        if wordGuessedCorrectly:
            print("------------")
            return "Congratulations, you won!"
        availableLetters = getAvailableLetters(lettersGuessedList)
    
    print("------------")
    return "Sorry, you ran out of guesses. The word was " + secretWord + "."

# word = 'apple'
# print(hangman(word))

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

secretWord = chooseWord(wordlist).lower()
print(hangman(secretWord))