"""

get name
display menu
get choice
while choice != Q
   if choice == H
       display "hello" name
   else if choice == G
       display "goodbye" name
   else
       display invalid message
   display menu
   get choice
display finished message

"""

name = input("Enter name: ")
choice = ""

while choice != 'Q':
    print("(H)ello")
    print("(G)oodbye")
    print("(Q)uit")

    choice = input(">>> ").upper()

    if choice == 'H':
        print("Hello " + name)
    elif choice == 'G':
        print("Goodbye " + name)
    elif choice != 'Q':
        print("Invalid choice")

print("Finished.")
