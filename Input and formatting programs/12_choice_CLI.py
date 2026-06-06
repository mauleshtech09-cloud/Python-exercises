# Practice Problem: Create a menu that offers three options: “1. Say Hello”, “2. Calculate Square”, and “3. Exit”. The program should perform the action based on the number the user types.

# Exercise Purpose: This is the foundation of “Command Line Interfaces” (CLI). It teaches you how to map user input to specific logic blocks using conditional statements, turning a linear script into an interactive application.

while True:
    choice=int(input("Enter choice between 1-3: "))

    if choice == 1:
        print("Heloo!!")


    elif choice == 2 :
        number=int(input("Enter number to square : "))
        print(f"Square of {number} = {number * number}") 
        
    elif choice == 3:
       print(f"Exiting.........")
       break
       
    else:
        print(f"Invalid choice! , enter between 1, 2 and 3")  