def start():
    query=input("Choose one: students_names, student_score, students_count: ")
    if query=="students_names":
        students_names()
    elif query=="student_score":
        student_score()
    elif query=="students_count":
        student_count()
    else:
        print("Enter a valid input")

def q2():
    query2= input("Please type done if you finished, or more for another query: ")
    if query2=="done":
        exit()
    elif query2=="more":
        start()
    else:
        print("Input is not valid")

def students_names():
    class_name=input("Please Enter Class Name: ")
    if class_name=="grade_one":
        print(list(grade_one.keys()))
    elif class_name=="grade_two":
        print(list(grade_two.keys()))
    elif class_name=="grade_three":
        print(list(grade_three.keys()))
    else:
        print("Input is not valid")
    q2()

def student_score():
    class_name=input("Please Enter Class Name: ")
    student_name=input("Please Enter Student Name: ")
    if class_name=="grade_one":
        if student_name in grade_one:
            print (sum(grade_one.get(student_name)))
        else:
            print ("Name not found")
    elif class_name=="grade_two":
        if student_name in grade_two:
            print (sum(grade_two.get(student_name)))
        else:
            print ("Name not found")
    elif class_name=="grade_three":
        if student_name in grade_three:
            print (sum(grade_three.get(student_name)))
        else:
            print ("Name not found")
    else:
        print('Input is not valid')
    q2()

def student_count():
    class_name=input("Please Enter Class Name: ")
    if class_name=="grade_one":
        print(len(grade_one))
    elif class_name=="grade_two":
        print(len(grade_two))
    elif class_name=="grade_three":
        print(len(grade_three))
    else:
        print('Input is not valid')
    q2()
while True:
    start()
