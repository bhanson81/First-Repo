# Hangman
import random

WORDLIST_FILE = "validwords.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILE, 'r')
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

# -----------------------------------
wordlist = loadWords()

def isWordGuessed(secretWord, letters_gussed):
    '''
    secretWord: string, the word the user is guessing
    letters_gussed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in letters_gussed;
      False otherwise
    '''
    c=0
    for i in letters_gussed:
        if i in secretWord:
            c+=1
    if c==len(secretWord):
        return True
    else:
        return False


def getGuessedWord(secretWord, letters_gussed):
    '''
    secretWord: string, the word the user is guessing
    letters_gussed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    s=[]
    for i in secretWord:
        if i in letters_gussed:
            s.append(i)
    ans=''
    for i in secretWord:
        if i in s:
            ans+=i
        else:
            ans+='_ '
    return ans



def getAvailableLetters(letters_gussed):
    '''
    letters_gussed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    import string
    ans=list(string.ascii_lowercase)
    for i in letters_gussed:
        ans.remove(i)
    return ''.join(ans)

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
    print("Welcome to the game, Hangman!")
    print("I am thinking of a word that is",len(secretWord),"letters long.")
    
    global letters_gussed
    mistakeMade=0
    letters_gussed=[]
    
    while 8 - mistakeMade > 0:
        
        if isWordGuessed(secretWord, letters_gussed):
            print("-------------")
            print("Congratulations, you won!")
            break
            
        else:
            print("-------------")
            print("You have",8-mistakeMade,"guesses left.")
            print("Available letters:",getAvailableLetters(letters_gussed))
            guess=str(input("Please guess a letter: ")).lower()
            
            if guess in letters_gussed:
                print("You've already guessed that letter:",getGuessedWord(secretWord,letters_gussed))
                
            elif guess in secretWord and guess not in letters_gussed:
                letters_gussed.append(guess)
                print("Good guess:",getGuessedWord(secretWord,letters_gussed))
                
            else:
                letters_gussed.append(guess)
                mistakeMade += 1
                print("Oops! That letter is not in my word:",getGuessedWord(secretWord,letters_gussed))
                
        if 8 - mistakeMade == 0:
            print("-------------")
            print("Sorry, you ran out of guesses. The word was else.",secretWord)
            break
        
        else:
            continue


secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
