## defining possibilities to user and keeping the whole program in a while loop for the purpose of running repeatedly:

while True:
    print("Select operation.")
    print("1.Addition      : + ")
    print("2.Subtraction : - ")
    print("3.Multiplication : * ")
    print("4.Division   : / ")
    print("5.Terminate: # ")
    
    ## asking for the choice of user and inserting break in loop in the condition of terminating the program:
    choice = input("Enter Your Choice From Given Signs: (+, -, *, /, #)\n")
    if choice == "#":
        print("Terminated!")
        break

    ## asking the numbers from the user: 
    num1 = float(input("Enter The 1st Number  :\n"))
    num2 = float(input("Enter The 2nd Number :\n"))

    ## applying conditions in the situation of selecting(+, -, *, /) by the user:
    if choice == "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    elif choice == "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    elif choice == "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    elif choice == "/":
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Invalid Choice!")

    #adding some space after running program once:  
    print("\n")