def Grading(a):
    global Grade
    if a > 79:
        Grade = "A*"
    elif a > 69:
        Grade = "A"
    elif a > 59:
        Grade = "B"
    elif a > 49:
        Grade = "C"
    elif a > 39:
        Grade = "D"
    else:
        Grade = "Fail"

def start():
    global Menu
    Menu = int(input("""Enter 1 to input a grade
Enter 2 to view grades
Enter 3 to exit the programme"""))

start()

while Menu != 3:
    if Menu == 1:
        StudentName = input("Enter student name")
        Date = input("Enter Date")
        Score = int(input("Enter Score"))
        TestName = input("Enter Test Name")
        TutorName = input("Enter Tutor Name")
        Grading(Score)
        with open("StudentData.txt","a")as file:
            file.write("Name:"+StudentName+" ")
            file.write("Date:"+Date+" ")
            file.write("Grade:"+Grade+" ")
            file.write("Test:"+TestName+" ")
            file.write("Tutor:"+TutorName+" ")
            file.write("""
""")
            file.close()
            start()
    elif Menu == 2:
        with open("StudentData.txt","r")as file:
            print(file.read())
            file.close()
        start()
