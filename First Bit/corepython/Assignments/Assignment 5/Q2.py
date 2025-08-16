# 2. Enter number of students from user. For those many students accept marks of 5  
#subject marks from user and calculate percentage. Display all percentage and  
#average percentage of students. 
### Enter number of students from user. For those many students accept marks of 5
#   subject marks from user and calculate percentage. Display all percentage and
#   average percentage of students.

student = int(input("Enter the number of student:"))
average = 0
for i in range(1,student + 1):
    print(f"Student marks")
    marks = 0

    for j in range(1,6):
        subject = int(input(f"Enter the marks of subject {j}:"))
        marks = marks + subject
    
    percentage = (marks / 500)*100
    print(f"Percentage of student {i} is {percentage}.")
    average = average + percentage

average_percentage = average / student

print(f"Average percentage of student is {average_percentage}.")
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
    
# Program 2: Calculate percentage of students

num_students = int(input("Enter number of students: "))
total_avg = 0

for i in range(1, num_students + 1):
    print(f"\nEnter marks of 5 subjects for Student {i}:")
    total_marks = 0
    for j in range(1, 6):
        marks = float(input(f"Subject {j} marks: "))
        total_marks += marks
    percentage = total_marks / 5
    total_avg += percentage
    print(f"Percentage of Student {i}: {percentage:.2f}%")

avg_percentage = total_avg / num_students
print(f"\nAverage percentage of all students: {avg_percentage:.2f}%")
