# Task 2: CSV Student Logger
# Ask for student name + marks
# Append it to grades.csv
# Then read and show all entries
#


import csv

# Step 1: Ask for student name and marks
name = input("Enter student name: ")
marks = input("Enter student marks: ")

# Step 2: Save to 'grades.csv'
# 'a' means append (add to existing file)
with open("grades.csv", "a", newline="") as file:
    writer = csv.writer(file)

    # If the file is empty, add header
    file.seek(0)
    if file.tell() == 0:
        writer.writerow(["Name", "Marks"])  # header row

    writer.writerow([name, marks])  # data row

print("\n✅ Student record saved!")

# Step 3: Read and print all entries
print("\n📋 All Student Records:")
with open("grades.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)
