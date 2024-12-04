import random

pikachu_heald = 80
squirtle_heald = 90

bola_voltio = 10
onda_trueno = 11

placaje = 10
pistola_agua = 12
burbuja = 9


while pikachu_heald > 0 and squirtle_heald > 0:

    print("Turno de pikachu!")
    ataque_pikachu = random.randint(1, 2)
    if ataque_pikachu == 1:
        print("Pikachu ataca con Bola Voltio")
        squirtle_heald -= 10
    else:
        print("Pikachu ataca con Onda Trueno")
        squirtle_heald -= 11

    print("La vida del pikachu es: {}\n La vida de squirtle es: {}".format(pikachu_heald, squirtle_heald))

    input("Enter para continuar...")

    ataque_squirtle = None
    print("Turno de squirtle!")
    while ataque_squirtle != 1 and squirtle_heald != 2 and squirtle_heald != 3:
        ataque_squirtle= int(input("¿Ataque a realizar? [1]Placaje,[2]Pistola, [3]Burbuja?"))

        if ataque_squirtle == 1:
            print("Squirtle ataca con Placaje")
            pikachu_heald -= 10
        elif ataque_squirtle == 2:
            print("Squirtle ataca con Pistola Agua")
            pikachu_heald -= 12
        elif ataque_squirtle == 3:
            print("Squirtle ataca con Burbuja")
            pikachu_heald -= 9

    print("La vida del pikachu es: {}\n La vida de squirtle es: {}".format(pikachu_heald, squirtle_heald))


    input("Enter para continuar...")

    if pikachu_heald == 0:
        print("Squirtle gana!\nPikachu queda fuera de combate.")
    if squirtle_heald == 0:
        print("Pikachu gana!\nSquirtle queda fuera de combate.")