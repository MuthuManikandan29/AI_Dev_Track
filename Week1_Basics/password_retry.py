# Task 2: Password Retry System (while loop)
# User gets 3 tries to enter a correct password ("admin123").
# If correct: print "Access Granted"
# If wrong 3 times: "Account locked"


correct_pass="admin123"
count=0
max_attempts=3

while count < max_attempts:
    a=input("enter a pass:")
    if a==correct_pass:
        print("Access Granted")
        break
    else:
        print("Access Denied")
        count+=1
if count==max_attempts:
    print("Account is locked")
