import random
# Assignment: Scores and Grades
# Write a function that generates ten scores between 60 and 100. Each time a score is generated, your function should display what the grade is for a particular score. Here is the grade table:


def schores_grades():
    score = random.randint(60, 101)

    grade = "Scores and Grades"
    print grade
    if(random_num >= 60 and random_num <= 69):
        print "Score: " + str(random_num) + " ;" + " Your grade is D"
    if(random_num >= 70 and random_num <= 79):
        print "Score: " + str(random_num) + " ;" + " Your grade is C"
    if(random_num >= 80 and random_num <= 89):
        print "Score: " + str(random_num) + " ;" + " Your grade is B"
    if(random_num >= 90 and random_num <= 100):
        print "Score: " + str(random_num) + " ;" + " Your grade is A"


schores_grades()
