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

#barrerita para que se vea chido
def barrerita():
    print("-------------------------------")

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

def main():
    menu()
    gameplay()

#
def gameplay():
    reload1 = 0
    shield1 = 0
    hp1 = 100
    reload2 = 0
    shield2 = 0
    hp2 = 100
    round_count = 1

    while hp1 > 0 and hp2 > 0:
        print("\n--- ROUND",round_count,"---")
        print("Player 1 -> Bullets: ",reload1,"| Shields: ",shield1)
        print("Player 2 -> Bullets: ",reload2,"| Shields: ",shield2)
        barrerita()

        #seleccion de acciones
        action1 = int(input("Player 1 (1: Reload, 2: Shield, 3: Shoot): "))
        action2 = int(input("Player 2 (1: Reload, 2: Shield, 3: Shoot): "))

        #accion Player 1
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

        #accion Player 2
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

        #condicionales limitantes
        if shield1 > 3:
            shield1 = 0
        if reload1 > 3:
            reload1 = 0
        if shield2 > 3:
            shield2 = 0
        if reload2 > 3:
            reload2 = 0

        #interacciones
        if shot1 and shield2 > 0:
            print("Player 2 blocked Player 1's shot!")
            shield2 -= 1
        elif shot1 and shield2 == 0:
            print("Player 1 shot Player 2!")
            hp2 = 0

        if shot2 and shield1 > 0:
            print("Player 1 blocked Player 2's shot!")
            shield1 -= 1
        elif shot2 and shield1 == 0:
            print("Player 2 shot Player 1!")
            hp1 = 0

        round_count += 1

    #display
    barrerita()
    if hp1 <= 0:
        print("Player 2 Wins!")
    elif hp2 >= 0:
        print("Player 1 Wins!")

main()