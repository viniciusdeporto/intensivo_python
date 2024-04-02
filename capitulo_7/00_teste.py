height_input = input('How tall are you, in inches or meters? ')
height = float(height_input)

if height >= 48:
    print('\nYou are tall enough to ride.')
else:
    print("\nYou'll be able to ride when you're a little older.")

# Convertendo metros para polegadas
if height < 48:  # Se a altura estiver em metros
    height_inches = height * 39.37  # Converta metros para polegadas
    print(f'\nYour height in inches is approximately {height_inches:.2f}.')
