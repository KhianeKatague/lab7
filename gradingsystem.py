name = input("Enter your name: ")
section = input("Enter your section:")
prelim = float(input("Enter your prelim grade:"))
midterm = float(input("Enter your midterm grade: "))
finals = float (input("Enter your final grade: "))
grade = (prelim + midterm + finals) /3

if grade <= 40 or grade >= 101:
    print("Error grade not valid")

elif grade >=99:
    print(round(grade),"Excellent your GPA is 1.00!")
elif grade >=96:
    print(round(grade),"Outstanding your GPA is 1.25!")
elif grade >=93:
    print(round(grade),"Superior your GPA is 1.50!")
elif grade >-90:
    print(round(grade),"Very Good your GPA is 1.75!")
elif grade >=87:
    print(round(grade),"Good your GPA is 2.00!")
elif grade >=84:
    print(round(grade),"Satisfactory your GPA is 2.25!")
elif grade >=81:
    print(round(grade),"Fairly Satisfactory your GPA is 2.50!")
elif grade >=78:
    print(round(grade),"Fair your GPA is 2.75!")
elif grade >=75:
    print(round(grade),"Passed your GPA is 3.00!")
elif grade <75:
    print(round(grade),"Failed your GPA is 5.00")

    
