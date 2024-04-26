def make_sandwich(*ingredientes):
    print('faça um sanduiche com esse ingrediente: ')
    for ingrediente in ingredientes:
        print(f"\t{ingrediente} ")
        
        
make_sandwich('frango crispy')
make_sandwich('queijo')
make_sandwich('molho de pimenta')