import random

"""
Inputs:
1.- Player's 1 action (1,2 or 3)
2.- Player's 2 action (1,2 or 3)

Process:
1.- Check if both players HP is higher to 0 to start the round
2.- Ask both players their actions
3.- Depending on the selected action, execute a conditional to create the interaction
4.- Check if the reloads or shields are greater than 0 to set them to 0 
5.- Continue the rounds until a player's hp becomes 0 or lower

Outputs:
1.- Display the rules, the interactions and the controls
2.- Display of the current players turn, current round and their stats(quantity of bullets and shield)
3.- Display a message if a player shoots without bullets
4.- If a player HP becomes 0 or lower, display a winning message for the winner
"""

#Variable Control
reload1 = 0
shield1 = 0
hp1 = 100
reload2 = 0
shield2 = 0
hp2 = 100
round_count = 1

#Effects that last more than one round  
efectos = {
    "skip1": False, 
    "skip2": False,        
    "cancel1": False,
    "cancel2": False,    
    "reflect1": False,
    "reflect2": False,  
    "free1": False,
    "free2": False,        
    "inv1": False,
    "inv2": False           
}

#Function that prints "----" for the menus
def barrerita():
    print("-------------------------------")

#Menu function with only text
def menu():
    print("Hello, welcome to VA-QUE-RI-TOS")
    barrerita()
    print("The rules are simple, each player has three actions:")
    print("- Reload (1): to reload your gun. If you have 0 bullets, you can't shoot.")
    print("- Shield (2): to protect yourself from other players' attacks.")
    print("- Shoot (3): to attack players.")
    print("Maximum 3 reloads or 3 shields stored. Excess sets them to 0.")
    print("If you are shot without a shield, you lose!")
    barrerita()

#Main function that calls menu and gameplay
def main():
    menu()
    selection = int(input("Please enter (1) for normal mode, or (2) for powers mode: "))
    if selection == 1:
        gameplay()
    elif selection == 2:
        s_gameplay()
    else:
        print("Please enter (1) for normal mode, or (2) for powers mode: ")
        selection = int(input("Please enter (1) for normal mode, or (2) for powers mode: "))


#Gameplay and codes for normal mode

#Gameplay function
def gameplay():
    r1, s1, h1 = reload1, shield1, hp1
    r2, s2, h2 = reload2, shield2, hp2
    r_count = round_count

    while h1 > 0 and h2 > 0:
        print("\n--- ROUND", r_count, "---")
        print("Player 1 -> Bullets:", r1, "| Shields:", s1, "| HP:", h1)
        print("Player 2 -> Bullets:", r2, "| Shields:", s2, "| HP:", h2)
        
        r1, s1, h1, r2, s2, h2, r_count = game_action(r1, s1, h1, r2, s2, h2, r_count)
        barrerita()

    display(h1, h2)
#Game_action funtion for the actions of each player
def game_action(reload1, shield1, hp1, reload2, shield2, hp2, round_count):
    action1 = int(input("Player 1 (1: Reload, 2: Shield, 3: Shoot): "))
    action2 = int(input("Player 2 (1: Reload, 2: Shield, 3: Shoot): "))
    if action1 < 1 or action1 > 3 and action2 < 1 or action2 >3:
        print("Please enter your action (1,2 or 3)")
        action1 = int(input("Player 1 (1: Reload, 2: Shield, 3: Shoot): "))
        action2 = int(input("Player 2 (1: Reload, 2: Shield, 3: Shoot): "))
    
    
    shot1 = False
    if action1 == 1:
        reload1 += 1
    elif action1 == 2:
        shield1 += 1
    elif action1 == 3:
        if reload1 > 0:
            reload1 -= 1
            shot1 = True
        else:
            print("Player 1 tried to shoot without bullets!")

    shot2 = False
    if action2 == 1:
        reload2 += 1
    elif action2 == 2:
        shield2 += 1
    elif action2 == 3:
        if reload2 > 0:
            reload2 -= 1
            shot2 = True
        else:
            print("Player 2 tried to shoot without bullets!")

    #Stablish limits to actions for a fair game
    if shield1 > 3:
        shield1 = 0
    if reload1 > 3:
        reload1 = 0
    if shield2 > 3:
        shield2 = 0
    if reload2 > 3:
        reload2 = 0

    #Actions interactions
    if shot1:
        if shield2 > 0:
            print("Player 2 blocked Player 1's shot!")
            shield2 -= 1
        else:
            print("Player 1 shot Player 2!")
            hp2 = 0

    if shot2:
        if shield1 > 0:
            print("Player 1 blocked Player 2's shot!")
            shield1 -= 1
        else:
            print("Player 2 shot Player 1!")
            hp1 = 0

    round_count += 1
    #Return the updated parameters
    return reload1, shield1, hp1, reload2, shield2, hp2, round_count

#Display function for the end of the game
def display(hp1, hp2):
    barrerita()
    if hp1 <= 0 and hp2 <= 0:
        print("It's a draw! Both players were eliminated.")
    elif hp1 <= 0:
        print("Player 2 Wins!")
    elif hp2 <= 0:
        print("Player 1 Wins!")

#Special mode functions

#Special abilities 
def habilities():
    habilidades = {
        1: "White album (Double Shield)", #Double shield
        2: "Sex pistols (Double shot)", #Doble disparo
        3: "Hol horse (Double reload)",   #Doble recarga
        4: "Mountain tim (Steal a shield from the other player)", #Roba un escudo
        5: "King crimson (Gives you a free turn shield)", #Esquiva bala(escudo gratis)   
        6: "C moon (The opponent's next shot will now be directed to itself)", #El oponente "sin querer" se autodispara en el proximo tiro
        7: "Metallica (The opponents shot will be cancelled)", #El próximo tiro del oponente será anulado
        8: "The World (The opponent can't action next turn)", #El oponente no puede jugar el siguiente turno
        9: "Killer queen (Eliminates all the opponents shields)", #Elimina todos los escudos guardados del oponente
        10: "Kars (Become invincible for 1 turn)" #EL jugador se hace invencible por un turno
    }

    #Lists that hold powers for each player

    player1_powers = []
    player2_powers = []

    return player1_powers,player2_powers,habilidades

    

"""
    for i in range(10):
        x = lista.append(random.randint(0-10))
        y = lista.find(x)
        if y == True:
            lista.pop()
        elif y == False: 
            pass
        """

#Function to display powewrs name
def nombres_poderes(powers, habilidades):
    nombres = []
    for p in powers:
        nombres.append(habilidades[p].split(" (")[0])
    return nombres

#This function askes the player if he wants to use a power
def elegir_poder(num, powers, habilidades):
    if len(powers) == 0:
        return 0
    print(f"Player {num} powers:")
    for i in range(len(powers)):
        print(f"  {i + 1}) {habilidades[powers[i]]}")
    opcion = int(input(f"Player {num}, use a power? (0 = none, or its number): "))
    while opcion < 0 or opcion > len(powers):
        opcion = int(input("Invalid option, try again: "))
    if opcion == 0:
        return 0
    return powers[opcion - 1]

#King Crimson and KArs interaction special function
def impacto(shield, hp, atacante, defensor, invencible, libre):
    if invencible:
        print(f"Player {defensor} is invincible! The shot had no effect.")
    elif libre:
        print(f"Player {defensor} dodged Player {atacante}'s shot with the free shield!")
        libre = False
    elif shield > 0:
        print(f"Player {defensor} blocked Player {atacante}'s shot!")
        shield -= 1
    else:
        print(f"Player {atacante} shot Player {defensor}!")
        hp = 0
    return shield, hp, libre

#Special gameplay funtion
def s_gameplay():
    r1, s1, h1 = reload1, shield1, hp1
    r2, s2, h2 = reload2, shield2, hp2
    r_count = round_count
    player1_powers, player2_powers, habilidades = habilities()   

    while h1 > 0 and h2 > 0:
        
        player1_powers, player2_powers = hab_ver(r_count, player1_powers, player2_powers)

        print("\n--- ROUND", r_count, "---")
        print("Player 1 -> Bullets:", r1, "| Shields:", s1, "| HP:", h1)
        print(f"Player 1 powers: {nombres_poderes(player1_powers, habilidades)}")
        print("Player 2 -> Bullets:", r2, "| Shields:", s2, "| HP:", h2)
        print(f"Player 2 powers: {nombres_poderes(player2_powers, habilidades)}")
        
        r1, s1, h1, r2, s2, h2, r_count, player1_powers, player2_powers, habilidades = s_game_action(r1, s1, h1, r2, s2, h2, r_count, player1_powers, player2_powers, habilidades)
        barrerita()

    display(h1, h2)  

#This sections gives each player a power every 3 turns and verifies that nobody has more than three powers, else, the first power in their power llist will be rmoved
def hab_ver(r_count,player1_powers,player2_powers):

    if r_count % 3 == 0:
        for i in range(2):
            x = random.randint(1, 10)
            if x not in player1_powers:
                player1_powers.append(x)
        for i in range(2):
            x = random.randint(1, 10)
            if x not in player2_powers:
                player2_powers.append(x)
    while len(player1_powers) > 2:
        player1_powers.pop(0)
    while len(player2_powers) > 2:
        player2_powers.pop(0)
    return player1_powers,player2_powers

def s_game_action(reload1, shield1, hp1, reload2, shield2, hp2, r_count,player1_powers,player2_powers,habilidades):
    
    #This part is just like the normal mode gemaplay part
    if efectos["skip1"]: #This verifies if The World habilitie is used on player1
        print("Player 1 is frozen by The World and can't act this turn!")
        efectos["skip1"] = False
        action1 = 0
        power1 = 0
    else:
        action1 = int(input("Player 1 (1: Reload, 2: Shield, 3: Shoot): "))
        while action1 < 1 or action1 > 3:
            action1 = int(input("Please enter your action (1,2 or 3): "))
        power1 = elegir_poder(1, player1_powers, habilidades)   

    if efectos["skip2"]: #This verifies if The World habilitie is used on player2
        print("Player 2 is frozen by Star platinum and can't act this turn!")
        efectos["skip2"] = False
        action2 = 0
        power2 = 0
    else:
        action2 = int(input("Player 2 (1: Reload, 2: Shield, 3: Shoot): "))
        while action2 < 1 or action2 > 3:
            action2 = int(input("Please enter your action (1,2 or 3): "))
        power2 = elegir_poder(2, player2_powers, habilidades)   
    
    
    shot1 = False
    disparos1 = 1   #QUantity of shots added for the Sex Pistols power
    if action1 == 1:
        reload1 += 1
    elif action1 == 2:
        shield1 += 1
    elif action1 == 3:
        if reload1 > 0:
            reload1 -= 1
            shot1 = True
        else:
            print("Player 1 tried to shoot without bullets!")

    shot2 = False
    disparos2 = 1
    if action2 == 1:
        reload2 += 1
    elif action2 == 2:
        shield2 += 1
    elif action2 == 3:
        if reload2 > 0:
            reload2 -= 1
            shot2 = True
        else:
            print("Player 2 tried to shoot without bullets!")

    #Powers action
    if power1 != 0:
        player1_powers.remove(power1)
        print(f"Player 1 used {habilidades[power1].split(' (')[0]}!")
        if power1 == 1:
            shield1 += 2
        elif power1 == 2:
            shot1 = True
            disparos1 = 2
        elif power1 == 3:
            reload1 += 2
        elif power1 == 4:
            if shield2 > 0:
                shield2 -= 1
                shield1 += 1
            else:
                print("Player 2 has no shields to steal.")
        elif power1 == 5:
            efectos["free1"] = True
        elif power1 == 6:
            efectos["reflect2"] = True
        elif power1 == 7:
            efectos["cancel2"] = True
        elif power1 == 8:
            efectos["skip2"] = True
        elif power1 == 9:
            shield2 = 0
        elif power1 == 10:
            efectos["inv1"] = True

    if power2 != 0:
        player2_powers.remove(power2)
        print(f"Player 2 used {habilidades[power2].split(' (')[0]}!")
        if power2 == 1:
            shield2 += 2
        elif power2 == 2:
            shot2 = True
            disparos2 = 2
        elif power2 == 3:
            reload2 += 2
        elif power2 == 4:
            if shield1 > 0:
                shield1 -= 1
                shield2 += 1
            else:
                print("Player 1 has no shields to steal.")
        elif power2 == 5:
            efectos["free2"] = True
        elif power2 == 6:
            efectos["reflect1"] = True
        elif power2 == 7:
            efectos["cancel1"] = True
        elif power2 == 8:
            efectos["skip1"] = True
        elif power2 == 9:
            shield1 = 0
        elif power2 == 10:
            efectos["inv2"] = True

    #Stablish limits to actions for a "fair" game
    if shield1 > 3:
        shield1 = 0
    if reload1 > 3:
        reload1 = 0
    if shield2 > 3:
        shield2 = 0
    if reload2 > 3:
        reload2 = 0

    #Actions interactions updated with habilities
    if shot1:
        if efectos["cancel1"]:
            print("Player 1's shot was cancelled by Metallica!")
            efectos["cancel1"] = False
        else:
            destino = 2
            if efectos["reflect1"]:
                print("C moon redirected Player 1's shot to himself!")
                efectos["reflect1"] = False
                destino = 1
            for i in range(disparos1):
                if destino == 2:
                    shield2, hp2, efectos["free2"] = impacto(shield2, hp2, 1, 2, efectos["inv2"], efectos["free2"])
                else:
                    shield1, hp1, efectos["free1"] = impacto(shield1, hp1, 1, 1, efectos["inv1"], efectos["free1"])

    if shot2:
        if efectos["cancel2"]:
            print("Player 2's shot was cancelled by Metallica!")
            efectos["cancel2"] = False
        else:
            destino = 1
            if efectos["reflect2"]:
                print("C moon redirected Player 2's shot to himself!")
                efectos["reflect2"] = False
                destino = 2
            for i in range(disparos2):
                if destino == 1:
                    shield1, hp1, efectos["free1"] = impacto(shield1, hp1, 2, 1, efectos["inv1"], efectos["free1"])
                else:
                    shield2, hp2, efectos["free2"] = impacto(shield2, hp2, 2, 2, efectos["inv2"], efectos["free2"])

    #One turn for kars and Crimson
    efectos["inv1"] = False
    efectos["inv2"] = False
    efectos["free1"] = False
    efectos["free2"] = False

    r_count += 1   
    #Return the updated parameters
    return reload1, shield1, hp1, reload2, shield2, hp2, r_count, player1_powers, player2_powers, habilidades

#Call main
main()