try:
    number = int(input("Enter number: "))
    result = 10 / number
    print(result)
except ValueError:
    print("Invalid number")

except ZeroDivisionError:
    print("Cannot divide by zero")

else:
    print("Trying else")

finally:
    print("End of Program")
