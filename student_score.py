student_score=input("enter the score of the student: ").split()
for i in range(0,len(student_score)):
    student_score[i]=int(student_score[i])
print(student_score)
#total score of the student
total_score=0
for score in student_score:
    total_score+=score

#total number of the subjects
total_subject=0
for subject in student_score:
    total_subject+=1
print(total_subject)
out_off=total_subject*100
print(f"the total score of the student is: {total_score}/{out_off}")
#find the highest mark of the subject
high_mark=0
for mark in student_score:
    if mark > high_mark:
        high_mark=mark;
print(f"the highest mark of the subject is{high_mark}")
#find the lowest mark of the subject
 low_mark=100 
for mark in student_score:
    if mark < low_mark:
        low_mark=mark;
print(f"the highest mark of the subject is{low_mark}")
    

