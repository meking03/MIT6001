# Problem Set 4B
# Name: <your name here>
# Collaborators:
# Time Spent: x:xx

import string

### HELPER CODE ###
def load_words(file_name):
    '''
    file_name (string): the name of the file containing 
    the list of words to load    
    
    Returns: a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    '''
    print("Loading word list from file...")
    # inFile: file
    inFile = open(file_name, 'r')
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.extend([word.lower() for word in line.split(' ')])
    print("  ", len(wordlist), "words loaded.")
    return wordlist

def is_word(word_list, word):
    '''
    Determines if word is a valid word, ignoring
    capitalization and punctuation

    word_list (list): list of words in the dictionary.
    word (string): a possible word.
    
    Returns: True if word is in word_list, False otherwise

    Example:
    >>> is_word(word_list, 'bat') returns
    True
    >>> is_word(word_list, 'asdf') returns
    False
    '''
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in word_list

def get_story_string():
    """
    Returns: a story in encrypted text.
    """
    f = open("story.txt", "r")
    story = str(f.read())
    f.close()
    return story

### END HELPER CODE ###

WORDLIST_FILENAME = 'words.txt'

class Message(object):
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        self.message_text = text
        self.valid_words = load_words(WORDLIST_FILENAME)

    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class.
        This helps you avoid accidentally mutating class attributes.
        
        Returns: a COPY of self.valid_words
        '''
        return self.valid_words.copy()

    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        mapping = {}
        assert 0 <= shift < 26, 'Shift should be between 0 and 26'
        for index in range(len(lowercase_letters)):
            if index + shift < 26:
                mapping[lowercase_letters[index]] = lowercase_letters[index+shift]
                mapping[uppercase_letters[index]] = uppercase_letters[index+shift]
            else:
                mapping[lowercase_letters[index]] = lowercase_letters[index+shift-26]
                mapping[uppercase_letters[index]] = uppercase_letters[index+shift-26]
        return mapping

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        mapping = Message.build_shift_dict(self, shift)
        ciphered_text = []
        for letter in self.message_text:
            if letter in string.ascii_lowercase + string.ascii_uppercase:
                ciphered_letter = mapping[letter]
                ciphered_text.append(ciphered_letter)
            else:
                ciphered_text.append(letter)
        ciphered_text = ''.join(ciphered_text)
        return ciphered_text
    

class PlaintextMessage(Message):
    def __init__(self, text, shift):
        '''
        Initializes a PlaintextMessage object        
        
        text (string): the message's text
        shift (integer): the shift associated with this message

        A PlaintextMessage object inherits from Message and has five attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
            self.shift (integer, determined by input shift)
            self.encryption_dict (dictionary, built using shift)
            self.message_text_encrypted (string, created using shift)

        '''
        Message.__init__(self, text)
        self.shift = shift
        self.encryption_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)
        

    def get_shift(self):
        '''
        Used to safely access self.shift outside of the class
        
        Returns: self.shift
        '''
        return self.shift

    def get_encryption_dict(self):
        '''
        Used to safely access a copy self.encryption_dict outside of the class
        
        Returns: a COPY of self.encryption_dict
        '''
        return self.encryption_dict.copy()

    def get_message_text_encrypted(self):
        '''
        Used to safely access self.message_text_encrypted outside of the class
        
        Returns: self.message_text_encrypted
        '''
        return self.message_text_encrypted

    def change_shift(self, shift):
        '''
        Changes self.shift of the PlaintextMessage and updates other 
        attributes determined by shift.        
        
        shift (integer): the new shift that should be associated with this message.
        0 <= shift < 26

        Returns: nothing
        '''
        self.shift = shift
        self.encryption_dict = Message.build_shift_dict(self, shift)
        self.message_text_encrypted = Message.apply_shift(self, shift)


class CiphertextMessage(Message):
    def __init__(self, text):
        '''
        Initializes a CiphertextMessage object
                
        text (string): the message's text

        a CiphertextMessage object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words)
        '''
        Message.__init__(self, text)
        

    def decrypt_message(self):
        '''
        Decrypt self.message_text by trying every possible shift value
        and find the "best" one. We will define "best" as the shift that
        creates the maximum number of real words when we use apply_shift(shift)
        on the message text. If s is the original shift value used to encrypt
        the message, then we would expect 26 - s to be the best shift value 
        for decrypting it.

        Note: if multiple shifts are equally good such that they all create 
        the maximum number of valid words, you may choose any of those shifts 
        (and their corresponding decrypted messages) to return

        Returns: a tuple of the best shift value used to decrypt the message
        and the decrypted message text using that shift value
        '''
        all_texts = []
        shifts_used = []
        for s in range(1, 27):
            decrypted_message_text = Message.apply_shift(self, 26 - s)
            all_texts.append(decrypted_message_text)
            shifts_used.append(s)
            
        
        list_for_correct_word_counter = []
        for text in all_texts:
            correct_word_counter = 0
            for word in text.split():
                if is_word(self.valid_words, word):
                    correct_word_counter += 1
            list_for_correct_word_counter.append(correct_word_counter)
            # if len(text.split()) == 1:
            #     if is_word(self.valid_words, text):
            #         correct_word_counter += 1
            #     list_for_correct_word_counter.append(correct_word_counter)
            # else:
            #     for word in text.split():
            #         if is_word(self.valid_words, word):
            #             correct_word_counter += 1
            #     list_for_correct_word_counter.append(correct_word_counter)
                
        correct_index = list_for_correct_word_counter.index(max(list_for_correct_word_counter))
                
        
        # for index in range(0, len(list_for_correct_word_counter)):
        #     if list_for_correct_word_counter[index] == max(list_for_correct_word_counter):
        #         correct_index = index
        #         break
        
        return (26 - shifts_used[correct_index] , all_texts[correct_index])

if __name__ == '__main__':

    #Example test case (PlaintextMessage)
    plaintext = PlaintextMessage('hello', 2)
    print('Expected Output: jgnnq')
    print('Actual Output:', plaintext.get_message_text_encrypted())

    #Example test case (CiphertextMessage)
    ciphertext = CiphertextMessage('jgnnq')
    print('Expected Output:', (24, 'hello'))
    print('Actual Output:', ciphertext.decrypt_message())

    # TODO: WRITE YOUR TEST CASES HERE
    
    #Example test case 1 (PlaintextMessage)
    plaintext = PlaintextMessage('gErceK', 12)
    print('Expected Output: sQdoqW')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    
    #Example test case 2 (PlaintextMessage)
    plaintext = PlaintextMessage('Sahar', 4)
    print('Expected Output: Welev')
    print('Actual Output:', plaintext.get_message_text_encrypted())
    
    #Example test case 1 (CiphertextMessage)
    ciphertext = CiphertextMessage('Hkra')
    print('Expected Output:', (4, 'Love'))
    print('Actual Output:', ciphertext.decrypt_message())
    
    #Example test case 2 (CiphertextMessage)
    ciphertext = CiphertextMessage('ebuktkr')
    print('Expected Output:', (7, 'library'))
    print('Actual Output:', ciphertext.decrypt_message())
    
    # TODO: best shift value and unencrypted story
    
    encrypted_story = get_story_string()
    ciphertext = CiphertextMessage(encrypted_story)
    my_tuple = ciphertext.decrypt_message()
    print(my_tuple)

    
    
