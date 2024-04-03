prompt = "\nEnter 'quit' to end the program."
prompt += '\nTell me something, and i will repeat it back to you: '

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)