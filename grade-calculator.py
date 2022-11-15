# Ask the user to prompt all his result in the following subject
History_grade = int(input("Please enter your math score:  "))
biology_grade = int(input("Please enter your biology score:  "))
chemistry_grade = int(input("Please enter your chemistry score:  "))
math_grade = int(input("Please enter your sociology score:  "))
physics_grade = int(input("Please enter your physics score:  "))


total_grade = History_grade + biology_grade + chemistry_grade + math_grade + physics_grade   #  the total grade
count = 5     # Add the number of subject 

average_grade = total_grade / count  # divide the total_grade by the number of subject to have  the total in 100

print(f"the average of all the grade is {average_grade}")
if average_grade > 90:
    print(f"You have A".format(average_grade))

if average_grade < 90 and average_grade > 80 :
    print(f"You have B".format(average_grade))

if average_grade < 80 and average_grade > 70 :
    print(f"You have C".format(average_grade))

if average_grade < 70 and average_grade > 60 :
    print(f"You have D".format(average_grade))

if average_grade < 60 :
    print(f"Sorry you have Failed ".format(average_grade))
