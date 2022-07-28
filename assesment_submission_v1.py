'''
File name: assesment_submission
creater: Ollie Robinson
Created: 29/6/2022
Description: A collection of various games. 
'''

import random
import time

# define functions
# function asking if the user wants to play a game again
def repeat_game(game):
    yes_no = 'no'
    yes_no = input('Do you want to play again? ')
    wrong = 'yes'
    while wrong == 'yes':
        if yes_no == 'yes' or yes_no == 'y' or yes_no == 'Yes':
            print('Okay then!')
            game()
        elif yes_no == 'no' or yes_no == 'n' or yes_no == 'No':
            print('Okay then, I have returned you to the menu.')
            main()
        else:
            yes_no = input("Please enter either 'yes' or 'no': ")
    return

# function testing whether an answer to a question is a number
def isnumeric(question):
    go = 1
    answer_int = 1
    while go == 1:
        answer = input(question)
        if answer.isnumeric():
            go = 2
            answer_int = int(answer)
        else:
            print('That is not a number. Please answer the question:')
    return answer_int

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------- ---------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------

# function for dodge game, defining each line
def dodge_game_line(place_one, place_two):
    if place_one == 1:
        print('⏬⬛')
    elif place_two == 1:
        print('⬛⏬')
    else:
        print('⬛⬛')
    return

   
# function for dodge game, defining main game
def dodge_game_main():
    oneone = 2
    onetwo = 2
    twoone = 2
    twotwo = 2
    threeone = 2
    threetwo = 2
    fourone = 2
    fourtwo = 2
    fiveone = 2
    fivetwo = 2
    repeat = 1
    side_letter = 'q'
    rand_int = 3
    side = 1
    difficulty = 1
    score = 0

    print('Instructions: ')
    print('')
    print('The five lines at the bottom of the screen is your game.')
    print('You are the circle, you are trying to avoid the triangles.')
    print("Enter 'a' to move left, and 'd' to move right.")
    print('Any other entry will move you forward.')
    print('You can move diagonally.')
    print('Good luck!')
    print('')
    print('')
    time.sleep(5)

    difficulty = input('Please select your difficulty. (e/m/h) ')
    if difficulty == 'e':
        hardness = 6
    elif difficulty == 'm':
        hardness = 4
    elif difficulty == 'h':
        hardness = 2
    else:
        print('You have not selected either e, m or h. In response, dificulty has been set to 0.001. Have fun!')
        hardness = 100
    
    while repeat == 1:

        if side == 1:
            rand_int = random.randint(1, 2)
            fiveone = fourone
            fivetwo = fourtwo
            fourone = threeone
            fourtwo = threetwo
            threeone = twoone
            threetwo = twotwo
            twoone = oneone
            twotwo = onetwo
            oneone = random.randint(1, hardness)
            onetwo = random.randint(1, hardness)
            if oneone == 1 and onetwo == 1 and random == 1:
                oneone = 2
            if oneone == 1 and onetwo == 1 and random == 2:
                onetwo = 2

                
            dodge_game_line(oneone, onetwo)
            dodge_game_line(twoone, twotwo)
            dodge_game_line(threeone, threetwo)

            if fourone == 1:
                print('GAME OVER')
                print('Score:',score)
                repeat = 3
                repeat_game(dodge_game_main)
                    
            elif fourtwo == 1:
                print('⚫⏬')
                score = score + 1
            else:
                print('⚫⬛')
                score = score + 1
            
            dodge_game_line(fiveone, fivetwo)

            side_letter = input('')
            if side_letter == 'a':
                side = 1
            elif side_letter == 'd':
                side = 2
            else:
                side = side

        #-----------------------------------------------------------------------
        elif side == 2:
            rand_int = random.randint(1, 2)
            fiveone = fourone
            fivetwo = fourtwo
            fourone = threeone
            fourtwo = threetwo
            threeone = twoone
            threetwo = twotwo
            twoone = oneone
            twotwo = onetwo
            oneone = random.randint(1, hardness)
            onetwo = random.randint(1, hardness)
            if oneone == 1 and onetwo == 1 and random == 1:
                oneone = 2
            if oneone == 1 and onetwo == 1 and random == 2:
                onetwo = 2

                
            dodge_game_line(oneone, onetwo)
            dodge_game_line(twoone, twotwo)
            dodge_game_line(threeone, threetwo)
            
            if fourone == 1:
                print('⏬⚫')
                score = score + 1
            elif fourtwo == 1:
                print('GAME OVER')
                print('Score:',score)
                repeat = 3
                repeat_game(dodge_game_main)
                main()
            else:
                print('⬛⚫')
                score = score + 1
                
            dodge_game_line(fiveone, fivetwo)

            side_letter = input('')
            if side_letter == 'a':
                side = 1
            elif side_letter == 'd':
                side = 2
            else:
                side = side
    return

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------

# find the number game
def finding_number():
    ARN = random.randint (1,50)
    counter = 1
    user_repeat = 'maybe'
    
    rn = isnumeric('I have generated a random number between 1 and 50. please try to guess it: ')
        
    while rn != ARN:
        counter = counter + 1
        if rn < ARN:
            rn = isnumeric('The number that I have generated is bigger than your guess. Please try again: ')
        if rn > ARN:
            rn = isnumeric('The number that I have generated is smaller than your guess. Please try again: ')
    print('You are correct!')
    print('It took you',counter,'guesses')
    repeat_game(finding_number)
    return

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------

#paper scissors rock function that codes for after each round.
def paper_scissers_rock_after(you, it):
    print('The score is:')
    print(you, ':' ,it)
    time.sleep(1)
    if you == 3:
        print('You have won! Congradulations!')
        repeat_game(paper_scissers_rock_main)
    elif it == 3:
        print('You have lost. Better luck next time!')
        repeat_game(paper_scissers_rock_main)
    else:
        print('Next round in:')
        time.sleep(1)
        print('Three')
        time.sleep(1)
        print('Two')
        time.sleep(1)
        print('One')
        time.sleep(1)
        print()
        print()
    return


# main code for paper scissors rock game.
def paper_scissers_rock_main():
    CHOICES = ['Paper', 'Scissors', 'Rock']
    PAPER = ['p', 'paper']
    SCISSORS = ['s', 'scissors', 'scissers']
    ROCK = ['r', 'rock']
    you_won = 0
    it_won = 0
    simplified_choice = 'a'


    print('We are going to play paper, scissors, rock.')
    print('First one to get three rounds wins.')
    while you_won <3 and it_won <3:
        personal_choice  = input('Give me your choice: ')
        computer_choice = random.choice (CHOICES)
        if personal_choice.lower() in PAPER and computer_choice == 'Paper' or personal_choice.lower() in SCISSORS and computer_choice == 'Scissors' or personal_choice.lower() in ROCK and computer_choice == 'Rock':
            if personal_choice.lower() in PAPER:
                simplified_choice = 'Paper'
            elif personal_choice.lower() in SCISSORS:
                simplified_choice = 'Scissors'
            elif personal_choice.lower() in ROCK:
                simplified_choice = 'Rock'
            print('I chose ', computer_choice, ' and you chose', simplified_choice)
            print('It is a draw.')
            paper_scissers_rock_after(you_won, it_won)

        elif personal_choice.lower() in PAPER and computer_choice == 'Rock' or personal_choice.lower() in SCISSORS and computer_choice == 'Paper' or personal_choice.lower() in ROCK and computer_choice == 'Scissors':
            if personal_choice.lower() in PAPER:
                simplified_choice = 'Paper'
            elif personal_choice.lower() in SCISSORS:
                simplified_choice = 'Scissors'
            elif personal_choice.lower() in ROCK:
                simplified_choice = 'Rock'
            print('I chose ', computer_choice, ' and you chose', simplified_choice)
            print('You have won!')
            you_won = you_won + 1
            paper_scissers_rock_after(you_won, it_won)

        elif personal_choice.lower() in PAPER and computer_choice == 'Scissors' or personal_choice.lower() in SCISSORS and computer_choice == 'Rock' or personal_choice.lower() in ROCK and computer_choice == 'Paper':
            if personal_choice.lower() in PAPER:
                simplified_choice = 'Paper'
            elif personal_choice.lower() in SCISSORS:
                simplified_choice = 'Scissors'
            elif personal_choice.lower() in ROCK:
                simplified_choice = 'Rock'
            print('I chose ', computer_choice, ' and you chose', simplified_choice)
            print('You have lost.')
            it_won = it_won + 1
            paper_scissers_rock_after(you_won, it_won)

        else:
            print('Please insert either paper, scissors or rock.')
    return

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------

# define function containing the code for each question
def math_question(dictonary, ability):

    # create variables and pick a random question
    user_answer = ''
    question, answer = random.choice(list(dictonary.items()))

    # discerne how hard the question will be
    if ability <= 2:
        print('Easy question:')
    elif ability >= 3 and ability <= 4:
        print('Medium question:')
    elif ability >= 5:
        print('Hard question:')

    # ask the chosen question
    user_answer = input('What is {}? '.format(question))

    # check the user's answer against a list of possable answers
    # decide how hard the next question will be
    if user_answer in answer:
        print('You are correct!')
        if ability != 6:
            ability = ability + 1
    else:
        print('You are not correct!')
        if ability != 0:
            ability = ability - 1

    # return
    return ability

#-----------------------------------------------------------------

# define function containing the after - quiz feedback.
def math_feedback(value, question_number):

    # print a different answer depending on how hard the question asked was.
    if value == 1:
        print('⬛---- Question no. {}.'.format(question_number))
    elif value == 2:
        print('--⬛-- Question no. {}.'.format(question_number))
    elif value == 3:
        print('----⬛ Question no. {}.'.format(question_number))

    # return
    return


#-----------------------------------------------------------------
        

# define function containing main code for math quiz
def math_main():

    # define variables
    skill = 3
    question_no = 0
    question_feedback = ['1']
    ques_feed = 1
    counter = 0

    # define dictonarys with all the questions
    questions_easy = {'one minus one':['zero', 'Zero', '0'],
                 'two plus two':['four', 'Four', '4'],
                 'three plus three':['six', 'Six', '6'],
                 'four minus two':['two', 'Two', '2']}
    
    questions_medium = {'medium question_1':['one', 'One', '1'],
                 'medium question_2':['two', 'Two', '2'],
                 'medium question_3':['three', 'Three', '3'],
                 'medium question_4':['four', 'Four', '4']}
    
    questions_hard = {'the square root of eighty-one':['nine', 'Nine', '9'],
                 '5 factorial':['one hundred and twenty', 'One Hundred And Twenty', '120'],
                 'XVII minus IX ':['eight', 'Eight', '8', 'VIII', 'viii']}

    # print introduction
    print('This is a maths quiz. ')
    number_of_questions = isnumeric('How many questions do you want? ')
    print('Okay then.')
    print('Please answer each question to the best of your ability.')

    # repeat questions until desired number of questions has been reached
    while question_no <= number_of_questions-1:

        # record a uestion has been asked, and introduce the question
        question_no = question_no + 1
        print()
        print('---------------')
        print()
        print('Question {}'.format(question_no))

        # call the question function with a different dictonary depending on varible 'skill'
        # add the difficulty of asked question to a list.
        if skill <= 2:
            question_feedback.append(1)
            skill = math_question(questions_easy, skill)
        elif skill >= 3 and skill <= 4:
            question_feedback.append(2)
            skill = math_question(questions_medium, skill)
        elif skill >= 5:
            question_feedback.append(3)
            skill = math_question(questions_hard, skill)

    # introduce the feedback
    print()
    print()
    print('Feedback:')
    print()
    print('E, M, H')

    # call the feedback function with an increasing question number and question.
    for counter in range(number_of_questions):
        counter = counter + 1
        ques_feed = question_feedback[counter]
        math_feedback(ques_feed, counter)

    # give option to repeat
    repeat_game(math_main)
    return

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------

#define wordle function to check if each letter in he word is correct.
def wordle_check(chosen, users_letter, section, letter):
    check = chosen.find(users_letter)
    if users_letter == letter:
        section = '☑️'
    elif check >= 0:
        section = '⬛️'
    else:
        section = '❌'
    return section
    
# define main code for wordle game
def wordle_main():
    go = 1
    userguess = 'aaaaa'
    WORDS = ['Polar','Speed','React','Awoke','Belly','Chase','Lodge','Ditch','Refit','Plain','Crazy','Round','Ready','Armor','Shout','Towel','Saute','Drink','Gross','Dance','Whine','Scrub','Event','Bless','Giddy','Debit','Squat','Still','Worse','Brown']
    word = random.choice(WORDS).lower()
    letter1 = word[0]
    letter2 = word[1]
    letter3 = word[2]
    letter4 = word[3]
    letter5 = word[4]
    section1 = '❌'
    section2 = '❌'
    section3 = '❌'
    section4 = '❌'
    section5 = '❌'
    while go == 1:
        userguess = input('Tell me your guess: ').strip()
        while not userguess.isalpha():
            userguess = input('That is not alphabetical. Please tell me your guess: ').strip()
        while not len(userguess) == 5:
            userguess = input('That is not a five letter word. Please tell me your guess: ').strip()
        userletter1 = userguess[0].lower()
        userletter2 = userguess[1].lower()
        userletter3 = userguess[2].lower()
        userletter4 = userguess[3].lower()
        userletter5 = userguess[4].lower()

        check = word.find(userletter1)
        if userguess == word:
            print('YAY! You got it!')
            repeat_game(wordle_main)
        section1 = wordle_check(word, userletter1, section1, letter1)
        section2 = wordle_check(word, userletter2, section2, letter2)
        section3 = wordle_check(word, userletter3, section3, letter3)
        section4 = wordle_check(word, userletter4, section4, letter4)
        section5 = wordle_check(word, userletter5, section5, letter5)
        print('{} {}  {}  {} {}'.format(userletter1.capitalize(), userletter2.capitalize(), userletter3.capitalize(), userletter4.capitalize(), userletter5.capitalize()))
        print('{}{}{}{}{}'.format(section1, section2, section3, section4, section5))
    return

#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------

# define tic-tac-toe function checking which square eas selected, and what to change it to. 
def test(player, player_number, user_select, letter, ti, tic, xo, counter):
    if player == player_number and user_select == letter:
        if ti == 1:
            counter = counter+1
            tic = xo
            ti = 2
            if player == 1:
                player = 2
            elif player == 2:
                player = 1
    return player, tic, ti, counter

# define main code for tic-tac-toe
def tictactoe_main():
    tic1 = '⬛'
    tic2 = '⬛'
    tic3 = '⬛'
    tic4 = '⬛'
    tic5 = '⬛'
    tic6 = '⬛'
    tic7 = '⬛'
    tic8 = '⬛'
    tic9 = '⬛'
    ti1 = 1
    ti2 = 1
    ti3 = 1
    ti4 = 1
    ti5 = 1
    ti6 = 1
    ti7 = 1
    ti8 = 1
    ti9 = 1
    player = 2
    go = 1
    user_select = 'q'
    counter = 0
    print(' Q | W | E')
    print('---+---+---')
    print(' A | S | D')
    print('---+---+---')
    print(' Z | X | C')
    print('Any letters or numbers apart from the above will not do anything, you will be asked to repeat your turn.')
    while go == 1:
        user_select = input('Input letter: ')

        go = 1
        player, tic1, ti1, counter = test(player, 1, user_select, 'q', ti1, tic1, '❌', counter)
        player, tic2, ti2, counter = test(player, 1, user_select, 'w', ti2, tic2, '❌', counter)
        player, tic3, ti3, counter = test(player, 1, user_select, 'e', ti3, tic3, '❌', counter)
        player, tic4, ti4, counter = test(player, 1, user_select, 'a', ti4, tic4, '❌', counter)
        player, tic5, ti5, counter = test(player, 1, user_select, 's', ti5, tic5, '❌', counter)
        player, tic6, ti6, counter = test(player, 1, user_select, 'd', ti6, tic6, '❌', counter)
        player, tic7, ti7, counter = test(player, 1, user_select, 'z', ti7, tic7, '❌', counter)
        player, tic8, ti8, counter = test(player, 1, user_select, 'x', ti8, tic8, '❌', counter)
        player, tic9, ti9, counter = test(player, 1, user_select, 'c', ti9, tic9, '❌', counter)
        player, tic1, ti1, counter = test(player, 2, user_select, 'q', ti1, tic1, '🟣', counter)
        player, tic2, ti2, counter = test(player, 2, user_select, 'w', ti2, tic2, '🟣', counter)
        player, tic3, ti3, counter = test(player, 2, user_select, 'e', ti3, tic3, '🟣', counter)
        player, tic4, ti4, counter = test(player, 2, user_select, 'a', ti4, tic4, '🟣', counter)
        player, tic5, ti5, counter = test(player, 2, user_select, 's', ti5, tic5, '🟣', counter)
        player, tic6, ti6, counter = test(player, 2, user_select, 'd', ti6, tic6, '🟣', counter)
        player, tic7, ti7, counter = test(player, 2, user_select, 'z', ti7, tic7, '🟣', counter)
        player, tic8, ti8, counter = test(player, 2, user_select, 'x', ti8, tic8, '🟣', counter)
        player, tic9, ti9, counter = test(player, 2, user_select, 'c', ti9, tic9, '🟣', counter)
        print(tic1, tic2, tic3)
        print(tic4, tic5, tic6)
        print(tic7, tic8, tic9)
        if tic1 == '❌' and tic2 == '❌' and tic3 == '❌' or tic4 == '❌' and tic5 == '❌' and tic6 == '❌' or tic7 == '❌' and tic8 == '❌' and tic9 == '❌' or tic1 == '❌' and tic4 == '❌' and tic7 == '❌' or tic2 == '❌' and tic5 == '❌' and tic8 == '❌' or tic3 == '❌' and tic6 == '❌' and tic9 == '❌' or tic1 == '❌' and tic5 == '❌' and tic9 == '❌' or tic3 == '❌' and tic5 == '❌' and tic7 == '❌':
            print('Yay! ❌ won!')
            repeat_game(tictactoe_main)
        elif tic1 == '🟣' and tic2 == '🟣' and tic3 == '🟣' or tic4 == '🟣' and tic5 == '🟣' and tic6 == '🟣' or tic7 == '🟣' and tic8 == '🟣' and tic9 == '🟣' or tic1 == '🟣' and tic4 == '🟣' and tic7 == '🟣' or tic2 == '🟣' and tic5 == '🟣' and tic8 == '🟣' or tic3 == '🟣' and tic6 == '🟣' and tic9 == '🟣' or tic1 == '🟣' and tic5 == '🟣' and tic9 == '🟣' or tic3 == '🟣' and tic5 == '🟣' and tic7 == '🟣':
            print('Yay! 🟣 won!')
            repeat_game(tictactoe_main)
        elif counter == 9:
            print('The game is a draw.')
            repeat_game(tictactoe_main)
    return
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------
#-----------------------------------------------------------------------------------------------------------------------------------------------------

# define main code - calls all the other games.
def main():
    which_game = 0
    print('1: Dodge Game')
    print('2: Find the Number')
    print('3: Paper Scissers Rock')
    print('4: Math Quiz')
    print('5: Wordle')
    print('6: tic-tac-toe')
    print('10: Exit')
    which_game = int(input('Which game do you want to play? '))
    if which_game == 1:
        dodge_game_main()
    elif which_game == 2:
        finding_number()
    elif which_game == 3:
        paper_scissers_rock_main()
    elif which_game == 4:
        math_main()
    elif which_game == 5:
        wordle_main()
    elif which_game == 6:
        tictactoe_main()


    elif which_game == 10:
        print('Okay then. Goodbye!')

    return
    
main()
