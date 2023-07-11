import readchar

import os

import random

import time

pos_x = 0

pos_y = 1

map_width = 20

map_height = 15

my_position = [3,1]

trainers = []

#Todo esto para el combate

names = ["Ramón","Luis","Juan","Galio","Jose","Angel","Carlos","Miguel","Pepe"]

pokemon_names = ["Pikachu", "Squirtle", "Charmander", "Venausaur", "Meowth", "Ariados", "Charizard", "Nidoking", "MewTwo"]

pokemon = [95, 80, 105, 85, 120]

final_boss = pokemon_names[-1]

HP = 135

reamining_hp = HP



# Aquí se crean las posiciones de los entrenadores

for i in range(4):

    rng_x = random.randint(1, 20)

    rng_y = random.randint(1, 15)

    trainers.append([rng_x,rng_y])



combat = False

while combat == False:

    os.system("cls")

    if len(trainers) < 1:

        print("\nEnhorabuena! Ganaste la liga Pokemon!")

        exit()

    print("+" + "-" * map_width * 3 + "+")

# Recorremos el mapa para dibujarlo

    for coordinate_y in range(map_height):

        print("|", end="")

        for coordinate_x in range(map_width):

            char_to_draw = " "

# Ponemos a los entrenadores en su posición

            for trainer in trainers:

                if trainer[pos_x] == coordinate_x and trainer[pos_y] == coordinate_y:

                    char_to_draw = "*"

# Combate Pokemon

                    if trainer[pos_x] == my_position[pos_x] and trainer[pos_y] == my_position[pos_y]:

                        who = trainer

                        combat = True

# Posicionamos al jugador

            if coordinate_x == my_position[pos_x] and coordinate_y == my_position[pos_y]:

                char_to_draw = "@"

            print(" {} ".format(char_to_draw), end="")

        print("|")

    print("+" + "-" * map_width * 3 + "+")

#Leemos el teclado para el movimiento

    direction = readchar.readchar()

    if (direction == "w"):

        my_position[pos_y] -= 1

        my_position[pos_y] %= map_height

    elif(direction == "s"):

        my_position[pos_y] += 1

        my_position[pos_y] %= map_height

    elif(direction == "a"):

        my_position[pos_x] -= 1

        my_position[pos_x] %= map_width

    elif(direction == "d"):

        my_position[pos_x] += 1

        my_position[pos_x] %= map_width

    elif(direction == "o"):

        break

# Segunda parte del programa, el combate

    i = random.randint(0,4)

    EHP = pokemon[i]

    e_reamining_hp = EHP

    potions = 2

    while combat != False:

        i = random.randint(0,8)

        print(i)

        print("Te encontraste con {}! Preparate para el combate!".format(names[i]))

        print("Su Pokemon es {} y tiene {} puntos de vida, a por él!".format(pokemon_names[i], EHP))

        enemy = pokemon_names[i]

        choice = True

        while choice:

            if potions > 0:

                choice = input("Selecciona una acción! \n 1. Atacar \n 2. Objeto de curación")

                if choice == "2":

                    potions -= 1

                    reamining_hp = reamining_hp + 30

                    print("Elegiste una poción\n Ahora tu salud es de {}".format(reamining_hp))

            else:

                choice = input("No te quedan pociones, solo puedes atacar :( \n 1. Atacar")

            if choice == "1":

                attack = True

                while attack:

                    attack = input("Selecciona tu ataque\n 1. Impactrueno 2. Onda Voltio 3. Placaje ///Enter -> Salir")

                    if attack == "1":

                        skill = "Impactrueno"

                        i = random.randint(10,30)

                    elif attack == "2":

                        skill = "Onda Voltio"

                        i = random.randint(5,25)

                    elif attack == "3":

                        skill = "Placaje"

                        i = random.randint(0,15)                        

                    else:

                        continue

                    e_reamining_hp = e_reamining_hp - i

                    print("Atacaste con {}, hiciste {} puntos de daño, ahora tu oponente tiene {} puntos de salud\n".format(skill, i, e_reamining_hp))

                    i = random.randint(0,28)

                    reamining_hp -= i

                    print("El {} enemigo atacó, hizo {} puntos de daño, ahora tu {} tiene {} puntos de salud\n".format(enemy, i, pokemon_names[0], reamining_hp))



                   

                    if e_reamining_hp < 1:

                        print("Ganaste este combate! Sigamos")

                        trainers.remove(who)

                        attack = False

                        choice = False

                    elif reamining_hp < 1:

                        print("Perdiste este combate")

                        time.sleep(1)

                        print(".")

                        time.sleep(1.3)

                        print("..\n Llevandote al centro Pokemon más cercano...")

                        attack = False

                        choice = False

                reamining_hp = HP

                               

            else:

                choice = True               

        combat = False