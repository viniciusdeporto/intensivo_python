# prompt = "\nDigite um ingrediente\n"
# prompt += "Para sair digite quit: "

# active = True
# ingredientes = []
# while active:
#     ingrediente = input(prompt)
#     if ingrediente == 'quit':
#         active = False
#     else:
#         ingredientes.append(ingrediente)


# print(ingredientes)

 





























prompt = '\nDigite um ingrediente na sua pizza,\n'
prompt += 'Para sair digite "quit": '

ingredientes = []
active = True
while active:
    ingrediente = input(prompt)
    if ingrediente.lower() == 'quit':
        active = False
    else:
        ingredientes.append(ingrediente)

print(ingredientes)

