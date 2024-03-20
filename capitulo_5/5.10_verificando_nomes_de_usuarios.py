current_users = ['levi', 'guilherme', 'joaquim', 'maria', 'PEDRO', 'homero']
new_users = ['mateus', 'marcos', 'juliana', 'pedro', 'HOMERO']

current_users_lower = [user.lower() for user in current_users]

for new_user in new_users:
    new_user_lower = new_user.lower()
    if new_user_lower in current_users_lower:
        print(f'O nome {new_user} já foi usado')
    else:
        print(f'O nome {new_user} está disponivel!')