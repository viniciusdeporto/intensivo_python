prompt = '\nEnter "quit" to end the program.'
prompt += '\nTell me something, and i will repeat it back to you: '


active = True
while active:
    message = input(prompt)

    if message == 'quit':
        active = False
        print('Game Over')
else:
    print(message)