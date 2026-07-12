contacts = {}

while True:
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contacts[name] = phone # Adds a key-value pair to a dictionary

    choice = input("Add more? (y/n): ")

    if choice.lower() == "n":
        break

print(contacts)
