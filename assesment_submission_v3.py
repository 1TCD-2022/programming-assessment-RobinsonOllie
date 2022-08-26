# import modules
import random
import time

'''
File name: assesment_submission
creater: Ollie Robinson
Created: 29/6/2022
Description: A collection of various games.
'''

'''
If it is helpful:
Dictonaries in math quiz
Editing a list in wordle
Lists in wordle, maths and paper/scissers/rock
Return at end of every function
Five comment lines with (---) divides between different games
while loop in most, an example below in def isnumeric
if / elif / else in most, an example below in def isnumeric
For loop in math quiz
inputing and outputting values are all of the not main functions, an example being below def isnumeric.
'''


# define functions

def isnumeric(question):
    '''
    This function automaticly dictates whether the answer to a question (that is input) is a number, and returns the answer.
    '''
    # define variables
    go = 1
    answer_int = 1
    # create loop
    while go == 1:
        # ask question, take input and judge whether input is a number
        answer = input(question).strip()
        if answer.isnumeric():
            answer_int = int(answer)
            # break the loop
            go = 2
        # if answer is not a number, run the loop again
        else:
            print('That is not a number. Please answer the question:')
    # return the answer to the inputed question
    return answer_int


def repeat_game(game):
    '''
    This function ia an automatic game repeater.
    When called, this askes the user if they want to play again, and either plays the game again or return to the menu.
    Every game calles this when it ends.
    '''

    # define variable
    yes_no = 'no'
    # ask user whether to play again, and repeat game
    yes_no = input('Do you want to play again? ')
    yes_no = yes_no.strip()
    yes_no = yes_no.lower()
    check_repeat = 1
    while check_repeat == 1:
        if yes_no == 'yes' or yes_no == 'y' or yes_no == 'Yes':
            print('Okay then!')
            print()
            print()
            check_repeat = 2
            game()
        elif yes_no == 'no' or yes_no == 'n' or yes_no == 'No':
            print()
            print('Very well.')
            print()
            check_repeat = 2
        else:
            yes_no = input("Please enter either 'yes' or 'no': ")
    return

'''
Math quiz below
-------------------------------------------------------------------------------------------------------------
'''


def math_question(dictonary, ability):
    '''
    this function takes a dictonary as input, selects a random question and answer from it, and askes it, recording whether the answer is right or wrong.
    '''

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
    user_answer = user_answer.lower()

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


def math_feedback(value, question_number):
    '''
    This function prints a line on whether the question is easy, medium or hard.
    '''

    # print a different answer depending on how hard the question asked was.
    if value == 1:
        print('⬛---- Question no. {}.'.format(question_number))
    elif value == 2:
        print('--⬛-- Question no. {}.'.format(question_number))
    elif value == 3:
        print('----⬛ Question no. {}.'.format(question_number))

    # return
    return


def math_main():

    '''
    This function is the main function for the math quiz. It defines most of the varibles and dictonaries.
    It selects whether the question would be easy medium or hard, and calls the math_question function with that.
    It then prints feedback with the ,math_feedback function.
    '''

    # define variables
    skill = 3
    question_no = 0
    question_feedback = ['1']
    ques_feed = 1
    counter = 0

    # define dictonarys with all the questions
    questions_easy = {'one minus one': ['zero', 'Zero', '0'],
                      'two plus two': ['four', 'Four', '4'],
                      'three plus three': ['six', 'Six', '6'],
                      'four minus two': ['two', 'Two', '2']}

    questions_medium = {'medium question_1': ['one', 'One', '1'],
                        'medium question_2': ['two', 'Two', '2'],
                        'medium question_3': ['three', 'Three', '3'],
                        'medium question_4': ['four', 'Four', '4']}

    questions_hard = {'the square root of eighty-one': ['nine', 'Nine', '9'],
                      '5 factorial': ['one hundred and twenty', 'One Hundred And Twenty', '120'],
                      'XVII minus IX ': ['eight', 'Eight', '8', 'VIII', 'viii']}

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

    # return
    return

'''
Dodge game below
-------------------------------------------------------------------------------------------------------------
'''


def dodge_game_line(place_one, place_two):
    '''
    This function prints a line for the dodge game, depending on what input it gets
    '''

    # check what the line should be, and print it
    if place_one == 1:
        print('⏬⬛')
    elif place_two == 1:
        print('⬛⏬')
    else:
        print('⬛⬛')

    # return
    return


def dodge_game_main():
    '''
    This function is the main function for the dodge game.
    It calles the dodge_game_line function for each line of the game, randomises where the obsticles spawn and records where the player is.
    '''
    # define variables
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

    # print game instructions
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

    # ask and set difficulty
    difficulty = input('Please select your difficulty. (e/m/h) ')
    difficulty = difficulty.lower()
    difficulty = difficulty.strip()
    if difficulty == 'e' or 'easy':
        hardness = 6
    elif difficulty == 'm' or 'medium':
        hardness = 4
    elif difficulty == 'h' or 'hard':
        hardness = 2
    else:
        print('You have not selected either e, m or h. In response, dificulty has been set to 0.001. Have fun!')
        hardness = 100

    # estblish a loop that the game runs in
    while repeat == 1:

        if side == 1:

            # randomise first row, and set other rows to the one above
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

            # make sure both squares will not both be a one
            if oneone == 1 and onetwo == 1 and random == 1:
                oneone = 2
            if oneone == 1 and onetwo == 1 and random == 2:
                onetwo = 2

            # call function above to print the game
            dodge_game_line(oneone, onetwo)
            dodge_game_line(twoone, twotwo)
            dodge_game_line(threeone, threetwo)

            # check and run game over else print line
            if fourone == 1:
                print('GAME OVER')
                print('Score:', score)
                repeat = 3
                repeat_game(dodge_game_main)
            elif fourtwo == 1:
                print('⚫⏬')
                score = score + 1
            else:
                print('⚫⬛')
                score = score + 1

            # check if game is over
            if repeat != 3:

                # print last game line
                dodge_game_line(fiveone, fivetwo)

                # ask for letter command for next loop
                side_letter = input('')
                side_letter = side_letter.lower()
                side_letter = side_letter.strip()
                if side_letter == 'a':
                    side = 1
                elif side_letter == 'd':
                    side = 2
                else:
                    side = side

        # -----------------------------------------------------------------------
        elif side == 2:

            # randomise first row, and set other rows to the one above
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

            # make sure both squares will not both be a one
            if oneone == 1 and onetwo == 1 and random == 1:
                oneone = 2
            if oneone == 1 and onetwo == 1 and random == 2:
                onetwo = 2

            # call functions above to print the game
            dodge_game_line(oneone, onetwo)
            dodge_game_line(twoone, twotwo)
            dodge_game_line(threeone, threetwo)

            # check and run game over else print line
            if fourone == 1:
                print('⏬⚫')
                score = score + 1
            elif fourtwo == 1:
                print('GAME OVER')
                print('Score:', score)
                repeat = 3
                repeat_game(dodge_game_main)
            else:
                print('⬛⚫')
                score = score + 1

            # check if game is over
            if repeat != 3:

                # print last game line
                dodge_game_line(fiveone, fivetwo)

                # ask for letter command for next loop
                side_letter = input('')
                side_letter = side_letter.lower()
                side_letter = side_letter.strip()
                if side_letter == 'a':
                    side = 1
                elif side_letter == 'd':
                    side = 2
                else:
                    side = side

    # return
    return

'''
Finding number game below
-------------------------------------------------------------------------------------------------------------
'''


def finding_number():
    '''
    This function is the only function for find the number game. It runs the whole game.
    '''

    # define varibles
    go = 1
    ARN = random.randint(1, 50)
    counter = 1
    user_repeat = 'maybe'

    # get a number input, and check whether it is a number or a decimal
    while go == 1:
        rn = input('I have generated a random number between 1 and 50. please try to guess it: ')
        try:
            rn = float(rn)
            go = 2
        except:
            print('That is not a number. Please answer the question:')

    # check whether the user number is bigger or smaller than the computer generated one
    while rn != ARN:
        counter = counter + 1
        if rn < ARN:
            while go == 1:
                rn = input('The number that I have generated is bigger than your guess. Please try again: ')
                try:
                    rn = float(rn)
                    go = 2
                except:
                    print('That is not a number. Please answer the question:')
            go = 1

        if rn > ARN:
            while go == 1:
                rn = input('The number that I have generated is smaller than your guess. Please try again: ')
                try:
                    rn = float(rn)
                    go = 2
                except:
                    print('That is not a number. Please answer the question:')
            go = 1
    # if the number is not either bigger or smaller than the computer one, print 'you won' and end the game
    print('You are correct!')
    print('It took you', counter, 'guesses')

    # call repeat game function
    repeat_game(finding_number)

    # return
    return

'''
Paper scissers rock game below
-------------------------------------------------------------------------------------------------------------
'''


def paper_scissers_rock_after(you, it):
    '''
    This function checks whether you won paper scissers rock or not, and prints answers accordingly. It then counts down to the next question.
    '''

    # print score, and print reaction statment
    print('The score is:')
    print(you, ':', it)
    if you == 3:
        print('You have won! Congradulations!')
        repeat_game(paper_scissers_rock_main)
    elif it == 3:
        print('You have lost. Better luck next time!')
        repeat_game(paper_scissers_rock_main)
    else:
        print('Next round in one second')
        time.sleep(1)

    # return
    return


def paper_scissers_rock_main():
    '''
    This function is the main code for paper scissers rock.
    '''

    # define varibles and lists
    CHOICES = ['Paper', 'Scissors', 'Rock']
    PAPER = ['p', 'paper']
    SCISSORS = ['s', 'scissors', 'scissers']
    ROCK = ['r', 'rock']
    you_won = 0
    it_won = 0
    simplified_choice = 'a'

    # give instructions
    print('We are going to play paper, scissors, rock.')
    print('First one to get three rounds wins.')

    # check if game over, and ask for choice
    while you_won < 3 and it_won < 3:
        personal_choice = input('Give me your choice: ')
        personal_choice = personal_choice.strip()
        personal_choice = personal_choice.lower()

        # check if draw
        computer_choice = random.choice(CHOICES)
        if personal_choice in PAPER and computer_choice == 'Paper' or personal_choice in SCISSORS and computer_choice == 'Scissors' or personal_choice in ROCK and computer_choice == 'Rock':
            if personal_choice in PAPER:
                simplified_choice = 'Paper'
            elif personal_choice in SCISSORS:
                simplified_choice = 'Scissors'
            elif personal_choice in ROCK:
                simplified_choice = 'Rock'
            print('I chose {} and you chose {}'.format(computer_choice, simplified_choice))
            print('It is a draw.')
            paper_scissers_rock_after(you_won, it_won)

        # check if win
        elif personal_choice in PAPER and computer_choice == 'Rock' or personal_choice in SCISSORS and computer_choice == 'Paper' or personal_choice in ROCK and computer_choice == 'Scissors':
            if personal_choice in PAPER:
                simplified_choice = 'Paper'
            elif personal_choice in SCISSORS:
                simplified_choice = 'Scissors'
            elif personal_choice in ROCK:
                simplified_choice = 'Rock'
            print('I chose {} and you chose {}'.format(computer_choice, simplified_choice))
            print('You have won!')
            you_won = you_won + 1
            paper_scissers_rock_after(you_won, it_won)

        # check if lose
        elif personal_choice in PAPER and computer_choice == 'Scissors' or personal_choice in SCISSORS and computer_choice == 'Rock' or personal_choice in ROCK and computer_choice == 'Paper':
            if personal_choice in PAPER:
                simplified_choice = 'Paper'
            elif personal_choice in SCISSORS:
                simplified_choice = 'Scissors'
            elif personal_choice in ROCK:
                simplified_choice = 'Rock'
            print('I chose {} and you chose {}'.format(computer_choice, simplified_choice))
            print('You have lost.')
            it_won = it_won + 1
            paper_scissers_rock_after(you_won, it_won)

        else:
            print('Please insert either paper, scissors or rock.')

    # return
    return


'''
Wordle game below
-------------------------------------------------------------------------------------------------------------
'''


def wordle_check(chosen, users_letter, section, letter):
    '''
    This function checks whether each letter in the word is correct
    '''
    check = chosen.find(users_letter)
    if users_letter == letter:
        section = '☑️'
    elif check >= 0:
        section = '⬛️'
    else:
        section = '❌'
    return section


def wordle_main():
    '''
    This function is the main function for wordle.
    It randomises a word form a list, askes the user for a word, and checks each letter using the wordle_check function.
    '''

    # define varibles and lists
    go = 1
    userguess = 'aaaaa'
    wordle_sections = []
    WORDS = ['Polar', 'Speed', 'React', 'Awoke', 'Belly', 'Chase', 'Lodge', 'Ditch', 'Refit', 'Plain', 'Crazy', 'Round', 'Ready', 'Armor', 'Shout', 'Towel', 'Sauce', 'Drink', 'Gross', 'Dance', 'Whine', 'Scrub', 'Event', 'Bless', 'Giddy', 'Debit', 'Squat', 'Still', 'Worse', 'Brown']
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

    # print instructions
    print('Instructions:')
    print()
    print('This is wordle. Please guess a five-letter word.')
    print('The computer will generate one too. Your goal is to guess the computers word.')
    print('You have unlimited tries.')
    print('Below each letter of your guess, a symbol will appear.')
    print('Cross means that letter is not in the word that the computer generated')
    print('Square means that the letter is in the computer-generated word, but that it is in the wrong place.')
    print('Tick means the letter is in the same place as in the computer genarated word')
    print('Good luck!')

    # establish loop
    while go == 1:
        userguess = input('Tell me your guess: ')
        userguess = userguess.strip()
        userguess = userguess.lower()
        # check guess
        while not userguess.isalpha() or not len(userguess) == 5:
            userguess = input('That is not a five letter word. Please tell me your guess: ')
            userguess = userguess.strip()
            userguess = userguess.lower()

        # break word into five letters
        userletter1 = userguess[0].lower()
        userletter2 = userguess[1].lower()
        userletter3 = userguess[2].lower()
        userletter4 = userguess[3].lower()
        userletter5 = userguess[4].lower()
        check = word.find(userletter1)

        # check if guess is correct
        if userguess == word:
            print('YAY! You got it!')
            go = 2
            repeat_game(wordle_main)

        # run each letter through the function above, and add the returned value to a list
        else:
            wordle_shape = wordle_check(word, userletter1, section1, letter1)
            wordle_sections.append(wordle_shape)
            wordle_shape = wordle_check(word, userletter2, section2, letter2)
            wordle_sections.append(wordle_shape)
            wordle_shape = wordle_check(word, userletter3, section3, letter3)
            wordle_sections.append(wordle_shape)
            wordle_shape = wordle_check(word, userletter4, section4, letter4)
            wordle_sections.append(wordle_shape)
            wordle_shape = wordle_check(word, userletter5, section5, letter5)
            wordle_sections.append(wordle_shape)

            # print the letters, and the list
            print('{}  {}   {}   {}  {}'.format(userletter1.capitalize(), userletter2.capitalize(), userletter3.capitalize(), userletter4.capitalize(), userletter5.capitalize()))
            print(*wordle_sections)

            # clear the list
            wordle_sections = []

    # return
    return


'''
Tic-tac-toe game below
-------------------------------------------------------------------------------------------------------------
'''


def tictactoe_test(player, player_number, user_select, letter, ti, tic, xo, counter):
    '''
    This function checks to see which square was selected, and what to turn it to
    '''
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


def tictactoe_main():
    '''
    This function is the main function for tic-tac-toe game
    '''

    # define varibles
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

    # print instructions
    print(' Q | W | E')
    print('---+---+---')
    print(' A | S | D')
    print('---+---+---')
    print(' Z | X | C')
    print('Any letters or numbers apart from the above will not do anything, it will still be your turn, and you will be prompted to enter a letter again.')
    while go == 1:
        user_select = input('Input letter: ')
        user_select = user_select.strip()
        user_select = user_select.lower()
        go = 1

        # check every move the player could have made with the function above, and update grid
        player, tic1, ti1, counter = tictactoe_test(player, 1, user_select, 'q', ti1, tic1, '❌', counter)
        player, tic2, ti2, counter = tictactoe_test(player, 1, user_select, 'w', ti2, tic2, '❌', counter)
        player, tic3, ti3, counter = tictactoe_test(player, 1, user_select, 'e', ti3, tic3, '❌', counter)
        player, tic4, ti4, counter = tictactoe_test(player, 1, user_select, 'a', ti4, tic4, '❌', counter)
        player, tic5, ti5, counter = tictactoe_test(player, 1, user_select, 's', ti5, tic5, '❌', counter)
        player, tic6, ti6, counter = tictactoe_test(player, 1, user_select, 'd', ti6, tic6, '❌', counter)
        player, tic7, ti7, counter = tictactoe_test(player, 1, user_select, 'z', ti7, tic7, '❌', counter)
        player, tic8, ti8, counter = tictactoe_test(player, 1, user_select, 'x', ti8, tic8, '❌', counter)
        player, tic9, ti9, counter = tictactoe_test(player, 1, user_select, 'c', ti9, tic9, '❌', counter)
        player, tic1, ti1, counter = tictactoe_test(player, 2, user_select, 'q', ti1, tic1, '🟣', counter)
        player, tic2, ti2, counter = tictactoe_test(player, 2, user_select, 'w', ti2, tic2, '🟣', counter)
        player, tic3, ti3, counter = tictactoe_test(player, 2, user_select, 'e', ti3, tic3, '🟣', counter)
        player, tic4, ti4, counter = tictactoe_test(player, 2, user_select, 'a', ti4, tic4, '🟣', counter)
        player, tic5, ti5, counter = tictactoe_test(player, 2, user_select, 's', ti5, tic5, '🟣', counter)
        player, tic6, ti6, counter = tictactoe_test(player, 2, user_select, 'd', ti6, tic6, '🟣', counter)
        player, tic7, ti7, counter = tictactoe_test(player, 2, user_select, 'z', ti7, tic7, '🟣', counter)
        player, tic8, ti8, counter = tictactoe_test(player, 2, user_select, 'x', ti8, tic8, '🟣', counter)
        player, tic9, ti9, counter = tictactoe_test(player, 2, user_select, 'c', ti9, tic9, '🟣', counter)

        # print grid
        print(tic1, tic2, tic3)
        print(tic4, tic5, tic6)
        print(tic7, tic8, tic9)

        # check if someone won
        if tic1 == '❌' and tic2 == '❌' and tic3 == '❌' or tic4 == '❌' and tic5 == '❌' and tic6 == '❌' or tic7 == '❌' and tic8 == '❌' and tic9 == '❌' or tic1 == '❌' and tic4 == '❌' and tic7 == '❌' or tic2 == '❌' and tic5 == '❌' and tic8 == '❌' or tic3 == '❌' and tic6 == '❌' and tic9 == '❌' or tic1 == '❌' and tic5 == '❌' and tic9 == '❌' or tic3 == '❌' and tic5 == '❌' and tic7 == '❌':
            print('Yay! ❌ won!')
            repeat_game(tictactoe_main)
            go = 2
        elif tic1 == '🟣' and tic2 == '🟣' and tic3 == '🟣' or tic4 == '🟣' and tic5 == '🟣' and tic6 == '🟣' or tic7 == '🟣' and tic8 == '🟣' and tic9 == '🟣' or tic1 == '🟣' and tic4 == '🟣' and tic7 == '🟣' or tic2 == '🟣' and tic5 == '🟣' and tic8 == '🟣' or tic3 == '🟣' and tic6 == '🟣' and tic9 == '🟣' or tic1 == '🟣' and tic5 == '🟣' and tic9 == '🟣' or tic3 == '🟣' and tic5 == '🟣' and tic7 == '🟣':
            print('Yay! 🟣 won!')
            repeat_game(tictactoe_main)
            go = 2
        elif counter == 9:
            print('The game is a draw.')
            go = 2
            repeat_game(tictactoe_main)

    # return
    return
'''
Reaction timer game below
-------------------------------------------------------------------------------------------------------------
'''


def reaction_main():
    '''
    This function is the only function for the reaction timer.
    '''
    # define varibles
    random_time = random.randint(1, 10)

    # print instructions
    print("When you see 'go' printed, press enter.")
    time.sleep(2)
    print('Ready')

    # randomise wait period, and start timer
    time.sleep(random_time)
    start = time.time()
    result = input('go')

    # minus timer from time already played in the game
    duration = time.time() - start

    # print responce
    print('It took you {} seconds to respond! Good job!'.format(duration))
    repeat_game(reaction_main)

    # return
    return

'''
main code below
-------------------------------------------------------------------------------------------------------------
'''


def main():
    '''
    This function is the main function. It asks the user which game they would like to play, and calls the main function for that game.
    '''

    # define varibles
    main_repeat = 1
    which_game = 0

    # establish loop
    while main_repeat == 1:

        # print menu
        print()
        print('This is the menu of this game. Please select one of the following:')
        print()
        print('1: Dodge Game')
        time.sleep(0.2)
        print('2: Find the Number')
        time.sleep(0.2)
        print('3: Paper Scissers Rock')
        time.sleep(0.2)
        print('4: Math Quiz')
        time.sleep(0.2)
        print('5: Wordle')
        time.sleep(0.2)
        print('6: tic-tac-toe')
        time.sleep(0.2)
        print('7: Reaction Timer')
        time.sleep(0.2)
        print('8: Exit')
        time.sleep(0.2)

        # ask for a responce, and check it through the function isnumeric
        which_game = isnumeric('Which game do you want to play? ')

        # play the games
        if which_game == 1:
            print()
            dodge_game_main()
        elif which_game == 2:
            print()
            finding_number()
        elif which_game == 3:
            print()
            paper_scissers_rock_main()
        elif which_game == 4:
            print()
            math_main()
        elif which_game == 5:
            print()
            wordle_main()
        elif which_game == 6:
            print()
            tictactoe_main()
        elif which_game == 7:
            print()
            reaction_main()
        elif which_game == 8:
            print('Okay then. Goodbye!')
            main_repeat = 2
        else:
            print('Plese select the number for a game above')
            print('I will reprint the menu for you.')
            main()

# run all the code
main()
