def greet_users(names):
    for name in names:
        msg = f"Hello, {name.title()}!"
        print(msg)

usernames = ['vinicius', 'maiara', 'darci']
greet_users(usernames)


