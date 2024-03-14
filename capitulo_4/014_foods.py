my_foods = ["pizza", "hamburguer", "frango frito", "batata frita"]
#o sinal de [:] é fatia, é igual copiar, mas uma nao é igual a outra, é possivel adicionar elementos diferentes nos dois

# friend_foods = my_foods[:]
friend_foods = my_foods

my_foods.append("churrasco")

friend_foods.append("sorvete")

print("my favorite foods are:")
print(my_foods)

print("my friend foods:")
print(friend_foods)