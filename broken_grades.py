# Calculating Grades (ok, let me think about this one)

# Write a program that will average 3 numeric exam grades, return an average test score, a corresponding letter grade, and a message stating whether the student is passing.

# Average	Grade
# 90+	A
# 80-89	B
# 70-79	C
# 60-69	D
# 0-59	F

# Exams: 89, 90, 90
# Average: 90
# Grade: A
# Student is passing.

# Exams: 50, 51, 0
# Average: 33
# Grade: F
# Student iis failing.


#fixing all input variables by making it a float input for proper inputs
exam_one = float(input("Input exam grade one: "))

exam_two = float(input("Input exam grade two: "))

exam_three = float(input("Input exam grade three: ")) #changed 'exam_3' to 'exam_three'
# fixed list bt adding commas to the list to separate elements
grades = [exam_one, exam_two, exam_three]

#sum cannot be a variable because it is a keyword so i replace it to 'sum_grade' everytime it shows up in the code
sum_grade = 0
for grade in grades:           #changed grade to 'grades' similar to our list
  sum_grade = sum_grade + grade
#fixed grade typo
avg = sum_grade / len(grades)
#fixed logic values for if statement , fixed string errors , fixed colen error
if avg >= 90:
    letter_grade = "A"
elif avg >= 80 and avg <= 90:
    letter_grade = "B"
elif avg >=70 and avg < 80:
    letter_grade = "C"
elif avg >= 60 and avg < 70:
    letter_grade = "D"
else:                            #changed elif to else
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))
#taking print statements out of loop so it doesnt repeatedy print everytime it loops
print("Average: " + str(avg))

print("Grade: " + letter_grade)
#fixed if statement 
if letter_grade == "F":    #fixed if statement , corrected variable name 
     #fixed print statements by adding '()'
    print ("Student is failing.")
else:
    print ("Student is passing.")
