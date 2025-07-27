#Write a program to accept marks of 6 students and display them in a sorted manner.
marks = []
#Loop to get marks for 6 students
for i in range(6):
    while True:
        try:
            mark=int(input(f"Enter the marks of Student {i+1}: "))
            marks.append(mark)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

marks.sort()
print("Marks of Students in a sorted order are:", marks)

