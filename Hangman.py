"""
OBJECTIVE:
    The objective is to create a hangman game
ALGORITHIM:
    First we need to write the three functions in our program
    The first function that will be defined is the function that randomly selects a word from the text dictionary we will create.
    The second function defined is the function that takes an input from the user which will be each letter guessed 
    The third function defined will be the one that will take what the user enters and turns it into a string
    In order for the first function to work we need to create a text file that the program can reference.
    Next we need to make sure we are working in the main module
    Now we need to create the various variables we are going to use to store the data the user enters
    We need a variable for the word the computer 
    We will also need to create a set of data that holds the letters guessed wrong and another one for letters guessed correctly
    Next we need to display an introduction to the program so users will know what to do
    Next we will build a repetitive system, so that the user will keep guessing words 
    Next we will code the game itself
    The first step is to have the user guess a word 
    Next we will create different options whether the user guessed the correct or incorrect 
    The next step is to print out the number of guesses that the user has left ans what they currently have guessed correctly in the word 
    The final step is a conditional at the end that lets them know if they won or not
PSUEDOCODE:
    This is taking the algorithm we just wrote and adding what code we can use to complete each step
    First we need to write the three functions in our program 
    We will use the define functions tool to create the functions
    The first function that will be defined is the the function that  that randomly selects a word from the dictionary we will create 
    We will us the open() function and the .readlines() functions to bring the text file into the program
    The second function defined is the function that takes an input from the user which will be each letter guessed
    We will usr the input() function to bring the users inout into the program
    The third function defined will be the one that will take the letters guesses correctly and turns it into a string
    We will usr a list and loop to check which letters they guesses and put it in the order of the word
    Create a text file that the program can reference
    We will use LuClipse to create the text file
    Next we need to make sure we are working in the main module
    We will use a conditional statement to check if we are working in the main module
    Then, create the various variables we are going to usr to store the data the user enter
    We need a variable for the word the computer picks
    We will also need to create a list that holds the letters guesses wrong and another list for letters guessed correctly
    Nect we need to print an introduction to the program
    Next we need to create a loop that allows the user to keep guessing
    We will use a while loop to repeat the game
    Next we will code the game itself
    The first step is to have the user guess a word
    Next we will create different options whether the user guessed correct or incorrect
    The next step is to print out the number of guesses that the user has left and what they currently have guesses in the word
    WE will use the .format() function to format the print statement
    The final step is a conditional statement that will print if the user won or not
    """
 
import random 
 
def pick_random_word():
    """
    This function picks a random word from the words dictionary.
    """
    # open the words dictionary
    with open("words.txt", 'r') as f:
        words = f.readlines()
            
    # generate a random index
    #-1 because len(words) is not a valid index into the list 'words'
    index = random.randint(0, len(words)-1)
        
    #print out the word at that index
    word = words[index].strip()
    return word 
    

def ask_user_for_next_letter():
    #this function gets a letter guess from the user
    letter = input("Guess your letter")
    return letter.strip().upper()



def generate_word_string(word, letters_guessed):
    #this function generates the word display that shows which letters have been guessed correctly
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter.upper())
        else: 
            output.append("_")
    return " ".join(output)

#this condition checks that the module we are using is currently the main module
if __name__ == '_main_':
    WORD = pick_random_word()
    
    letters_to_guess = set(WORD)
    correct_letters_guessed = set()
    incorrect_letters_guessed = set ()
    num_guesses = 0
    
    print("Welcome to Hangman, Halsey Songs Edition!!!")
    #this loop repeats the guessing sequence until the user guesser all the word or until the user runs out of get_lib_location_guesses
    while (len(letters_to_guess) > 0) and num_guesses < 6:
        guess = ask_user_for_next_letter()
        guess = guess.lower()
        #check if we already guessed letter 
        
        if guess in correct_letters_guessed or \
                guess in incorrect_letters_guessed:
            # print out a message 
            print("You already guessed that letter.")
            continue
        
        #if the guess was correct 
        if guess in letters_to_guess:
            #update the letters_to_guess
            letters_to_guess.remove(guess)
            #update the correct the letters guessed
            correct_letters_guessed.add(guess)
        else:
            incorrect_letters_guessed.add(guess)
            #only update the number of guesses if you guess incorrecty
            num_guesses += 1
            
        word_string = generate_word_string(WORD, correct_letters_guessed)
        print(word_string)
        print("You have () guesses left".format(6 - num_guesses))
        
    #tell the user they have won or lost 
    if num_guesses < 6:
        print("Congratulations! You have guessed the song (). You WIN!!!".format(WORD))
    else:
        print("Sorry, you lose. The song was ()".format(WORD))
        