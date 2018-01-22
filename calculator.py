def add(a, b) :
    return a+b

def sub(a, b) :
    return a-b

def mul(a, b) :
    return a*b

def div(a, b) :
    return a/b

def main():

    flag = True
    
    while(flag):
        
        print("\n\tMain Menu\n")
        print("a: Addition(+)\n")
        print("b: Subtraction(-)\n")
        print("c: Multiplication(*)\n")
        print("d: Division(\)\n")
        print("x: Quit\n")
        option = raw_input("Select an option: ")
        
        if(option == "X" or option == "x"):
            flag = False
        else:
            number1 = int(input("\nEnter First Number: "))
            number2 = int(input("Enter Second Number: "))

        if(option == "A" or option == "a"):
            print("Answer is: {}".format(add(number1, number2)))
        elif(option == "B" or option == "b"):
            print("Answer is: {}".format(sub(number1, number2)))
        elif(option == "C" or option == "c"):
            print("Answer is: {}".format(mul(number1, number2)))
        elif(option == "D" or option == "d"):
            print("Answer is: {}".format(div(number1, number2)))
        elif(option == "X" or option == "x"):
            flag = False
        else:
            print("Invalid option entered!!")

        raw_input("Press Enter to continue...")

if __name__ == "__main__":
    main()
