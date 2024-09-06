from QuestionsAndAnswers import *

def StartQuiz(questions):
    score = 0
    for q in questions:
        print(q["question"]) # gets the prompt of the list and show them.
        for option in q["options"]: # iterate over the options for the current question
            print(option) # print the option
        answer = input("Enter your answer (A, B, C, or D), or 0 to exit: ")
        if answer.strip() == "0": # check if the user wants to exit add strip to remove whitespace
            print("Exiting quiz. Goodbye!")
            return
        elif answer.upper() == q["answer"].upper(): # convert both to uppercase for comparison
            print("Correct!\n")
            print("-------------------------------------------\n")
            score += 1
        else:
            print("Wrong Answer, the correct answer is " + q["answer"])
            print("-------------------------------------------\n")

    print("Quiz finished! Your final score is " + str(score) + "/" + str(len(questions)))