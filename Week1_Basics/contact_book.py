contacts={}
def add_contact():
    name=input("enter the name : ")
    num=int(input("enter the num : "))
    contacts[name]=num
    print("\n number added successfully")

def search_contact():
    search=input("enter the person name : ")
    if search in contacts:
        print(f"{search} is in contacts")
        print(f"{search}-{contacts[search]}")
    else:
        print(f"{search}is not in the contact book")

def view_contacts():
    if contacts:
        print("\n📖 Contact List:")
        for name, number in contacts.items():
            print(f"{name} → {number}")
    else:
        print("No contacts found.")
def main():
    while True:
        print("\n----contact book----")
        print("1. Add contact")
        print("2. search sontact")
        print("3. view contact")
        print("4. exit")

        choice=int(input("enter the choice : "))

        if choice==1:
            add_contact()
        elif choice==2:
            search_contact()
        elif choice==3:
            view_contacts()
        elif choice==4:
            print("exiting the contact book , goodbye!!")
            break
        else:
            print("invalid input")
main()