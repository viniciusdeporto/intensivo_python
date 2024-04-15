def describe_pet(pet_name, animal_type='dog'):
    '''Exibe as informações sobre um animal de estimação'''
    print(f'\nI have a {animal_type}.')
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='bob')

describe_pet(pet_name='stuart', animal_type='hamster')