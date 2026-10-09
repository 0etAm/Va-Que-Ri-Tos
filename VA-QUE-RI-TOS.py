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
    gameplay()

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
#Call main
main()