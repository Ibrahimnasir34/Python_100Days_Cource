# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆

add=0
#Write your code below this row 👇
numberofStudents=0
for students in student_heights:
  add=add+students
  numberofStudents+=1

print(add)
print("THE NUMBER OF STUDENTS ARE")
print(numberofStudents)
print("THE  AVERAGE HEIGHT OF STUDENTS IS :")
print(round(add/numberofStudents))