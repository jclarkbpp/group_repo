from calc import add, divide, multiply, subtract

repeat = True
while repeat == True:  
    user_input1 = int(input("Input Nunber 1: "))
    user_input2 = int(input("Input Number 2: "))
    operation1 = input("Input operation (+-*/): ")
    try: 
        if operation1 == "+":
            print(f"{user_input1} + {user_input2} = {add(user_input1, user_input2)}")
        elif operation1 == "-":
            print(f"{user_input1} - {user_input2} = {subtract(user_input1, user_input2)}")
        elif operation1 == "*":
            print(f"{user_input1} * {user_input2} = {multiply(user_input1, user_input2)}")
        elif operation1 == "/":
            print(f"{user_input1} / {user_input2} = {divide(user_input1, user_input2)}")
        
        user = input("Want do another caluculation? y/n")
        if user == "n":
            repeat = False
    except:
        user = input("Invalid operation: Want to try again? y/n")
        if user == "n":
            repeat = False
            break