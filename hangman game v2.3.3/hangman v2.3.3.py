# Problem Set 2, hangman.py
# Name: Llanowar
# Collaborators:
# Time spent or crazy programmer's diary:
# 07.12.2019 --> THE BEGINNING:
# 18:03 --> START
# 19:26 --> I understood that it's difficult for me, but I don't give up...
# 20:18 --> I understand that my functions are wrong (it's bad) =(
# 20:53 --> lots of tests...
# 21:04 --> function by the name of 'get_guessed_word' is done (I think)
# 21:24 --> new file 'HANGMAN.py' was born (test of the same name function) (in my opinion the hardest function)
# 21:39 --> I decided to ask You about one detail. I'm waiting for Your answer...
# 21:55 --> thank You for Your help
# 22:30 --> first tests (a lot of errors). Try again...
# 22:45 --> underscores are my problems (not remember letters)
# 23:00 --> I understand what's a problem, but how to do it???
# 23:23 --> now I don't know what's a problem
# 23:37 --> I've found my mistake, yeah (it's good), bit it's not a finish...
# 08.12.2019 - new day (night), new possibilities:
# 00:05 --> !!! IT WORKS !!! 'Hangman game by Andy v1.0' was born. To be continued...
# 09:14 --> good morning or my way to 'Hangman game by Andy v2.0' (START)
# 09:43 --> 'is_word_guessed' function is done (now 100%)
# 10:33 --> word_output system is done. !!! v1.1 !!!
# 11:00 --> !!! v1.2 !!! (small details)
# 11:09 --> have a rest. See you soon my Hangman game. It's not a finish...
# 23:xx --> Thank you Sonya Rodina for your laptop <3. My hangman become better...
# 10.12.2019 - it was late and I want to sleep:
# 00:13 --> not so late for you, is it True? But for me it is late...
# 01:18 --> warnings system is done (!!! v1.3 !!!) + you can enter uppercase letters (SO GOOD)
# 10:52 --> it is time to continue...
# 11:37 --> I must go, anti-dibil system don't work as I want. Try later...
# 17:59 --> I have come back
# 19:53 --> how to do this anti-dibil system?
# 20:44 --> it works, but not as I want. Try again...
# 21:05 --> YEEEEEEEEEES!!! IT WORKS!!! anti-dibil system is done (I think) !!! v1.4 !!!
# 23:xx --> communication with user (you can not understand this string)
# 23:50 --> hints is difficult for me, but 3 months ago first lab was difficult for me too (think about it)...
# 11.12.2019 --> night is my best friend (no):
# 00:10 --> I want to sleep but I must continue
# 00:14 --> my new target and problem - match_with_gaps function (it is interesting and mysterious)
# 19:44 --> good evening, continue my work...
# 19:56 --> I decided to read rules and it broke my game and I must rewrite. That is a new reason why I don't read!!!
# 20:33 --> I found a new mistake
# 20:42 --> now I know what is Llanowar and I am a forest
# 22:46 -->  I have done HARDCORE 'matches_with_gaps' function, it works and I am happy, but exhausted !!! v1.5 !!!
# 23:26 --> I am close to the victory. Keeping going...
# 12.12.2019 --> I think that night will be very interesting
# 00:29 --> Sophia Rodina takes her laptop. Ehhh...
# 15:xx --> continue, new mistakes and new thoughts...
# 15:36 --> !!! IT WORKS !!! OFFICIALLY, 'Hangman game by Andy' !!! v2.0 !!! is available, now with hints!
# It can be a finish, but there are lots of details that I want to fix... New versions, soon... Last version - v2.3.9
# 15:47 --> I found and fixed a mistake and added a new detail !!! v2.1 !!!
# 16:13 --> fewer row ---> better program !!! v2.2 !!!
# 16:20 --> found and DESTROY a mistake. I am a fighter (cool) !!! v2.3 !!!
# 15.12.2019 --> 18/2- is good, but I think that I can better. Continue...
# 20:59 --> 1 guessES, really? I thought that my English is better !!! v2.3.1 !!!
# 22:05 --> new warnings system !!! v2.3.2 !!!
# 22:21 --> score system is done !!! v2.3.3 !!!


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

    counter = 0

    for letter in secret_word:
        if letter in letters_guessed:
            counter += 1

    return counter == len(secret_word)


def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, the word the user is guessing
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string, comprised of letters, underscores (_), and spaces that represents
      which letters in secret_word have been guessed so far.
    '''

    underscores = list('_' * len(secret_word))

    for letter in range(len(secret_word)):
        if secret_word[letter] in letters_guessed:
            underscores[letter] = secret_word[letter]
    return ' '.join(underscores)


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), which letters have been guessed so far
    returns: string (of letters), comprised of letters that represents which letters have not
      yet been guessed.
    '''

    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    available_letters = sorted(list(set(all_letters) - set(letters_guessed)))
    available_letters = ''.join(available_letters)
    return available_letters


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

    letters_number = len(secret_word)

    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    vowels = ['a', 'o', 'u', 'e', 'i']
    letters_guessed = []
    used_letters = []

    guesses = 6
    round_number = 1
    warnings = 0

    print('The secret word contains', letters_number, 'letters.')
    print(get_guessed_word(secret_word, letters_guessed))

    while guesses != 0:
        print('Round number', round_number, '\nYou have', guesses, 'guesses left')

        letter = input('Please guess a letter: ').lower()

        while letter not in all_letters:
            print('You MUST enter a letter!')
            if warnings != 3:
                warnings += 1
                print('You have', 3-warnings, 'warnings left!')
            else:
                guesses -= 1
                if guesses == 0:
                    break
            letter = input('Please guess a letter: ').lower()

        if guesses == 0:
            break

        while letter in used_letters:
            print('Oops! You have already guessed that letter!')
            if warnings != 3:
                warnings += 1
                print('You have', 3-warnings, 'warnings left!')
            else:
                guesses -= 1
                print('Too many warnings! You have just lost 1 guess.', '\nYou have', guesses, 'guesses left')
            if guesses == 0:
                break
            print('You have', 3-warnings, 'warnings left')
            letter = input('Please guess a letter: ').lower()
            while letter not in all_letters:
                print('You MUST enter a letter!')
                if warnings != 3:
                    warnings += 1
                    print('You have', 3-warnings, 'warnings left!')
                else:
                    guesses -= 1
                    if guesses == 0:
                        break
                print('You have', 3-warnings, 'warnings left!')
                letter = input('Please guess a letter: ').lower()

        if guesses == 0:
            break

        if letter in secret_word:
            print('Good guess. You are a lucky person:')
            letters_guessed.append(letter)
        else:
            if letter in vowels:
                guesses -= 2
            else:
                guesses -= 1
            print('Oops! That letter is not in secret word:')


        used_letters.append(letter)

        secret_word = list(secret_word)

        print(get_guessed_word(secret_word, letters_guessed))

        print('Used letters:', ', '.join(used_letters))
        print('Available letters:', ', '.join(sorted(list(set(get_available_letters(letters_guessed)) - set(used_letters)))))

        round_number += 1

        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations! You won!\n' + 'Your total score for this game is:', guesses * len(set(secret_word)))
            break
        print('-----------------------')
    if '_' in list(get_guessed_word(secret_word, letters_guessed)):
        print('You lose! But do not be upset.')
    print('Secret word was', ''.join(secret_word))


# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the first two lines to test
# (hint: you might want to pick your own
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

    counter = 0

    letters = list(other_word)

    if len(my_word) == len(other_word):
        for i in range(len(my_word)):
            if list(my_word)[i] == letters[i]:
                counter += 1
            elif list(my_word)[i] == '_':
                if letters[i] in list(my_word):
                    counter -= 1
                else:
                    counter += 1

    return counter == len(my_word)


def show_possible_matches(my_word):
    '''
    my_word: string with _ characters, current guess of secret word
    returns: nothing, but should print out every word in wordlist that matches my_word
             Keep in mind that in hangman when a letter is guessed, all the positions
             at which that letter occurs in the secret word are revealed.
             Therefore, the hidden letter(_ ) cannot be one of the letters in the word
             that has already been revealed.

    '''

    possible_matches = []

    for word in wordlist:
        if match_with_gaps(my_word, word):
            possible_matches.append(word)

    if len(possible_matches) == 0:
        print('No matches found')
    else:
        print(', '.join(possible_matches))


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

    letters_number = len(secret_word)

    all_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
                   'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    vowels = ['a', 'o', 'u', 'e', 'i']
    letters_guessed = []
    used_letters = []

    guesses = 6
    round_number = 1
    warnings = 0

    print('The secret word contains', letters_number, 'letters.')
    print(get_guessed_word(secret_word, letters_guessed))

    while guesses != 0:
        print('Round number', round_number, '\nYou have', guesses, 'guesses left')

        my_word = ''.join(get_guessed_word(secret_word, letters_guessed).split(' '))

        letter = input('Please guess a letter: ').lower()

        while letter == '*':
            print('Possible matches:')
            show_possible_matches(my_word)
            letter = input('Please guess a letter: ').lower()

        while letter not in all_letters:
            print('You MUST enter a letter!')
            if warnings != 3:
                warnings += 1
                print('You have', 3-warnings, 'warnings left!')
            else:
                guesses -= 1
                print('Too many warnings! You have just lost 1 guess.', '\nYou have', guesses, 'guesses left')
                if guesses == 0:
                    break
            letter = input('Please guess a letter: ').lower()
            while letter == '*':
                print('Possible matches:')
                show_possible_matches(my_word)
                letter = input('Please guess a letter: ').lower()

        if guesses == 0:
            break

        while letter in used_letters:
            print('Oops! You have already guessed that letter!')
            if warnings != 3:
                warnings += 1
                print('You have', 3-warnings, 'warnings left!')
            else:
                guesses -= 1
                print('Too many warnings! You have just lost 1 guess.', '\nYou have', guesses, 'guesses left')
            if guesses == 0:
                break
            letter = input('Please guess a letter: ').lower()
            while letter == '*':
                print('Possible matches:')
                show_possible_matches(my_word)
                letter = input('Please guess a letter: ').lower()
            while letter not in all_letters:
                print('You MUST enter a letter!')
                if warnings != 3:
                    warnings += 1
                    print('You have', 3-warnings, 'warnings left!')
                else:
                    guesses -= 1
                    if guesses == 0:
                        break
                letter = input('Please guess a letter: ').lower()
                while letter == '*':
                    print('Possible matches:')
                    show_possible_matches(my_word)
                    letter = input('Please guess a letter: ').lower()

        if guesses == 0:
            break

        if letter in secret_word:
            print('Good guess. You are a lucky person:')
            letters_guessed.append(letter)
        else:
            if letter in vowels:
                guesses -= 2
            else:
                guesses -= 1
            print('Oops! That letter is not in secret word:')

        used_letters.append(letter)

        secret_word = list(secret_word)

        print(get_guessed_word(secret_word, letters_guessed))

        print('Used letters:', ', '.join(used_letters))
        print('Available letters:', ', '.join(sorted(list(set(get_available_letters(letters_guessed)) - set(used_letters)))))

        round_number += 1

        if is_word_guessed(secret_word, letters_guessed):
            print('Congratulations! You won!\n' + 'Your total score for this game is:', guesses * len(set(secret_word)))
            break
        print('-----------------------')
    if '_' in list(get_guessed_word(secret_word, letters_guessed)):
        print('You lose! But do not be upset.')
    print('Secret word was', ''.join(secret_word))


# When you've completed your hangman_with_hint function, comment the two similar
# lines above that were used to run the hangman function, and then uncomment
# these two lines and run this file to test!
# Hint: You might want to pick your own secret_word while you're testing.


#if __name__ == "__main__":
    # pass

    # To test part 2, comment out the pass line above and
    # uncomment the following two lines.

    #secret_word = choose_word(wordlist)
    #hangman(secret_word)

###############

# To test part 3 re-comment out the above lines and
# uncomment the following two lines.

secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
