# Task 3: CSV Search Tool
# Ask for a name
# Search it inside grades.csv
# If found, show grade
# If not, print “Not found”

import csv

# Step 1: Ask for a name to search
search_name = input("Enter student name to search: ")

# Step 2: Open grades.csv and search
found = False

with open("grades.csv", "r") as file:
    reader = csv.reader(file)
    for row in reader:
        # Skip the header row
        if row[0] == "Name":
            continue

        if row[0].lower() == search_name.lower():
            print(f"✅ Found! {row[0]}'s Marks: {row[1]}")
            found = True
            break

if not found:
    print("❌ Not found")
