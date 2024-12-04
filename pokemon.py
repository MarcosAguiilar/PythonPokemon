import random

PIKACHU_VIDA_INICIAL = 80
SQUIRTLE_VIDA_INICIAL = 90

pikachu_vida_actual = PIKACHU_VIDA_INICIAL
squirtle_vida_actual = SQUIRTLE_VIDA_INICIAL

while pikachu_vida_actual > 0 and squirtle_vida_actual > 0:


    print("Turno de pikachu!")
    ataque_pikachu = random.randint(1, 2)
    if ataque_pikachu == 1:
        print("Pikachu ataca con Bola Voltio")
        squirtle_vida_actual -= 10
    else:
        print("Pikachu ataca con Onda Trueno")
        squirtle_vida_actual -= 11

    barra_de_vida_pikachu = int(pikachu_vida_actual * 10 / PIKACHU_VIDA_INICIAL)
    print("Pikachu  {}hp [{}{}] ".format(pikachu_vida_actual, "#" * barra_de_vida_pikachu,
                                       " " * (10 - barra_de_vida_pikachu)))

    barra_de_vida_squirtle = int(squirtle_vida_actual * 10 / SQUIRTLE_VIDA_INICIAL)
    print("Squirtle  {}hp [{}{}]".format(squirtle_vida_actual, "#" * barra_de_vida_squirtle,
                                       " " * (10 - barra_de_vida_squirtle)))

    if pikachu_vida_actual <= 0:
        print("Squirtle gana!\nPikachu queda fuera de combate.")

        barra_de_vida_pikachu = int(pikachu_vida_actual * 10 / PIKACHU_VIDA_INICIAL)
        print("Pikachu  0hp [{}{}] ".format("#" * barra_de_vida_pikachu,
                                            " " * (10 - barra_de_vida_pikachu)))

        barra_de_vida_squirtle = int(squirtle_vida_actual * 10 / SQUIRTLE_VIDA_INICIAL)
        print("Squirtle  {}hp [{}{}]".format(squirtle_vida_actual, "#" * barra_de_vida_squirtle,
                                             " " * (10 - barra_de_vida_squirtle)))
        break
    if squirtle_vida_actual <= 0:
        print("Pikachu gana!\nSquirtle queda fuera de combate.")

        barra_de_vida_pikachu = int(pikachu_vida_actual * 10 / PIKACHU_VIDA_INICIAL)
        print("Pikachu  {}hp [{}{}] ".format(pikachu_vida_actual, "#" * barra_de_vida_pikachu,
                                             " " * (10 - barra_de_vida_pikachu)))

        barra_de_vida_squirtle = int(squirtle_vida_actual * 10 / SQUIRTLE_VIDA_INICIAL)
        print("Squirtle  0hp [{}{}]".format("#" * barra_de_vida_squirtle, " " * (10 - barra_de_vida_squirtle)))
        break
    input("Enter para continuar...")

    print("\n")

    ataque_squirtle = None
    print("Turno de squirtle!")
    while ataque_squirtle != "1" and ataque_squirtle != "2" and ataque_squirtle!= "3":
        ataque_squirtle= input("¿Ataque a realizar? [1]Placaje,[2]Pistola, [3]Burbuja?")

        if ataque_squirtle == "1":
            print("Squirtle ataca con Placaje")
            pikachu_vida_actual -= 10
        elif ataque_squirtle == "2":
            print("Squirtle ataca con Pistola Agua")
            pikachu_vida_actual -= 12
        elif ataque_squirtle == "3":
            print("Squirtle ataca con Burbuja")
            pikachu_vida_actual -= 9

    if pikachu_vida_actual <= 0:
        print("Squirtle gana!\nPikachu queda fuera de combate.")

        barra_de_vida_pikachu = int(pikachu_vida_actual * 10 / PIKACHU_VIDA_INICIAL)
        print("Pikachu  0hp [{}{}] ".format( "#" * barra_de_vida_pikachu,
                                             " " * (10 - barra_de_vida_pikachu)))

        barra_de_vida_squirtle = int(squirtle_vida_actual * 10 / SQUIRTLE_VIDA_INICIAL)
        print("Squirtle  {}hp [{}{}]".format(squirtle_vida_actual, "#" * barra_de_vida_squirtle,
                                             " " * (10 - barra_de_vida_squirtle)))
        break
    if squirtle_vida_actual <= 0:
        print("Pikachu gana!\nSquirtle queda fuera de combate.")

        barra_de_vida_pikachu = int(pikachu_vida_actual * 10 / PIKACHU_VIDA_INICIAL)
        print("Pikachu  {}hp [{}{}] ".format(pikachu_vida_actual, "#" * barra_de_vida_pikachu,
                                             " " * (10 - barra_de_vida_pikachu)))

        barra_de_vida_squirtle = int(squirtle_vida_actual * 10 / SQUIRTLE_VIDA_INICIAL)
        print("Squirtle  0hp [{}{}]".format("#" * barra_de_vida_squirtle, " " * (10 - barra_de_vida_squirtle)))
        break

    barra_de_vida_pikachu = int(pikachu_vida_actual * 10 / PIKACHU_VIDA_INICIAL)
    print("Pikachu  {}hp [{}{}] ".format(pikachu_vida_actual, "#" * barra_de_vida_pikachu,
                                         " " * (10 - barra_de_vida_pikachu)))

    barra_de_vida_squirtle = int(squirtle_vida_actual * 10 / SQUIRTLE_VIDA_INICIAL)
    print("Squirtle  {}hp [{}{}]".format(squirtle_vida_actual, "#" * barra_de_vida_squirtle,
                                         " " * (10 - barra_de_vida_squirtle)))

    input("Enter para continuar...")
    print("\n")



