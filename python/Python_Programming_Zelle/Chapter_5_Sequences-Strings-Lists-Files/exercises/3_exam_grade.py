#exam_grade.py

def main():
    examGrade = 999
    while (examGrade != (-1)):
        letter = ["F","D","C","B","A","A"]

        examGrade = eval(input("Enter the exam grade (0-100): "))

        if (examGrade < 0) | (examGrade > 100):
            examGrade = -1
            print("Invalid grade entered")
        else:
            letterGradeIdx = examGrade//10 - 5
            if (letterGradeIdx < 0):
                letterGradeIdx = 0

            print("The exam letter grade is {0}".format(letter[letterGradeIdx]))
main()