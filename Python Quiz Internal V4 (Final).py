##Version 1
##First working quiz

##Version 2
##Far more effient quiz
##Layed out some ground works for player making quiz
##Added comments an will continue to do so

##Version 3
##Got player made quiz working and some overall changes

##Version 4
##Final finished product
##Overall Quality of life changes 



nz_amount_of_question = 10  ##Constant vairable (amount of Questions in the NZ quiz)
p1_slot = 0          ##This is to see iff there is a player made quiz in slot
start = True         ##Start up
make_overwrite = False    ##Process for making quiz if there i already a quiz in the quiz slot
menu = False         ##Menu
pick_quiz = False    ##Picking a quiz
nz = False           ##NZ quiz
make_p1 = False      ##Making a quiz
p1 = False           ##PLaying player made quiz         
nz_score = 0         ##NZ Score
nz_questions = ["Q1: How many stars does the New Zealand flag have? \n a)3 \n b)7 \n c)5 \n d)4", \
        "Q2: New Zealand has three official languages. English and New Zealand sign language are two. What is the other one? \n a)Samoan \n b)Maori \n c)Indian \n d)Fijian", \
        "Q3: Which of the following is NOT a bank operating in New Zealand? \n a)ANZ \n b)Bank of Wellington \n c)Kiwibank \n d)Country Wide Bank", \
        "Q4: Aotearoa (New Zealand) means what? \n a)Land of the long white cloud \n b)Land of the long black cloud \n c)Land of the long lost cloud \n d)Land of the clouds", \
        "Q5: Which popular New Zealand comedian, who had their own show, died of a heart attack in 1991? \n a)Michele A' Court \n b)Jon Gadsby \n c)David Mcphail \n d)Billy T.James", \
        "Q6: The first Europeans known to have reached New Zealand were led by Abel Tasman, who sailed up the West Coasts of the North & South Islands in which year? \n a)1640 \n b)1645 \n c)1644 \n d)1642", \
        "Q7: Former New Zealand Prime Minister Helen Clark is affiliated with which political party? \n a)ACT NZ \n b)Green Party \n c)Labour Party \n d)National Party", \
        "Q8: Which New Zealand sports team has the best winning record of any male national team? \n a)Silver Ferns \n b)All Blacks \n c)Tall Blacks \n d)All Whites", \
        "Q9:Which New Zealand mountain is 23 kilometres North East of Ohakune, 40 kilometres South West of the southern shore of Lake Taupo and is part of Tongariro National Park? \n a)Mount Tasman \n b)Mount Cook \n c)Mount Ruapehu \n d)Mangere Mountain", \
        "Q10: Which of these is not a popular New Zealand junk-food? \n a)Cheetos \n b)Burger Rings \n c)Twisties \n d)Rashuns"]
        ##NZ Questions and answers options
            
nz_correct_answer = ["d", "b", "b", "a", "d", "d", "c", "b", "c", "a"] ##Correct answers for NZ Quiz
p1_score = 0        ##PLayer made quiz Score
p1_questions = []           ##Player made quiz questions
p1_answer = []           ##PLayer made quiz answer options
p1_correct_answer = []           ##Player made quiz correct answers
p1_current_questions = 0      ##Total amount of questions for player made quiz
p1_current_answer = 0     ##So player made quiz can cycle correctly for the correct answer option
p1_current_correct_answer = 0     ##So player made quiz can cycle correctly for the correct answer
    


while start == True:      ##Start menu(Press enter to start
    print("Welcome to the Quiz")
    start_in=input("Press Enter to Continue")
    if start_in == "":
        start = False
        menu = True
    else:
        print("WHY?",)  ##Error catching 
    print()
    

##Main menu
##Everythig falls under this loop so that it can loop and go between while loops
while menu == True:  
    print("Menu", "\n" "Type 'play' to pick a quiz", "\n" "Type 'make' to make a quiz", "\n" "Type 'quit' to quit the program")
    play_make=input()
    if play_make == "play":  ##Picking what quiz you want
        pick_quiz = True
    elif play_make == "make":  ##Making a quiz
        make_overwrite = True
    elif play_make == "quit":  ##Quiting a program
        menu = False
    else:
        print("We don't support that sorry")  ##ERROR catching
    print()  ##These print Statments or any other \n ares for looks no pratical use
        




    while pick_quiz == True:  ##Quiz pick      ## All print statements attempt to be in one line by using \n so it doesn't take up so much room
        print("NZ General Knowledge. Difficulty: Average. Questions: 10. Type 'NZ' to play", "\n" "Type 'p1' for player made quiz 1", "\n" "Press Enter to Return to Menu")
        quiz_play=input()
        if quiz_play == "NZ":  ##NZ quiz
            nz = True
            pick_quiz = False
        elif quiz_play == "p1":   ##Player made quiz
            p1 = True
            pick_quiz = False
        elif quiz_play == "":   ##To go back to main menu
            pick_quiz = False
        else:
            print("Sorry no quiz under that name. Check spelling.")  ##Error catching
        print() ##For looks
            



    while nz == True:   ##NZ quiz
        print("Type the corresponding letting that you think is correct. e.g. 'a'")
        for num in range(nz_amount_of_question):  ##Constant vairable if i ever want to change the amount of questions NZ quiz cycles through
            print(nz_questions[num])   ##Printing Questions and answer options
                               ##Everything is in a for loop so I can be far more code efficient 
                               ##After each cycle it prints a different part of the list
            nz_1 = input()
            if nz_1 == nz_correct_answer[num]:     ##To check if it the correct options
                print("correct", "\n")
                nz_score += 1
            else:
                print("incorrect, correct answer:", nz_correct_answer[num], "\n")

        print("summary", "\n" "Total Score:", nz_score, "/", nz_amount_of_question)   ##Overall Summary of how the player did
        if nz_score == nz_amount_of_question:
            print("Well Done! Perfect Score!")    ##Depending on the result they get then the summary will be different
        elif nz_score > 6:
            print("Decent Score")
        elif nz_score > 3:
            print("Not Bad")
        elif nz_score > 0:
            print("Better Luck Next Time")
        else:
            print("You Tried")
        nz_score -= nz_score    ##The score subracts it self so the score can reset to zero for the next quiz attempt
        print()
        nz = False




    while p1 == True:  ##PLayer the player made quiz
        try:     ##It's in a try and except statment becasue if there was no player made quiz in a slot then it would crash
            if p1_questions[0] == "":
                print("Sorry, No Quiz Found")    ##If they started making a quiz but canceled
            else:
                print("Type the corresponding answer that you think it is correct. e.g. 'True'")
                for num in range(p1_current_questions):         ##Cycles throug the total amount of questions they made
                    print(p1_questions[num])                  ##Almost the same process as NZ quiz although The question and the option answers are in different slots
                                                      ##This is because I am unable to append the question and the answer option into one part of a list
                    for num in range(4):
                        print(p1_answer[p1_current_answer])
                        p1_current_answer += 1              ##Unable to use num vairable as it does not work for this loop
            
                            
                    Q1_1 = input()

                    if Q1_1 == p1_correct_answer[p1_current_correct_answer]:      ##Checking if the answer is correct
                        print("correct", "\n")
                        p1_score += 1
                    else:
                        print("incorrect, correct answer:", p1_correct_answer[p1_current_correct_answer], "\n") ##Summary
                    p1_current_correct_answer += 1

                print("summary", "\n" "Total Score:", p1_score, "/", p1_current_questions)
                if p1_score == p1_current_questions:
                    print("Well Done! Perfect Score!")
                elif p1_score == 0:
                    print("You Tried")
                else:
                    print("not bad")
                p1_score -= p1_score              ##Vairables subrtacting itself for the next loop
                p1_current_correct_answer -= p1_current_correct_answer
                p1_current_answer -= p1_current_answer
            print()
            p1 = False
        except:
            print("Sorry, No Quiz Found \n")  ##If there is no player made quiz in the slot

            p1 = False
            

        


    while make_overwrite == True:    ##If there is already a player made quiz it will make sure that they don't overite the quiz accedently 
        try:
            if  p1_slot == 1:    ##After making a quiz it will add a number to this slot. ##So next time they try to make a quiz it will detect that there is alreadya quiz in the slot
                print("There is already a player made quiz. Are you sure you want to continue, Doing so will wipe the prevous quiz." "\n" "Type 'yes' to continue or Press Enter to go back to main menu")
                a =input()
            if a == "yes":  ## IF they say yes they would like to overite the slot then it will continue to make a quiz
                make_p1 = True
                make_overwrite = False
            elif a == "":      ##If they so no and that they would like to return to the main menu then it will do so
                make_overwrite = False
            else:
                print("Sorry we don't support that. Please check spelling. \n")  ##Error catching

        except:
            make_p1 = True
            make_overwrite = False  ##if p1_slot is not 1 then there is no quiz slot meaning it will proceed to make the quiz





    while make_p1 == True:
        print("If you don't want all 'abcd' then just press enter on the ones you don't want.", "\n" "Press Enter on what is your ... question to finish making quiz.", "\n")
        p1_questions.clear()  ##Clearing the prevous quizes
        p1_answer.clear()
        p1_correct_answer.clear()

        for num in range(10):
            p1_questions.append(input("What is your question \n"))    ##Repeating the process of making quiz to make code more effient
            if p1_questions[num] == "":
                print()  ##If they want to break the loop
                break
            else:
                p1_current_questions += 1
                p1_correct_answer.append(input("What is the answer to your question \n"))  ##appending the player made quiz
                p1_answer.append(input("a \n"))
                p1_answer.append(input("b \n"))
                p1_answer.append(input("c \n"))
                p1_answer.append(input("d \n"))
                print()
                p1_slot = 1
        make_p1 = False
        

    
        

        
        
        
    
                  
        
        
    



