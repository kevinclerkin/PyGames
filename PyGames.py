import random

#Program that allows user/s to play either Rock, Paper, Scissors, Lizard, Spock or Hangman

print("**************************************************************************")
print("*************************   Game Menu   ********************************************")
print("Press  1 to   Play: Rock, Paper, Scissors, Lizard, Spock")
print("Press  2 to   Play: Hangman")
print("Press  3 to   Exit:")
print(sep="")

#asks for user selection
user_selection = int(input("Choose your game: "))
    



# presents continuous game menu to user
while user_selection != 3:
    if user_selection == 1:
        options = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        #original solution contained if, elif, else statements covering all possible outcomes
        #smaller/more efficient solution uses a scoring matrix/data structure from https://www.askpython.com/python/examples/rock-paper-scissors-in-python
        #solution adapted with scoring matrix, which assigns a value to each option in options 
        # 5 x 5 arrary includes a score for all possible outcomes when player 1 and player 2 choose from options
        scoring_matrix = [[-1, 1, 0, 0, 4],[1, -1, 2, 3, 1], [0, 2, -1, 2, 4], [0, 3, 2, -1, 3], [4, 1, 4, 3, -1]]
        player_1 = ""
        player_2 = ""
        attempts = 0
        player_1_wins = 0
        player_2_wins = 0
        print("SCISSORS CUTS PAPER")
        print(sep="")
        print("PAPER COVERS ROCK")
        print(sep="")
        print("ROCK CRUSHES LIZARD")
        print(sep="")
        print("LIZARD POISONS SPOCK")
        print(sep="")
        print("SPOCK SMASHES SCISSORS")
        print(sep="")
        print("SCISSORS DECAPITATES LIZARD")
        print(sep="")
        print("LIZARD EATS PAPER")
        print(sep="")
        print("PAPER DISPROVES SPOCK")
        print(sep="")
        print("SPOCK VAPORIZES ROCK")
        print(sep="")
        print("ROCK CRUSHES SCISSORS")
        print(sep="")

        #asks for user input and breaks after 5 attempts
        while attempts < 5:
            player_1 = str(input("Player 1: pick one of - Rock, Paper, Scissors, Lizard, Spock: ")).lower()
            while player_1 not in options:
                player_1 = str(input("Player 1: pick one of - Rock, Paper, Scissors, Lizard, Spock: ")).lower()
                
            player_2 = str(input("Player 2: pick one of - Rock, Paper, Scissors, Lizard, Spock: ")).lower()
            while player_2 not in options:
                player_2 = str(input("Player 2: pick one of - Rock, Paper, Scissors, Lizard, Spock: ")).lower()
            
            #iterates through options and maps index to index in scoring matrix
            for i, option in enumerate(options):
                i == scoring_matrix[i]
            
            #assigns a different value to each player option from options
            if player_1 == "rock":
                player_1_option = 0
            
            elif player_1 == "paper":
                player_1_option = 1    
    
            elif player_1 == "scissors":
                player_1_option = 2
    
            elif player_1 == "lizard":
                player_1_option = 3
    
            elif player_1 == "spock":
                player_1_option = 4

            if player_2 == "rock":
                player_2_option = 0
    
            elif player_2 == "paper":
                player_2_option = 1    
    
            elif player_2 == "scissors":
                player_2_option = 2
    
            elif player_2 == "lizard":
                player_2_option = 3
    
            elif player_2 == "spock":
                player_2_option = 4 

            #each assigned value for each player option is matched to the equivalent index in the scoring matrix
            winner = scoring_matrix[player_1_option][player_2_option]

            #increments player 1 wins if winner 
            if winner == player_1_option:
                player_1_wins += 1
                print(sep="")
                print("Player 1 is the winner")
            
            #increments player 2 wins if winner
            elif winner == player_2_option:
                player_2_wins += 1
                print(sep="")
                print("Player 2 is the winner")
           
           #displays if there's a tie
            else:
                print("It's a tie!")

            
            #displays current score
            print(sep="")
            print("Player 1: {0}".format(player_1_wins))
            print("Player 2: {0}".format(player_2_wins))
            print(sep="")
            
            # each iteration increments the number of attempts by 1
            attempts += 1 
        
        #displays overall result
        if player_1_wins > player_2_wins:
                print("The overall winner is Player 1")
        elif player_2_wins > player_1_wins:
            print("The overall winner is Player 2")
        else:
            print("No overall winner! It's a tie!")  
    
    elif user_selection == 2:
        #list of words to be picked by computer
        hangman_words = ['baubles' , 'guards' , 'boneshaker' , 'drudges' , 'medicide' , 'fullbottom' , 'coagulase' , 'simmer' , 'bunnia' , 'tremie' , 'muttonheads' , 'roughneck' , 'creds' , 'timberline' , 'emberiza' , 'dominionism' , 'sunsets' , 'cucujo' , 'earthbank' , 'streaks' , 'extravagate' , 'conjuncture' , 'elongator' , 'ology' , 'cutworms' , 'refusion' , 'levitator' , 'unbowel' , 'keenness' , 'droschka' , 'darnels' , 'flammables' , 'wildtype' , 'gypsy' , 'retrainee' , 'piaga' , 'giddyhead' , 'rastafarianism' , 'selenology' , 'hymenoptera' , 'wristdrop' , 'triggermen' , 'multilingualism' , 'cloaths' , 'hemophobia' , 'retrofit' , 'commandments' , 'unglue' , 'inshining' , 'nicholas' , 'hotfoot' , 'pubkeeper' , 'gastank' , 'uprun' , 'stabler' , 'doctrinaires' , 'akathisia' , 'ribcage' , 'neurophysicist' , 'unappropriate']
        #random assignment of chosen word from hangman_words
        chosen_word = random.choice(hangman_words)
        user_guess = ""
        guesses = ""
        lives = 9
        wrong_letter = 0
        print(sep="")
        print("Welcome to Hangman! Guess the word! You have 9 lives!")
        
        # user starts with 9 lives
        while lives > 0:
            wrong_letter = 0
            guesses += user_guess 
            
            #iterates through chosen computer word and prints user guess at index if in chosen word
            for letter in chosen_word:
                if letter in guesses:
                    print(letter, end=" ")
                # displays an underscore for every letter in chosen computer word
                # increments wrong-letter-counter by 1 for each wrong guess    
                else:
                    print("_", end=" ")
                    wrong_letter += 1
            
            #if every letter in user guess is correct, displays each letter of word and does not increment wrong-letter-counter
            #if wrong-letter-counter is unincremented, then user guessed word correctly. BREAK LOOP
            if wrong_letter == 0:
                print(sep="")
                print(end="")
                print("Well done, you guessed the word correctly!")
                break
            
            #asks for user input
            print(sep="")
            print(sep="")    
            user_guess = str(input("Guess a letter in this unknown word: ")).lower()
            
            
             
            # decrements a life for evey wrong guess by user and alerts user of wrong guess
            if user_guess not in chosen_word:
                lives -= 1
                print(sep="")
                print("That's a wrong guess!")
                
                #ends game when no lives remain; displays message to user
                if lives == 0:
                    print(sep="")
                    print("Sorry, you have no lives left!")         
                
                #displays remaining lives to user after each wrong guess
                else:
                    print(sep="")
                    print(f"You still have {lives} lives left!")
            #alerts user to correct guess
            else:
                print(sep="")
                print("You guessed correctly!") 
    else:
        print(sep="")
        print("**************************************************************************")
        print("*************************   Game Menu   ********************************************")
        print("***** Press  1 to   Play: Rock, Paper, Scissors, Lizard, Spock")
        print("****  Press  2 to   Play: Hangman")
        print("****  Press 3 to    Exit")

        user_selection = int(input("Choose your game: "))          