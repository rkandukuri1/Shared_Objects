try:
    print("")
    print("Choose one of the following operations")

    print("\t1. Addition \n\t2. Substraction \n\t3. Multiplication \n\t4. Division \n\t5. Exit \n")

    opertn = input("\t  Enter your choice: ")

    choices = ["1", "2", "3", "4"]

    if (opertn not in choices):
        print("Un-expected Operation choice, exiting …")
        exit()

    print("")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number:  "))

    print("")

    if opertn == "1":
        print("Addition selected")
        result = num1 + num2

    elif opertn == "2":
        print("Substraction selected")
        result = num1 - num2

    elif opertn == "3":
        print("Multiplication selected")
        result = num1 * num2

    elif opertn == "4":
        print("Division selected")
        result = num1 / num2   

    print(f" \n\t  *** Result: {result} *** ")

except ZeroDivisionError:
    print(f" \n\t  *** Cannot divide by zero *** ")

except ValueError:
    print(f" \n\t  *** Invalid input *** ")

finally:
    print("Done")
