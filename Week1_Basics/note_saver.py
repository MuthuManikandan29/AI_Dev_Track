#  Task 1: File Note Saver
# Ask user to write a note and save it to a file called notes.txt.
# Then read and print all notes saved so far.

note = input("Write your note: ")

with open("notes.txt", "a") as file:
    file.write(note + "\n")

print("\n✅ Note saved successfully!\n")

print("📓 All Notes:")
with open("notes.txt", "r") as file:
    notes = file.readlines()
    for line in notes:
        print("- " + line.strip())
