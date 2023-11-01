# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

n=0
w=0
for n in student_scores:
  n=max(student_scores)
  w=min(student_scores)


print(f"The maximum number in students score is  {n}")
print(f"The minimum number in student scores is {w}")
highest_score=0
low=100
for score in student_scores:
  if score>highest_score:
    highest_score=score
  if score < low:
    low = score


print(f"The highest score in class is :{highest_score}")
print(f"The lowest score in class is :{low}")


