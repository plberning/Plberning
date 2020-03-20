
# Patrick Berning. Chess Quiz. Integration project.
def grade(quiz_score):
     if (quiz_score == 100):
            print("Excellent job " + name + "! You got an A+") #TypeError: bad operand type for unary +: 'str'  #had , after "excellent job"
     elif (quiz_score < 100 and quiz_score > 80):
            print("Great job " + name + "! You got an A")
     elif (quiz_score < 90 and quiz_score >= 80):
            print("Good job " + name + "! You got a B")
     elif (quiz_score == 70):
            print("You passed " + name + "! You got a C")
     elif (quiz_score == 60):
            print("Study more " + name + " You got a D") # if name equaled a number than this method would not work because string + number + string will not work.
     else:
            print("Sorry you failed" , name , "You got a F") # if name equaled a number, this would work.
            
print("Welcome to Chess Quiz ")
# Ask user to input their name; assign their input to variable name.
correct_name = True
name =(input("What is your name? Please enter your name and then press enter. "))
    
# NOTE: PUT SPACES AFTER OPERATORS LIKE +   (corrected line below)
print("Hello "+ name)
# Assited by Vlad with line below. With his assistane I leaned variable = input(question).

start_Quiz = input("Are you ready to begin the quiz? Yes or No ")
if (start_Quiz == "yes" or start_Quiz == "Yes" or start_Quiz == "YES" or start_Quiz == "Y" or start_Quiz == "y"):
    quiz_complete = True
    while (quiz_complete == True):
    # Assited by Jairo with loop.
            

# When I learn loop I well set the else to go back to line 1/beginning when the answer to start quiz is no
# instructions.

        print("For multiple choice questions please type the letter of the answer you believe to be correct and then press enter")
    # Q1 user inputs a, b, c, or d. I also added capitols just incase user answer with capital letter.
        score = 0
        answer_Question_1 = input("#1 Which direction does a bishop move? A. Diagonally. B. Forward. C. Left and right. D. backwards ")
        if (answer_Question_1 == "A" or answer_Question_1 == "a"):
            score += 1
            # I came up with the short cut operator on my own (learned in class), but TA; Rachael assisted me in the location to place it.
            print("correct")
        else:
            print("incorrect")
            print("The correct answer is B because the bishop moves diagonally")
        answer_Question_2 = input("#2 Which direction does the rook move? A. Diagonally B. Only forward C. Only Backward D. None of these ")
        if (answer_Question_2 == "D" or answer_Question_2 == "d"):
            score += 1
            print("correct")
        else:
            print("incorrect")
            print("The rook moves only forward, left, right, and backwards")
        answer_Question_3 = input("#3 Which piece may move any direction any number of spaces? A. King B. Queen C. Bishop D. Rook ")
        if (answer_Question_3 == "B" or answer_Question_3 == "b"):
            score += 1
            print("correct")
        else:
            print("incorrect")
            print("The Queen may moveany direction any number of spaces")
        answer_Question_4 = input("#4 Which piece may move any direction, but only one space? A. King B. Queen. C. Rook D. Knight ")
        if (answer_Question_4 == "a" or answer_Question_4 == "A"):
            score += 1
            print("correct")
        else:
            print("incorrect")
            print("The King may move any direction, but only one space")
        answer_Question_5 = input("#5 When attacking which direction does the pawn move, and how many spaces? A. Two spaces diagonally B. Two spaces vertically or horizontally C. One space diagonally D. One space vertically or horizontally ")
        if (answer_Question_5 == "c" or answer_Question_5 == "C"):
            score += 1
            print("correct")
        else:
            print("incorrect")
        answer_Question_6 = input("#6 On a pawn's first move how many spaces may a pawn move? A. 2 or 3 B. 1 C. 2 D. 1 or 2 ")
        if (answer_Question_6 == "D" or answer_Question_6 == "d"):
            score += 1
            print("correct")
        else:
            print("incorrect")
        answer_Question_7 = input("#7 Which piece or pieces may move through another piece? A. Pawns and Rooks B. Kights and Bishops C. Only Bishops D. Only Kights ")
        if (answer_Question_7 == "D" or answer_Question_7 == "d"):
            score += 1
            print("correct")
        else:
            print("incorrect")
        answer_Question_8 = input("#8 How does a game of chess end? A. Stale mate B. Check mate C. Once a player has lost all pieces D. Both answer A & B ")
        if (answer_Question_8 == "D" or answer_Question_8 == "d"):
            score += 1
            print("correct")
        else:
            print("incorrect")
        answer_Question_9 = input("#9 Which piece or pieces move in the shape of a L? A. Knight and Bishop B. Knight C. Bishop D. Rook and Bishop ")
        if (answer_Question_9 == "B" or answer_Question_9 == "b"):
            score += 1
            print("correct")
        else:
            print("incorrect")
        print("#10 For this next question select all answers that apply. For example: if you believe the answer to be A and D than type AD and then press enter. Answer selection must be in alphabetical order. For example do not answer DA ")
        answer_Question_10 = input("Which piece or pieces may move diagonally? A. Rook B. King C. Bishop D. Pawn E. Knight F. Queen ")
        if (answer_Question_10 == "BCDF" or answer_Question_10 == "bcdf"):
            score += 1
            print("correct " + name + " Chess Quiz Complete!")
        else:
            print("incorrect " + name + " Chess Quiz Complete!")
        # numeric operator
        # NOTE: DON'T USE CAPITOLS FOR VARIABLES (  corrected line below)
        final_score = score * 10
        # most of my code is from using all the resources on the course website and just playing with/trail and error. 
        # brain storming
        #if (score == 10):
         #   score * 1000 = score
        #elif score == 9:
         #   score * 9
         #NOTE: PUT A SPACE AFTER COMMA FOR READABILITY. LINE BELOW. I DO NOT PREFER THIS
        print("Score:", final_score, "out of 100")
        final_score = int(final_score)

        #TRYING TO WORK THIS IN
        # purposely used multiply arithmic operators. would be simplier with less or the same.

        grade(final_score)

        restart_quiz_answer = input("Do you want to start the quiz again? ")
        if (restart_quiz_answer == "yes" or restart_quiz_answer == "Yes" or restart_quiz_answer == "YES" or restart_quiz_answer == "Y" or restart_quiz_answer == "y"):
            quiz_complete = True
            # For future if statements may be easier to use if the "if" state is the false
        else:
            quiz_complete = False
            print("Have a great day not doing the chess quiz!")
            #Another option would be to remove the else line below
else:
    print("Have a great day not doing the chess quiz!")


# ANSWER KEY: A, D, B, A, C, D, D, D, B, BCDF
# num_1=2
# num_1=num_1+3
# above lines is shortcut operator
# num1+=3
# above line is better shortcut operator that will get you chicks
# print(num_1)
# I have been writing code as I go. After watching the conditinals video I realize this whole process would have been eaiser if I started with notes of what I want to happein and then wrote code under each note. 
# How can I make multiple answer questions
# print(start_Question_1)
# Assited by Vlad with line above. With his assistane I leaned variable = input(question).
# most notes below are me practing and learning
# if ():
    
# if (start_Question_1==a or A):
#   print("correct")

# originally how I was trying to creat quiz before I leaned if else in class and was assisted by Vlad.
# A = True
# B = False
# C = False
# D = False
# a = True
# b = False
# c = False
# d = False
# print(
# Answer = input("Which direction does a bishop move? A. Diagonally. B. Forward. C. Left and right. D. backwards ")
# Correct_Answer = Diagonally

# Answer = input()
# Answer = input
