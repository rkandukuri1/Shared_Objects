import ollama

user_prompt = input("Enter a prompt: ")

result = ollama.generate(
    model="gemma3:1b",
    prompt = user_prompt
)

print (result.response)