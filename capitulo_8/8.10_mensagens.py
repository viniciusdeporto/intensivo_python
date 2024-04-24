mensagens = ["Nada é permanente, exceto a mudança", "O ser é e o não-ser não é.", "Só sei que nada sei.", "Uma vida sem reflexão não vale a pena ser vivida."]
mensagens_passadas = []

def passar_mensagens(mensagens, mensagens_passadas):
    while mensagens:
        mensagens_atualizadas = mensagens.pop()
        print(f"{mensagens_atualizadas}")
        mensagens_passadas.append(mensagens_atualizadas)


# print("---------")
# for msg in mensagens_passadas:
#     print(msg)

passar_mensagens(mensagens, mensagens_passadas)

print(f"Começou cheia terminou vazia: {mensagens}")
print(f"Começou vazia e terminou cheia: {mensagens_passadas}")

