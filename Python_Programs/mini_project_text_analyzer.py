text = input("Enter text: ")

print(f"Charactaers: {len(text)}")

words = text.split()

print(f"Words: {len(words)}")

print(f"Uppercase: {text.upper()}")

search = input("Enter word to search: ")

if search in text:
    print("Word found")
else:
    print("Word not found")
