

while(True):
    print("    Number Representation Converter     ")
    print("----------------------------------------")
    print("A. Binary to Others")
    print("B. Decimal to Others")
    print("C. Octal to Others")
    print("D. Hexadecimal to Others")
    print("X. Exit")

    choice=input("Enter Your Choice : ")
    if(choice=='A'):
        print("1. Binary to Decimal")
        print("2. Binary to Octal")
        print("3. Binary to Hexadecimal")
        print("0. Exit")

        choice1=input("Choose any Option : ")

        if(choice1=='1'):
            binary_number=int(input("Enter Binary Number : "))

        elif(choice1=='2'):
            binary_number=input("Enter Binary Number : ")
        elif(choice1=='3'):
            binary_number=input("Enter Binary Number : ")
        elif(choice1=='0'):
            exit()
        else:
            print("Wrong Choice!!!")

    elif(choice=='B'):
        print("1. Decimal to Binary")
        print("2. Decimal to Octal")
        print("3. Decimal to Hexadecimal")
        print("0. Exit")

        while(True):
            choice2=input("Choose any Option : ")
            if(choice2=='1'):
                binary_number=input("Enter Decimal Number : ")
            elif(choice2=='2'):
                binary_number=input("Enter Decimal Number : ")
            elif(choice2=='3'):
                binary_number=input("Enter Decimal Number : ")
            elif(choice2=='0'):
                exit()
            else:
                print("Wrong Choice!!!")

    elif(choice=='C'):
        print("1. Octal to Binary")
        print("2. Octal to Decimal")
        print("3. Octal to Hexadecimal")
        print("0. Exit")

        while(True):
            choice3=input("Choose any Option : ")
            if(choice3=='1'):
                binary_number=input("Enter Binary Number : ")
            elif(choice3=='2'):
                binary_number=input("Enter Binary Number : ")
            elif(choice3=='3'):
                binary_number=input("Enter Binary Number : ")
            elif(choice3=='0'):
                exit()
            else:
                print("Wrong Choice!!!")
    
    elif(choice=='D'):
        print("1. Hexadecimal to Binary")
        print("2. Hexadecimal to Decimal")
        print("3. Hexadecimal to Octal")
        print("0. Exit")

        while(True):
            choice4=input("Choose any Option : ")
            if(choice4=='1'):
                binary_number=input("Enter Binary Number : ")
            elif(choice4=='2'):
                binary_number=input("Enter Binary Number : ")
            elif(choice4=='3'):
                binary_number=input("Enter Binary Number : ")
            elif(choice4=='0'):
                exit()
            else:
                print("Wrong Choice!!!")

    elif(choice=='X'):
        print("Let's Exit")
        exit(0)

    else:
        print("Wrong Choice!!")

