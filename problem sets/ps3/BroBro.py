# -*- coding: utf-8 -*-
"""
Created on Sun May 24 16:00:52 2020

@author: egultekin
"""


import math
import string
import random

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 7
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    
    print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print("  ", len(wordlist), "words loaded.")
    return wordlist


class ScrabbleGame(object):
    def __init__(self, handSize, letterValues):
        ''' Initiates a Scrabble Game object,
        handSize : the number of letters a player receives at the start of every hand
        letterValues : a dict that has letters and their respective values as key:value pairs
        validWords : the list of valid words that players can use
        hand : a dict that represents the current hand of the player
        word : the word that the user plays'''
        
        self.handSize = handSize
        self.letterValues = letterValues
        self.validWords = load_words()
        self.hand = {}
        self.word = ''
        
    def getHandSize(self):
        ''' Getter method for self.handSize'''
        return self.handSize
    
    def getLetterValues(self):
        ''' Getter method for self.letterValues'''
        return self.letterValues
    
    def getValidWords(self):
        ''' Getter method for self.validWords'''
        return self.validWords
    
    def setHandSize(self, newHandSize):
        ''' Setter method for self.handSize'''
        self.handSize = newHandSize
        
    def setLetterValues(self, letterToBeChanged, newLetterValue):
        ''' Setter method for self.letterValues'''
        self.letterValues[letterToBeChanged] = newLetterValue
        
    def addValidWord(self, newValidWord):
        ''' Method for adding a new word to the list of valid words,
        updates self.validWords'''
        self.validWords.append(newValidWord)
        
    def calcWordScore(self):
        """
        Returns the score for a word. Assumes the word is a
        valid word.
    
        You may assume that the input word is always either a string of letters, 
        or the empty string "". You may not assume that the string will only contain 
        lowercase letters, so you will have to handle uppercase and mixed case strings 
        appropriately. 
    
    	The score for a word is the product of two components:
    
    	The first component is the sum of the points for letters in the word.
    	The second component is the larger of:
                1, or
                7*wordlen - 3*(n-wordlen), where wordlen is the length of the word
                and n is the hand length when the word was played
    
    	Letters are scored as in Scrabble; A is worth 1, B is
    	worth 3, C is worth 3, D is worth 2, E is worth 1, and so on.
    
        returns: int >= 0
        """
        # make parameter "word" all lowercase because scrabble letter values dict has all letters in lowercase
        lowercaseWord = self.word.lower()
        firstSum = 0
        n = ScrabbleGame.calcHandLength(self)
        secondSum = 7 * len(self.word) - 3 * (n - len(self.word))
        if len(self.word) > 0:
        ### calculate the first component of word score --> sum of the points for letters in the word
            for letter in lowercaseWord:
                if letter != '*':
                    firstSum += self.letterValues[letter]
                else:
                    pass
        ### recalculate the second component of word score in case the sum is lower than 1
            if secondSum < 1:
                secondSum = 1
        else:
            return 0       
        return firstSum * secondSum
        
    def dealHand(self):
        """
        Returns a random hand containing self.handSize lowercase letters.
        ceil(self.handSize/3) letters in the hand should be VOWELS (note,
        ceil(self.handSize/3) means the smallest integer not less than self.handSize/3).
    
        Hands are represented as dictionaries. The keys are letters and the values are the number of times the
        particular letter is repeated in that hand.
    
        returns: dictionary (string -> int)"""
        
        num_vowels = int(math.ceil(self.handSize / 3)) - 1
    
        for i in range(num_vowels):
            x = random.choice(VOWELS)
            self.hand[x] = self.hand.get(x, 0) + 1
    
        for i in range(num_vowels, self.handSize-1):    
            x = random.choice(CONSONANTS)
            self.hand[x] = self.hand.get(x, 0) + 1
    
        self.hand['*'] = 1
    
        return self.hand
    
    def isValidWord(self):
        """
        Returns True if word is in the word_list and is entirely
        composed of letters in the hand. Otherwise, returns False.
        Does not mutate hand or word_list.
       
        returns: boolean"""
        
        copiedHand = self.hand.copy()
        correctLetters = 0
        lowercaseWord = self.word.lower()
        for letter in lowercaseWord:
            if letter in copiedHand.keys() and copiedHand[letter] > 0:
                correctLetters += 1
                copiedHand[letter] -= 1
        if correctLetters == len(self.word):
            if lowercaseWord in self.validWords:
                return True
            elif '*' in lowercaseWord:
                letters = []
                index = lowercaseWord.find('*')
                possibleWords = []
                for letter in lowercaseWord:
                    letters.append(letter)
                for vowel in VOWELS:
                    letters[index] = vowel
                    possWord = ''.join(letters)
                    possibleWords.append(possWord)
                confirmation = False
                for word in possibleWords:
                    if word in self.validWords:
                        confirmation = True
                if confirmation:
                    return True
                else:
                    return False
            else:
                return False
            
    def calcHandLength(self):
        """ 
        Returns the length (number of letters) in the current hand.
        
        returns: integer
        """
        
        lengthOfHand = 0
        for value in self.hand.values():
            lengthOfHand += value
        return lengthOfHand
    
    def updateHand(self):
        """
        Does NOT assume that hand contains every letter in word at least as
        many times as the letter appears in word. Letters in word that don't
        appear in hand should be ignored. Letters that appear in word more times
        than in hand should never result in a negative count; instead, set the
        count in the returned hand to 0 (or remove the letter from the
        dictionary, depending on how your code is structured). 
    
        Updates the hand: uses up the letters in the given word
        and returns the new hand, without those letters in it.
    
        Has no side effects: does not modify hand.
       
        returns: dictionary (string -> int)
        """
    
        newHand = self.hand.copy()
        for letter in self.word.lower():
            if letter in newHand.keys():
                if newHand[letter] > 0:
                    newHand[letter] -= 1
        return newHand
    
    def displayHand(self):
        """ Method for displaying the letters currently in the hand."""
        
        for letter in self.hand.keys():
            for j in range(self.hand[letter]):
                print(letter, end=' ')

    def playHand(self):
        """
        Allows the user to play the given hand, as follows:

        * The hand is displayed.
        
        * The user may input a word.
    
        * When any word is entered (valid or invalid), it uses up letters
          from the hand.
    
        * An invalid word is rejected, and a message is displayed asking
          the user to choose another word.
    
        * After every valid word: the score for that word is displayed,
          the remaining letters in the hand are displayed, and the user
          is asked to input another word.
    
        * The sum of the word scores is displayed when the hand finishes.
    
        * The hand finishes when there are no more unused letters.
          The user can also finish playing the hand by inputing two 
          exclamation points (the string '!!') instead of a word.
    
          returns: the total score for the hand"""
         
        # As long as there are still letters left in the hand:
        lettersLeft = ScrabbleGame.calcHandLength(self)
        # track total score
        totalScore = 0
        while lettersLeft > 0:
            # Display the hand
            print('Current hand: ', end = '')
            ScrabbleGame.displayHand(self)
            # Ask user for input
            self.word = input('Enter word, or "!!" to indicate that you are finished: ')
            # If the input is two exclamation points:
            if self.word == '!!':
                # End the game (break out of the loop)
                break
                
            # Otherwise (the input is not two exclamation points):
            else:
                # If the word is valid:
                if ScrabbleGame.isValidWord(self):
                    # Tell the user how many points the word earned,
                    # and the updated total score
                    wordScore = ScrabbleGame.calcWordScore(self)
                    print('"'+ self.word + '"' + ' earned ' + str(wordScore) + ' points.', end = '')
                    totalScore += wordScore
                    print(' Total: ' + str(totalScore) + ' points')
                    print()
                # Otherwise (the word is not valid):
                else:
                    # Reject invalid word (print a message)
                    print('That is not a valid word. Please choose another word.')
                    print()
                # update the user's hand by removing the letters of their inputted word
                self.hand = ScrabbleGame.updateHand(self)
                lettersLeft = ScrabbleGame.calcHandLength(self)
    
        # Game is over (user entered '!!' or ran out of letters)
        self.hand = {}
        if lettersLeft == 0:
        # so tell user the total score
            print('Ran out of letters. Total score for this hand: ' + str(totalScore))
            print('-----------')
        else:
            print('Total score for this hand: ' + str(totalScore))
            print('-----------')
        # Return the total score as result of function
        return totalScore
    
    def substituteHand(self, letter):
        """ 
        Allow the user to replace all copies of one letter in the hand (chosen by user)
        with a new letter chosen from the VOWELS and CONSONANTS at random. The new letter
        should be different from user's choice, and should not be any of the letters
        already in the hand.
    
        If user provide a letter not in the hand, the hand should be the same.
    
        Has no side effects: does not mutate hand.
    
        For example:
            substitute_hand({'h':1, 'e':1, 'l':2, 'o':1}, 'l')
        might return:
            {'h':1, 'e':1, 'o':1, 'x':2} -> if the new letter is 'x'
        The new letter should not be 'h', 'e', 'l', or 'o' since those letters were
        already in the hand.
        
        letter: string
        returns: dictionary (string -> int)
        """
        # make a copy of the hand
        copiedHand = self.hand.copy()
        # if the letter is actually in the hand dealt to the user
        if letter.lower() in copiedHand.keys():
            # note the value of the to-be-deleted letter
            value = copiedHand.get(letter.lower())
            # delete it from the copied hand
            del copiedHand[letter.lower()]
            # create a set of letters that doesn't include the letters already in the hand
            alphabet = VOWELS + CONSONANTS
            letters = copiedHand.keys()
            lettersStr = ''.join(letters)
            setOfLetters = []
            for letter in alphabet:
                if letter not in lettersStr:
                    setOfLetters.append(letter)
            setOfLetters.remove(letter)
            lettersLeft = ''.join(setOfLetters)
            # select a random letter
            newLetter = random.choice(lettersLeft)
            # add the new letter
            copiedHand[newLetter] = value
        # return the copy of the hand
        return copiedHand
          
    def handleSubstitution(self, subsLeft):
        ''' Handles the substitution process,
        updates subsLeft and returns it with current hand'''
        
        if subsLeft:
            # Display the hand
            print('Current hand: ', end = '')
            ScrabbleGame.displayHand(self)
            # ask if the user wants to substitute a letter in the hand
            substitution = input('Would you like to substitute a letter? ')
            # if the user says yes
            if substitution.lower() == 'yes':
                # reduce subs left
                subsLeft = False
                # ask which letter the user wants to substitute
                letterToBeChanged = input('Which letter would you like to replace: ')
                # switch that letter with a random one and update the hand
                substitutedHand = ScrabbleGame.substituteHand(self, letterToBeChanged)
                return subsLeft, substitutedHand
        return subsLeft, self.hand
    
    def replayHand(self, replaysLeft, totalNumOfHands, totalScore, hand):
        ''' Handles the replay process after a hand is finished,
        updates replaysLeft and returns it with number of hands left to play and total score'''
        # decrease numb of hands
        totalNumOfHands -= 1
        if replaysLeft:
            # ask if the user wants to replay that round
            replay = input('Would you like to replay the hand: ')
            if replay.lower() == 'no':
                return totalScore, replaysLeft, totalNumOfHands
            elif replay.lower() == 'yes':
                # make the user play that hand again
                self.hand = hand
                replayedRoundScore = ScrabbleGame.playHand(self)
                # decrease the number of replay by one
                replaysLeft = False
                return totalScore if totalScore > replayedRoundScore else replayedRoundScore, replaysLeft, totalNumOfHands
        else:
            return totalScore, replaysLeft, totalNumOfHands
    
    def playGame(self):
        """
        Allow the user to play a series of hands
    
        * Asks the user to input a total number of hands
    
        * Accumulates the score for each hand into a total score for the 
          entire series
     
        * For each hand, before playing, ask the user if they want to substitute
          one letter for another. If the user inputs 'yes', prompt them for their
          desired letter. This can only be done once during the game. Once the
          substitue option is used, the user should not be asked if they want to
          substitute letters in the future.
    
        * For each hand, ask the user if they would like to replay the hand.
          If the user inputs 'yes', they will replay the hand and keep 
          the better of the two scores for that hand.  This can only be done once 
          during the game. Once the replay option is used, the user should not
          be asked if they want to replay future hands. Replaying the hand does
          not count as one of the total number of hands the user initially
          wanted to play.
    
                * Note: if you replay a hand, you do not get the option to substitute
                        a letter - you must play whatever hand you just had.
          
        * Returns the total score for the series of hands"""
        
        # ask the user to input a total number of hands
        totalNumOfHands = int(input('Enter total number of hands: '))
        # track the substitution right of the user
        subsLeft = True
        # track replay rights of the user
        replaysLeft = True
        # track total score over all hands
        totalScore = 0
        # continue a loop where the user's number of hands is bigger than 0
        while totalNumOfHands > 0:
            # give the user a random hand
            initialHand = ScrabbleGame.dealHand(self)
            subsLeft, self.hand = ScrabbleGame.handleSubstitution(self, subsLeft)
            roundScore = ScrabbleGame.playHand(self)
            roundScore, replaysLeft, totalNumOfHands = ScrabbleGame.replayHand(self, replaysLeft, totalNumOfHands, roundScore, initialHand)
            totalScore += roundScore
        print('Total score over all hands: ' + str(totalScore))
        return totalScore
    
    
a = ScrabbleGame(HAND_SIZE, SCRABBLE_LETTER_VALUES)
a.playGame()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    