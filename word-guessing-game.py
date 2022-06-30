#random will be used later to select random words from a list
import random

#starts paramater for the game loop
wordgame=True

#creates the scoreboard
victories = 0
defeats = 0
#grabs the potential words from the file words_alpha.txt 
#taken from https://github.com/dwyl/english-words/blob/master/words_alpha.txt
with open("words_alpha.txt", "r") as file:
    allanswers = file.read()
    answers = list(map(str, allanswers.split()))

used_answers = []
answer = random.choice(answers)

#Function for the gameplay
while wordgame:

    #make sure the current answer is new
    for answer in used_answers:
        if answer in used_answers:
            answer = random.choice(answers)
        else:
            continue
    # setting lives(guess_count), using ascii to show letters found in the word
    # creating a list of letters guessed for this word
    guess_count = 7    
    display = ['_' for i in answer]
    answer_guessed_letters = []

    # intro flavor text
    print('''Greeting, and welcome. I want to play a game. 
    The rules are simple. You try to guess the word of which I am thinking. 
    You have 7 tries. You can guess the whole word or inidividual letters''')
    
    #print the word for testing purposes only
    print(answer)

    #loop runs until player runs out of guesses
    while guess_count > 0:    
        print(f'{guess_count} tries remaining. Let us hope you make it in time.')
        guess = str(input('What is your guess?: '))

        #makes sure the answer is in the correct format
        if guess.isalpha()==True:

            # checks letter based on guess length, descriments guess count
            if len(guess) == 1:
                guess_count = guess_count -1

                #adds guessed letter to guessed letter list
                if guess in answer:
                    answer_guessed_letters = [i for i, singleletter in enumerate(answer) if singleletter == guess]

                    #adds letter to diplayed letters
                    for i in answer_guessed_letters:
                        display[i] = guess
                    
                    if '_' not in display:
                        print(f'You have survived this round. The word was {answer} and you guessed it correctly.')
                        break

                    else:
                        print(f'That letter is correct. Here is what you have: {display}')

                else:
                    print(f'Oh, not quite. {guess} was not in the word. Let us guess again.')
                
            # check if the entry is the whole word
            elif len(guess) > 1:
                guess_count = guess_count -1
                if guess == answer:
                    print(f'You have survived this round. The word was {answer} and you guessed it correctly.')
                    break
                else:
                    print(f'Oh not quite, {guess} was not the correct guess')
        #Throws text if answer is not correct format
        else:
            print('''You think I can be fooled by these tricks? You must guess a valid letter or word.
            You are lucky I did not take a guess away from you.''')

    #update the win loss count
    if guess_count == 0:
        defeats += 1

    else: 
        victories += 1

    print(f"The word is {answer}. You have {victories} victories and {defeats} defeats.")
    
    #prmopts for the next game
    another = input('Would you like to play another game? (Y/N): ').upper()
    if another == "Y":
        used_answers.append(answer)
    if another == "N":
        print(f'All together you had {victories} victories, and I defeated you {defeats} times.')
        wordgame=False
