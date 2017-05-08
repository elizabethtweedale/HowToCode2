# Teacher Quiz - Python Code - Elizabeth Tweedale

import csv, random

def askName():                                                              # askName function returns the name of the student
    print("Welcome to the Super Python Quiz!")
    yourName = input("What is your name? ")
    print ("Hello",str(yourName))
    return yourName

def getQuestions():                                                         # getQuestions reads in the questions from a CSV file
    questions = []                                                          # this creates an empty list for adding the questions to
    with open("SuperPythonQuiz.csv", mode="r", encoding="utf-8") as myFile:
        myQuiz = csv.reader(myFile)
        for row in myQuiz:
            questions.append(row)
    return questions

def askQuestion(question,score):                                            # askQuestion prints the question and choices to the screen then checks the answer
    print(question[0])                                                      # print the question - this is in the [0] position of the row
    for eachChoice in question[1:-1]:                                       # print each choice from [1] to the last position [-1]
        print("{0:>5}{1}".format("", eachChoice))
    answer = input("Please select an answer: ")                             # get the student's answer
    if answer == question[-1]:                                              # check if the answer matches the last position in the question, the correct answer
        print("Correct!")                                                   # if it's correct, tell the user and add one to the score
        score += 1
    else:                                                                   # if it's incorrect, tell the user what the correct answer was
        print("Incorrect, the correct answer was {0}.".format(question[-1]))
    return score                                                            # return the score

def recordScore(studentName, score):
    with open("QuizResults.txt", mode="a+",encoding="utf-8") as myFile:     # note the '+' sign after the a means if the file does not exist, then create it
        myFile.write(str(studentName) + "," + str(score) + "\n")            # write name,score to the file
                                                                            # "\n" will add a new line to the file so that it's ready for the next name
def main():
    studentName = askName()                                                 # call the askName function
    questions = getQuestions()                                              # call the getQuestions function
    score = 0                                                               # initialise the score to 0

    number = len(questions)                         # use the number to keep track of the total number of questions - which is the length of the 'questions' list
    for eachQuestion in range(number):              # reppeat for each question
        question = random.choice(questions)         # choose a random question from the questions list
        score = askQuestion(question,score)         # ask the question and update the score
        questions.remove(question)                  # remove the current question from the list so that you don't ask it again

    print("Your final score is:", score, "out of:", number)                 # tell the user what their final score is
    recordScore(studentName, score)                                         # call the recordScore function
    
main()
