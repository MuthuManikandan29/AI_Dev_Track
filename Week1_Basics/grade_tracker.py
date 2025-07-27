#  Task 2: Student Grade Tracker
# Ask how many students
#
# Take input of student names and their marks
#
# Store in a dictionary
#
# Calculate and print the average

stud_list={}

stud_count=int(input("enter the count  : "))

def add_mark():
    for i in range(stud_count):
        name=input("enter the name : ")
        marks=int(input("enter the marks : "))
        stud_list[name]=marks
        print(f"\n{name} successfully added")

def calculate_marks():
    if stud_list:
        total=sum(stud_list.values())
        average=total/len(stud_list)
        print(f"\nClass average is: {average:.2f}")
    else:
        print("no data found")

def view_all():
    print("\n---studs marks---")
    for name,marks in stud_list.items():
        print(f"{name}: {marks}")


add_mark()
calculate_marks()
view_all()