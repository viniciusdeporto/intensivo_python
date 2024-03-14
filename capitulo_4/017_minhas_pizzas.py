my_pizzas = ["peperoni", "portuguesa", "4 queijos", "calabresa"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("bacon")
friend_pizzas.append("margherita")

print("minhas pizzas favoritas são:")
for pizza in my_pizzas:
    my_pizzas = pizza
    print(my_pizzas)

print("\n--------------------------------\n")

print("Pizzas favoritas do meu amigo:")
for f_pizza in friend_pizzas:
    friend_pizzas = f_pizza
    print(friend_pizzas)