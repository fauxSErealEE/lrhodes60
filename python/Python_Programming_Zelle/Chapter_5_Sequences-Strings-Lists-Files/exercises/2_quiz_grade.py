#grade.py

def main():
    quizGrade = 999
    while (quizGrade != (-1)):
        letter = ["F","F","D","C","B","A"]

        quizGrade = eval(input("Enter the quiz grade (0-5): "))

        if (quizGrade < 0) | (quizGrade > 5):
            quizGrade = -1
            print("Invalid letter grade")
        else:
            print("The letter grade is {0}-{1}".format(quizGrade,letter[quizGrade]))

main()