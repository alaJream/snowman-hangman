import random

def load_word():
    '''
    A function that reads a text file of words and randomly selects one to use as the secret word
        from the list.

    Returns: 
           string: The secret word to be used in the spaceman guessing game
    '''
    f = open('words.txt', 'r')
    words_list = f.readlines()
    f.close()
    
    words_list = words_list[0].split(' ') #comment this line out if you use a words.txt file with each word on a new line
    secret_word = random.choice(words_list)
    return secret_word

def is_word_guessed(secret_word, letters_guessed):
    '''
    A function that checks if all the letters of the secret word have been guessed.

    Args:
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        bool: True only if all the letters of secret_word are in letters_guessed, False otherwise
    '''
    # TODO: Loop through the letters in the secret_word and check if a letter is not in lettersGuessed
    for char in secret_word:
        if char != "\n":
            if char not in letters_guessed:
                return False

    print("I CAN'T BELIEVE YOU WON\nAHHHHHHHHH")
    return True

def get_guessed_word(secret_word, letters_guessed):
    '''
    A function that is used to get a string showing the letters guessed so far in the secret word and underscores for letters that have not been guessed yet.

    Args: 
        secret_word (string): the random word the user is trying to guess.
        letters_guessed (list of strings): list of letters that have been guessed so far.

    Returns: 
        string: letters and underscores.  For letters in the word that the user has guessed correctly, the string should contain the letter at the correct position.  For letters in the word that the user has not yet guessed, shown an _ (underscore) instead.
    '''

    #TODO: Loop through the letters in secret word and build a string that shows the letters that have been guessed correctly so far that are saved in letters_guessed and underscores for the letters that have not been guessed yet
    # example: glasses, u a j, __a____
    # with the letters guessed, loop through secret_word, if letter shows correct then show letter 
    # otherwise show the rest of secret_word as "_"
    word = [ ]
    for letter in secret_word:
        correct_letter = False
        for guessed_letter in letters_guessed:
            if letter == guessed_letter:
                word.append(letter)
                correct_letter = True
        if correct_letter == False:
            word.append("_")
    return "|".join(word)



def is_guess_in_word(user_guess, secret_word):
    '''
    A function to check if the guessed letter is in the secret word

    Args:
        guess (string): The letter the player guessed this round
        secret_word (string): The secret word

    Returns:
        bool: True if the guess is in the secret_word, False otherwise

    '''
    #TODO: check if the letter guess is in the secret word
    guessed_correctly = False
    for letter in secret_word:
        if user_guess == letter:
            print("WOW That one was correct!")
            guessed_correctly = True
            return True
    if guessed_correctly == False:
        print("\nHAHAHA\n\nYou got that wrong!")
        return False
  




def spaceman(secret_word):
    '''
    A function that controls the game of spaceman. Will start spaceman in the command line.

    Args:
      secret_word (string): the secret word to guess.

    '''
    print("\n\nWELCOME!\n\nbrrrr..\n\nTo The\n\nSNOWMAN GAME! \n\n\nHere you have 7 tries to guess the word I have chosen!\n\n ***shivers***\n\n")
    print("You can only guess 1 letter per round!")
    letters_guessed = []
    guesses_left = 7
    while guesses_left > 0:
   

        #TODO: show the player information about the game according to the project spec
        # explain game to user
        

        # ---------------------------------
        #TODO: Ask the player to guess one letter per round and check that it is only one letter
        # check through length to make sure length of word is one letter
        # if more than one, print "only one letter!"
        
        user_guess = input("Enter your guess!")
        if len(user_guess) > 1:
            print("ONLY 1 LETTER")
            return

        # ---------------------------------
        #TODO: Check if the guessed letter is in the secret or not and give the player feedback
        # check if letter is in secret_word, print if it is or not
        is_guess_in_word(user_guess, secret_word)
        guessed_right = is_guess_in_word(user_guess, secret_word)
        if guessed_right == False:
            guesses_left -= 1
        letters_guessed.append(user_guess)
        print(f"\nbrrrr....\n\nYou have {guesses_left} guesses remaining!")

        #else: letters_guessed.append(guess)
        

        # ---------------------------------
        #TODO: show the guessed word so far
        # print status of secret word
        get_guessed_word(secret_word, letters_guessed)
        print(get_guessed_word(secret_word, letters_guessed))

        # ---------------------------------
        #TODO: check if the game has been won or lost
        # print if user won or lost after 7 incorrect guesses
        if (guesses_left < 1):
            print("HAHAHA\nI KNEW YOU'D LOSE")
            print(f"The word was: {secret_word}")
            play_again()
            break
        word_guessed = is_word_guessed(secret_word, letters_guessed)
        if word_guessed == True:
            play_again() 
def play_again():
    run_it_back = input("PLAY AGAIN. y/n: ")
    if run_it_back == "y":
        start_game()
    else: return

def start_game():
    secret_word = load_word()
    spaceman(secret_word)

start_game()

# These function calls that will start the game
