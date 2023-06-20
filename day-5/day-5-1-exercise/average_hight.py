# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
sum_student =0
count = 0
for student_height in student_heights:
  sum_student += student_height
  count +=1

average_student= sum_student/count

print(round(average_student))

