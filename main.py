try:
    a=int(input("Enter the first number: "))
    b=int(input("Enter the second number: "))
    print("What opertation do you want to perform.\npress + for addition\npress - for subtraction\npress / for division\npress * for multiplication")

    o=input("Enter operation: ")
    match o:
        case "+":
            print(f"The result is : {a + b}")
        case "-":
            print(f"The result is : {a - b}")
        case "/":
            print(f"The result is : {a / b}")
        case "*":
            print(f"The result is : {a * b}")
        case default:
            print("There was  an error")

except Exception as e:
    print("Enter a valid number")
