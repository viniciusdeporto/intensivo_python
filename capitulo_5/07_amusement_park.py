age = 12
if age < 4:
    price = 0
    # print('Your admission cost is $0')
elif age < 18:
    price = 25
    # print('Your admission cost is $25')
elif age < 65:
    price = 40
    # print('Your admission cost is $25')
elif age >= 65:
# else:
    price = 20
    # print('Your admission cost is $40')

print(f'Your admission cost is ${price}')