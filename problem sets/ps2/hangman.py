# Problem Set 2, hangman.py
# Name: 
# Collaborators:
# Time spent:

# Hangman Game
# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)
import random
import string

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
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code

# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing; assumes all letters are
      lowercase
    letters_guessed: list (of letters), which letters have been guessed so far;
      assumes that all letters are lowercase
    returns: boolean, True if all the letters of secret_word are in letters_guessed;
      False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    len_secret_word = len(secret_word)
    true_letter_counter = 0
    for letter in secret_word:
        if letter in letters_guessed:
            true_letter_counter += 1
    if true_letter_counter == len_secret_word:
        return True
    else:
        return False

# secret_word = 'apple'
# letters_guessed = ['e', 'l', 'a', 'p', 'r', 's']
# print(is_word_guessed(secret_word, letters_guessed))

def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    correct_guessed_letters = []
    for i in range(0, len(secret_word)):
        for j in range(0, len(letters_guessed)):
            if letters_guessed[j] == secret_word[i]:
                correct_guessed_letters.insert(i, letters_guessed[j])
    for j in range(0, len(secret_word)):
        if secret_word[j] not in letters_guessed:
            correct_guessed_letters.insert(j, '_ ')            
    current_sit = ''.join(correct_guessed_letters)        
    return current_sit

# secret_word = 'apple'
# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_guessed_word(secret_word, letters_guessed))   

def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    lowercase_letters = list(string.ascii_lowercase)
    for letter in letters_guessed:
        if letter in lowercase_letters:
            lowercase_letters.remove(letter)
    remaining_letters = ''.join(lowercase_letters)
    return remaining_letters
    

# letters_guessed = ['e', 'i', 'k', 'p', 'r', 's']
# print(get_available_letters(letters_guessed))
    
def seperator(guesses_left, letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: puts a dashed line seperator and prints out how many guesses left and available letters
    '''
    print('------------')
    print('You have ' + str(guesses_left) + ' guesses left.')
    print('Available letters: ' + get_available_letters(letters_guessed), end = '')
    
def check_user_guess(users_guess):
    '''
    users_guess: user input
    letters_guessed: letters that the user has guessed so far
    guesses_left: how many guesses that the user has left
    returns: if guessed letter is in secret word, prints good guess, 
    if not, prints bad guess and takes away one guess
    '''
    return users_guess in secret_word
        

def is_warning(users_guess, letters_guessed):
    if str.isalpha(users_guess) == False:
        return 1
    elif users_guess in letters_guessed:
        return 2
    else:
        return 0


def handle_warning(guesses_left, warnings_left):
    no_warnings_left = False
    if warnings_left > 0:
        warnings_left -= 1
    else:
        guesses_left -= 1
        no_warnings_left = True
    return guesses_left, warnings_left, no_warnings_left

def update_guessed_letters(users_guess, letters_guessed):
     letters_guessed.append(users_guess)
        
def handle_incorrect_guess(guesses_left, users_guess):
    vowels = 'aeiou'
    if users_guess in vowels:
        guesses_left -= 2
    else:
        guesses_left -= 1
    return guesses_left, users_guess in vowels

def end_game(guesses_left):
    if guesses_left == 0:
        print('------------')
        print('Sorry, you ran out of guesses. The word was ' + secret_word + '.')
    else:
        total_score = guesses_left * len(set(secret_word))
        print('------------')
        print('Congratulations, you won!')
        print('Your total score for this game: ' + str(total_score))
        
def print_invalid_guess_warning(warnings_left, no_warnings_left, main_sentence):
    if no_warnings_left:
        second_sentence = 'You have no warnings left so you lose one guess: '
    else:
        second_sentence = 'You have ' + str(warnings_left) + ' warning(s) left: '
    print(main_sentence, second_sentence)
    
    
    
    
    
    
def hangman2(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # users start with 6 guesses and 3 warnings
    guesses_left = 6
    warnings_left = 3
    # there are no guessed letters at the start of the game
    letters_guessed = []
    # At the start of the game, let the user know how many letters the computer's word contains and how many guesses s/he starts with. 
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')
    print('You have ' + str(warnings_left) + ' warnings left.')
    ### continue user-comp interaction until the game is over where user has 0 guesses left or have correctly guessed the word
    while is_word_guessed(secret_word, letters_guessed) == False and guesses_left > 0:
        # before each guess from the user, put a dashed line seperator, tell the user how many guesses left and available letters
        seperator(guesses_left, letters_guessed)
    ### user interactions starts
    # ask for an input from the user
        users_guess = str.lower(input('Please guess a letter: '))
    # user has to type in an alphabetic letter, if not user gets a warning and after 3 warnings, user loses a guess
    # check if user's guess is within the user input requirements, if not, give a warning
        warning_result = is_warning(users_guess, letters_guessed)
        if warning_result > 0:
            # handle warning
            guesses_left, warnings_left, no_warnings_left = handle_warning(guesses_left, warnings_left)
            if warning_result == 1:
                # guess is not in alphabet
                main_sentence = 'Oops! That is not a valid letter. '
                print_invalid_guess_warning(warnings_left, no_warnings_left, main_sentence)
            else:
                # guessed letter is already guessed
                main_sentence = 'Oops! You have already guessed that letter. '
                print_invalid_guess_warning(warnings_left, no_warnings_left, main_sentence)
        else:
            guess_result = check_user_guess(users_guess)
            update_guessed_letters(users_guess, letters_guessed)
            if guess_result:
                #handle correct guess
                print('Good guess: ')
            else:
                #handle incorrect guess
                guesses_left, is_guess_vowel = handle_incorrect_guess(guesses_left, users_guess)
                print('Oops! That letter is not in my word: ')
                if is_guess_vowel:
                    print('You lost 2 guesses since your letter was a vowel.')
        print(get_guessed_word(secret_word, letters_guessed))
    end_game(guesses_left)

    

def hangman(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses

    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a letter!
    
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    # users start with 6 guesses and 3 warnings
    guesses_left = 6
    warnings_left = 3
    # there are no guessed letters at the start of the game
    letters_guessed = []
    # At the start of the game, let the user know how many letters the computer's word contains and how many guesses s/he starts with. 
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')
    print('You have ' + str(warnings_left) + ' warnings left.')
    ### continue user-comp interaction until the game is over where user has 0 guesses left or have correctly guessed the word
    while is_word_guessed(secret_word, letters_guessed) == False and guesses_left > 0:
    # before each guess from the user, put a dashed line seperator, tell the user how many guesses left and available letters
        seperator(guesses_left, letters_guessed)
    ### user interactions starts
    # ask for an input from the user
        users_guess = str.lower(input('Please guess a letter: '))
    # user has to type in an alphabetic letter, if not user gets a warning and after 3 warnings, user loses a guess
    # check if user's guess is within the user input requirements, if not, give a warning
        while warnings_left > 0:
    # the input of the user in not an aplhabetic character
            if str.isalpha(users_guess) == False:
                warnings_left -= 1
                print('Oops! That is not a valid letter. You have ' + str(warnings_left) + ' warnings left: ' + get_guessed_word(secret_word, letters_guessed))
                break
    # the input of the user is an alphabetic character that he/she already guessed
            elif str.isalpha(users_guess) == True and users_guess in letters_guessed:
                warnings_left -= 1
                print('Oops! You have already guessed that letter. You have ' + str(warnings_left) + ' warnings left: \n' + get_guessed_word(secret_word, letters_guessed))
                break
    # break out of this loop if user's input is acceptable
            elif str.isalpha(users_guess) == True and users_guess not in letters_guessed:
                vowels = 'aeiou'
                if check_user_guess(users_guess, letters_guessed, guesses_left) == False:
                    if users_guess in vowels:
                        print('You lost 2 guesses since your letter was a vowel.')
                        guesses_left -= 2
                    else:
                        guesses_left -= 1
                break
    # if the user already has 3 warnings, he/she loses a guess on every incorrect input
        else:
    # the input of the user in not an alphabetic character
            if str.isalpha(users_guess) == False:
                guesses_left -= 1
                print('Oops! That is not a valid letter. You have no warnings left so you lose one guess: ' + get_guessed_word(secret_word, letters_guessed))
    # the input of the user is an alphabetic character that he/she already guessed
            elif str.isalpha(users_guess) == True and users_guess in letters_guessed:
                guesses_left -= 1
                print('Oops! You have already guessed that letter. You have no warnings left so you lose one guess: \n' + get_guessed_word(secret_word, letters_guessed))
    # break out of this loop if user's input is acceptable
            elif str.isalpha(users_guess) == True and users_guess not in letters_guessed:
                vowels = 'aeiou'
                if check_user_guess(users_guess, letters_guessed, guesses_left) == False:
                    if users_guess in vowels:
                        print('You lost 2 guesses since your letter was a vowel.')
                        guesses_left -= 2
                    else:
                        guesses_left -= 1

    if guesses_left == 0:
        print('------------')
        print('Sorry, you ran out of guesses. The word was ' + secret_word + '.')
    else:
        total_score = guesses_left * len(set(secret_word))
        print('------------')
        print('Congratulations, you won!')
        print('Your total score for this game: ' + str(total_score))
        
    
        
# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
#(hint: you might want to pick your own
# secret_word while you're doing your own testing)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string with _ characters, current guess of secret word
    other_word: string, regular English word
    returns: boolean, True if all the actual letters of my_word match the 
        corresponding letters of other_word, or the letter is the special symbol
        _ , and my_word and other_word are of the same length;
        False otherwise: 
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    matching_letters = []
    underscores = []
    stripped_my_word = my_word.replace(' ', '')
    lowercase_letters = list(string.ascii_lowercase)
    if len(stripped_my_word) == len(other_word):
        for i in range(0, len(stripped_my_word)):
            if stripped_my_word[i] in lowercase_letters and stripped_my_word[i] == other_word[i]:
                matching_letters.append(stripped_my_word[i])
            elif stripped_my_word[i] not in lowercase_letters:
                underscores.append(stripped_my_word[i])
        unique_matching_letters = set(matching_letters)
        counter = 0
        for letter in unique_matching_letters:
            for i in range(0, len(other_word)):
                if letter == other_word[i]:
                    counter += 1
        if counter > len(matching_letters):
            return False
        elif len(matching_letters) + len(underscores) == len(other_word):
            return True
        else:
            return False
    else:
        return False
           
                
# match_with_gaps("te_ t", "tact")
# match_with_gaps("a_ _ le", "banana")
# match_with_gaps("a_ _ le", "apple")
# match_with_gaps("a_ ple", "apple")
# match_with_gaps("a_ pl_ ", "apple")


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    possible_matches = []
    for other_word in wordlist:
        if match_with_gaps(my_word, other_word) == True:
            possible_matches.append(other_word)
    if len(possible_matches) > 0:
        print(possible_matches)
    else:
        print('No matches found')
        

# show_possible_matches("t_ _ t")
# show_possible_matches("abbbb_ ")
# show_possible_matches("a_ pl_ ")

def hangman_with_hints(secret_word):
    '''
    secret_word: string, the secret word to guess.
    
    Starts up an interactive game of Hangman.
    
    * At the start of the game, let the user know how many 
      letters the secret_word contains and how many guesses s/he starts with.
      
    * The user should start with 6 guesses
    
    * Before each round, you should display to the user how many guesses
      s/he has left and the letters that the user has not yet guessed.
    
    * Ask the user to supply one guess per round. Make sure to check that the user guesses a letter
      
    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the 
      partially guessed word so far.
      
    * If the guess is the symbol *, print out all words in wordlist that
      matches the current guessed word. 
    
    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    guesses_left = 6
    warnings_left = 3
    # there are no guessed letters at the start of the game
    letters_guessed = []
    # At the start of the game, let the user know how many letters the computer's word contains and how many guesses s/he starts with. 
    print('Welcome to the game Hangman with hints!')
    print('I am thinking of a word that is ' + str(len(secret_word)) + ' letters long.')
    print('You have ' + str(warnings_left) + ' warnings left.')
    ### continue user-comp interaction until the game is over where user has 0 guesses left or have correctly guessed the word
    while is_word_guessed(secret_word, letters_guessed) == False and guesses_left > 0:
    # before each guess from the user, put a dashed line seperator, tell the user how many guesses left and available letters
        seperator(guesses_left, letters_guessed)
    ### user interactions starts
    # ask for an input from the user
        users_guess = str.lower(input('Please guess a letter: '))
    # user has to type in an alphabetic letter, if not user gets a warning and after 3 warnings, user loses a guess
    # check if user's guess is within the user input requirements, if not, give a warning
        while warnings_left > 0:
    # the input of the user in not an aplhabetic character
            if str.isalpha(users_guess) == False:
                if users_guess == '*':
                    print('Possible word matches are:')
                    show_possible_matches(get_guessed_word(secret_word, letters_guessed))
                    break
                else:
                    warnings_left -= 1
                    print('Oops! That is not a valid letter. You have ' + str(warnings_left) + ' warnings left: ' + get_guessed_word(secret_word, letters_guessed))
                    break
    # the input of the user is an alphabetic character that he/she already guessed
            elif str.isalpha(users_guess) == True and users_guess in letters_guessed:
                warnings_left -= 1
                print('Oops! You have already guessed that letter. You have ' + str(warnings_left) + ' warnings left: \n' + get_guessed_word(secret_word, letters_guessed))
                break
    # break out of this loop if user's input is acceptable
            elif str.isalpha(users_guess) == True and users_guess not in letters_guessed:
                vowels = 'aeiou'
                if check_user_guess(users_guess, letters_guessed, guesses_left) == False:
                    if users_guess in vowels:
                        print('You lost 2 guesses since your letter was a vowel.')
                        guesses_left -= 2
                    else:
                        guesses_left -= 1
                break
    # if the user already has 3 warnings, he/she loses a guess on every incorrect input
        else:
    # the input of the user in not an alphabetic character
            if str.isalpha(users_guess) == False:
                if users_guess == '*':
                    print('Possible word matches are:')
                    show_possible_matches(get_guessed_word(secret_word, letters_guessed))
                else:
                    guesses_left -= 1
                    print('Oops! That is not a valid letter. You have no warnings left so you lose one guess: ' + get_guessed_word(secret_word, letters_guessed))
    # the input of the user is an alphabetic character that he/she already guessed
            elif str.isalpha(users_guess) == True and users_guess in letters_guessed:
                guesses_left -= 1
                print('Oops! You have already guessed that letter. You have no warnings left so you lose one guess: \n' + get_guessed_word(secret_word, letters_guessed))
    # break out of this loop if user's input is acceptable
            elif str.isalpha(users_guess) == True and users_guess not in letters_guessed:
                vowels = 'aeiou'
                if check_user_guess(users_guess, letters_guessed, guesses_left) == False:
                    if users_guess in vowels:
                        print('You lost 2 guesses since your letter was a vowel.')
                        guesses_left -= 2
                    else:
                        guesses_left -= 1

    if guesses_left == 0:
        print('------------')
        print('Sorry, you ran out of guesses. The word was ' + secret_word + '.')
    else:
        total_score = guesses_left * len(set(secret_word))
        print('------------')
        print('Congratulations, you won!')
        print('Your total score for this game: ' + str(total_score))



# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.
    
    secret_word = choose_word(wordlist)
    hangman2(secret_word)

###############
    
    # To test part 3 re-comment out the above lines and 
    # uncomment the following two lines. 
    
    # secret_word = choose_word(wordlist)
    # hangman_with_hints(secret_word)
