import random
import colorful as cf

"""
Normal Mode
Inputs:
1.- Player's 1 action (1, 2 or 3)
2.- Player's 2 action (1, 2 or 3)

Process:
1.- Check if both players HP is higher to 0 to start the round
2.- Ask both players their actions
3.- Depending on the selected action, execute a conditional to create the
    interaction
4.- Check if the reloads or shields are greater than 0 to set them to 0
5.- Continue the rounds until a player's hp becomes 0 or lower

Outputs:
1.- Display the rules, the interactions and the controls
2.- Display of the current players turn, current round and their stats
    (quantity of bullets and shield)
3.- Display a message if a player shoots without bullets
4.- If a player HP becomes 0 or lower, display a winning message for the winner
"""

RELOAD_INIT = 0
SHIELD_INIT = 0
HP_INIT = 100
ROUND_INIT = 1
MAX_LIMIT = 3

# Effects that last more than one round
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


#Function to validate and avoid crashes
def leer_opcion(mensaje, minimo, maximo):
    """Validate integer input within a given range to prevent crashes."""
    while True:
        try:
            valor = int(input(mensaje))
            if minimo <= valor <= maximo:
                return valor
            print(cf.red(f"Please enter a number between {minimo} and {maximo}."))
        except ValueError:
            print(cf.red("Invalid input. Please enter a numeric value."))


def barrerita():
    """Print '----' divider line for the menus."""
    print(cf.blue("-------------------------------"))


def menu():
    """Display welcome message and game rules."""
    print("Hello, welcome to VA-QUE-RI-TOS")
    barrerita()
    print("The rules are simple, each player has three actions:")
    print("- Reload (1): to reload your gun. If you have 0 bullets, " "you can't shoot.")
    print("- Shield (2): to protect yourself from other players' attacks.")
    print("- Shoot (3): to attack players.")
    print("Maximum 3 reloads or 3 shields stored. Excess sets them to 0.")
    print("If you are shot without a shield, you lose!")
    barrerita()

def score_read():
    """Read historical scores for Player 1 and Player 2 from Score.txt."""
    try:
        with open("Score.txt", "r", encoding="utf-8") as score:
            content = score.read()

        # Find ":" to read each player score
        p1_find = content.find(":")
        p2_find = content.rfind(":")

        # Find where each player score line ends
        p1_line = content.find("\n", p1_find)
        p2_line = content.find("\n", p2_find)

        p1_strip = int(content[p1_find + 1:p1_line].strip())
        p2_strip = int(content[p2_find + 1:p2_line].strip())
        return p1_strip, p2_strip
    except (FileNotFoundError, ValueError):
        return 0, 0

def score_write(p1, p2):
    """Add match points to historical scores and write them to Score.txt."""
    p1_strip, p2_strip = score_read()
    total_p1 = p1_strip + p1
    total_p2 = p2_strip + p2

    with open("Score.txt", "w", encoding="utf-8") as score:
        score.write("---------------------\n")
        score.write(f"Player 1 score: {total_p1}\n\n")
        score.write(f"Player 2 score: {total_p2}\n")
        score.write("---------------------")

    print(f"Historical Scores -> Player 1: {total_p1} | Player 2: {total_p2}")


#Function to print battle log
def mostrar_matriz_historial(historial_matriz):
    """Display the 2D matrix containing the round-by-round match log."""
    print(cf.yellow("\n--- MATCH HISTORY MATRIX ---"))
    print(cf.yellow("Round | P1 Act | P2 Act | P1 HP | P2 HP"))
    barrerita()
    for fila in historial_matriz:
        print(cf.yellow(f"  {fila[0]:<4}|   {fila[1]:<5}|   {fila[2]:<5}|  "f"{fila[3]:<5}|  {fila[4]:<5}"))
    barrerita()


def gameplay():
    """Run the main gameplay loop for normal mode."""
    r1, s1, h1 = RELOAD_INIT, SHIELD_INIT, HP_INIT
    r2, s2, h2 = RELOAD_INIT, SHIELD_INIT, HP_INIT
    p1, p2 = 0, 0
    r_count = ROUND_INIT
    historial_matriz = []  #Matrix to save each round data

    prev_p1, prev_p2 = score_read()
    print(f"Saved Score -> Player 1: {prev_p1} | Player 2: {prev_p2}")

    while h1 > 0 and h2 > 0:
        print("\n--- ROUND", r_count, "---")
        print(cf.blue(f"Player 1 -> Bullets: {r1}| Shields: {s1}| HP: {h1}"))
        barrerita()
        print(cf.blue(f"Player 1 -> Bullets: {r2}| Shields: {s2}| HP: {h2}"))

        r1, s1, h1, r2, s2, h2, r_count, p1, p2, act1, act2 = game_action(r1, s1, h1, r2, s2, h2, r_count, p1, p2)
        historial_matriz.append([r_count - 1, act1, act2, h1, h2])
        barrerita()

    display(h1, h2, p1, p2, historial_matriz)


def game_action(reload1, shield1, hp1, reload2, shield2, hp2,
                round_count, p1, p2):
    """Process actions and interactions for each player in normal mode."""
    action1 = leer_opcion("Player 1 (1: Reload, 2: Shield, 3: Shoot): ", 1, 3)
    action2 = leer_opcion("Player 2 (1: Reload, 2: Shield, 3: Shoot): ", 1, 3)

    shot1 = False
    if action1 == 1:
        reload1 += 1
        p1 += 10
    elif action1 == 2:
        shield1 += 1
        p1 += 10
    elif action1 == 3:
        if reload1 > 0:
            reload1 -= 1
            shot1 = True
            p1 += 10
        else:
            print(cf.red("Player 1 tried to shoot without bullets!"))

    shot2 = False
    if action2 == 1:
        reload2 += 1
        p2 += 10
    elif action2 == 2:
        shield2 += 1
        p2 += 10
    elif action2 == 3:
        if reload2 > 0:
            reload2 -= 1
            shot2 = True
            p2 += 10
        else:
            print(cf.red("Player 2 tried to shoot without bullets!"))

    # Establish limits to actions for a fair game
    if shield1 > MAX_LIMIT:
        p1 -= 20
        shield1 = 0
    if reload1 > MAX_LIMIT:
        p1 -= 20
        reload1 = 0
    if shield2 > MAX_LIMIT:
        p2 -= 20
        shield2 = 0
    if reload2 > MAX_LIMIT:
        p2 -= 20
        reload2 = 0

    # Player 1 shoots Player 2
    if shot1:
        if shield2 > 0:
            print(cf.green("Player 2 blocked Player 1's shot!"))
            shield2 -= 1
            p1 += 25
        else:
            print(cf.green("Player 1 shot Player 2!"))
            hp2 = 0
            p1 += 100

    # Player 2 shoots Player 1
    if shot2:
        if shield1 > 0:
            print(cf.green("Player 1 blocked Player 2's shot!"))
            shield1 -= 1
            p2 += 25
        else:
            print(cf.green("Player 2 shot Player 1!"))
            hp1 = 0
            p2 += 100

    round_count += 1
    return (reload1, shield1, hp1, reload2, shield2, hp2,
            round_count, p1, p2, action1, action2)


def display(hp1, hp2, p1, p2, historial_matriz):
    """Display winner at the end of the game, update score, and show log."""
    barrerita()
    if hp1 <= 0 and hp2 <= 0:
        print(cf.grey("It's a draw! Both players were eliminated."))
        p1 += 200
        p2 += 200
    elif hp1 <= 0:
        print(cf.green("Player 2 Wins!"))
        p2 += 500
    elif hp2 <= 0:
        print(cf.green("Player 1 Wins!"))
        p1 += 500

    score_write(p1, p2) 
    mostrar_matriz_historial(historial_matriz) 


# Special mode functions
def habilities():
    """Initialize player power lists and the special abilities dictionary."""
    habilidades = {
        1: "White album (Double Shield)",
        2: "Sex pistols (Double shot)",
        3: "Hol horse (Double reload)",
        4: "Mountain tim (Steal a shield from the other player)",
        5: "King crimson (Gives you a free turn shield)",
        6: "C moon (The opponent's next shot will be directed to itself)",
        7: "Metallica (The opponent's shot will be cancelled)",
        8: "The World (The opponent can't act next turn)",
        9: "Killer queen (Eliminates all the opponent's shields)",
        10: "Kars (Become invincible for 1 turn)"
    }

    player1_powers = []
    player2_powers = []

    return player1_powers, player2_powers, habilidades


def nombres_poderes(powers, habilidades):
    """Extract and return clean power names using split()."""
    nombres = []
    for p in powers:
        nombres.append(habilidades[p].split(" (")[0])
    return nombres


def elegir_poder(num, powers, habilidades):
    """Ask the player if they want to use an available power."""
    if len(powers) == 0:
        return 0
    print(f"Player {num} powers:")
    for i in range(len(powers)):
        print(f"  {i + 1}) {habilidades[powers[i]]}")
    opcion = leer_opcion(
        f"Player {num}, use a power? (0 = none, or its number): ",
        0,
        len(powers)
    )
    if opcion == 0:
        return 0
    return powers[opcion - 1]


def impacto(shield, hp, atacante, defensor, invencible, libre):
    """Resolve shot impact considering King Crimson, Kars, and shields."""
    if invencible:
        print(cf.green(f"Player {defensor} is invincible! The shot had no effect."))
    elif libre:
        print(cf.green(f"Player {defensor} dodged Player {atacante}'s shot " "with the free shield!"))
        libre = False
    elif shield > 0:
        print(cf.green(f"Player {defensor} blocked Player {atacante}'s shot!"))
        shield -= 1
    else:
        print(cf.green(f"Player {atacante} shot Player {defensor}!"))
        hp = 0
    return shield, hp, libre


def s_gameplay():
    """Run the main gameplay loop for special powers mode."""
    r1, s1, h1 = RELOAD_INIT, SHIELD_INIT, HP_INIT
    r2, s2, h2 = RELOAD_INIT, SHIELD_INIT, HP_INIT
    p1, p2 = 0, 0
    r_count = ROUND_INIT
    historial_matriz = []  #Matrix to store used powers
    player1_powers, player2_powers, habilidades = habilities()

    prev_p1, prev_p2 = score_read()
    print(cf.yellow(f"Saved Score -> Player 1: {prev_p1} | Player 2: {prev_p2}"))

    while h1 > 0 and h2 > 0:
        player1_powers, player2_powers = hab_ver(
            r_count, player1_powers, player2_powers
        )
        print("\n--- ROUND", r_count, "---")
        print(cf.blue(f"Player 1 -> Bullets: {r1}| Shields: {s1}| HP: {h1}"))
        print(cf.purple(f"Player 1 powers: {nombres_poderes(player1_powers, habilidades)}"))
        print(cf.blue(f"Player 1 -> Bullets: {r2}| Shields: {s2}| HP: {h2}"))
        print(cf.purple(f"Player 2 powers: {nombres_poderes(player2_powers, habilidades)}"))

        (r1, s1, h1, r2, s2, h2, r_count, player1_powers,
        player2_powers, habilidades, p1, p2, act1, act2) = s_game_action(r1, s1, h1, r2, s2, h2, r_count, player1_powers, player2_powers, habilidades, p1, p2)
        historial_matriz.append([r_count - 1, act1, act2, h1, h2])
        barrerita()

    display(h1, h2, p1, p2, historial_matriz)


def hab_ver(r_count, player1_powers, player2_powers):
    """Give random powers every 3 turns and cap inventory at 3 powers."""
    if r_count % 3 == 0:
        for i in range(3):
            x = random.randint(1, 10)
            if x not in player1_powers:
                player1_powers.append(x)
        for i in range(3):
            x = random.randint(1, 10)
            if x not in player2_powers:
                player2_powers.append(x)
    while len(player1_powers) > MAX_LIMIT:
        player1_powers.pop(0)
    while len(player2_powers) > MAX_LIMIT:
        player2_powers.pop(0)
    return player1_powers, player2_powers


def s_game_action(reload1, shield1, hp1, reload2, shield2, hp2, r_count,
                player1_powers, player2_powers, habilidades, p1, p2):
    """Process player actions, powers, and interactions in special mode."""
    if efectos["skip1"]:
        print(cf.purple("Player 1 is frozen by The World and can't act this turn!"))
        efectos["skip1"] = False
        action1 = 0
        power1 = 0
        p2 += 50
    else:
        action1 = leer_opcion(
            "Player 1 (1: Reload, 2: Shield, 3: Shoot): ", 1, 3
        )
        power1 = elegir_poder(1, player1_powers, habilidades)

    if efectos["skip2"]:
        print(cf.purple("Player 2 is frozen by The World and can't act this turn!"))
        efectos["skip2"] = False
        action2 = 0
        power2 = 0
        p1 += 50
    else:
        action2 = leer_opcion(
            "Player 2 (1: Reload, 2: Shield, 3: Shoot): ", 1, 3
        )
        power2 = elegir_poder(2, player2_powers, habilidades)

    shot1 = False
    disparos1 = 1
    if action1 == 1:
        reload1 += 1
        p1 += 10
    elif action1 == 2:
        shield1 += 1
        p1 += 10
    elif action1 == 3:
        if reload1 > 0:
            reload1 -= 1
            shot1 = True
            p1 += 10
        else:
            print(cf.red("Player 1 tried to shoot without bullets!"))

    shot2 = False
    disparos2 = 1
    if action2 == 1:
        reload2 += 1
        p2 += 10
    elif action2 == 2:
        shield2 += 1
        p2 += 10
    elif action2 == 3:
        if reload2 > 0:
            reload2 -= 1
            shot2 = True
            p2 += 10
        else:
            print(cf.red("Player 2 tried to shoot without bullets!"))

    #Powers action for Player 1
    if power1 != 0:
        player1_powers.remove(power1)
        print(cf.purple(f"Player 1 used {habilidades[power1].split(' (')[0]}!"))
        if power1 == 1:
            shield1 += 2
            p1 += 50
        elif power1 == 2:
            shot1 = True
            disparos1 = 2
            p1 += 50
        elif power1 == 3:
            reload1 += 2
            p1 += 50
        elif power1 == 4:
            if shield2 > 0:
                shield2 -= 1
                shield1 += 1
                p1 += 50
            else:
                print(cf.red("Player 2 has no shields to steal."))
        elif power1 == 5:
            efectos["free1"] = True
            p1 += 50
        elif power1 == 6:
            efectos["reflect2"] = True
            p1 += 50
        elif power1 == 7:
            efectos["cancel2"] = True
            p1 += 50
        elif power1 == 8:
            efectos["skip2"] = True
            p1 += 50
        elif power1 == 9:
            shield2 = 0
            p1 += 50
        elif power1 == 10:
            efectos["inv1"] = True
            p1 += 50

    # Powers action for Player 2
    if power2 != 0:
        player2_powers.remove(power2)
        print(cf.purple(f"Player 2 used {habilidades[power2].split(' (')[0]}!"))
        if power2 == 1:
            shield2 += 2
            p2 += 50
        elif power2 == 2:
            shot2 = True
            disparos2 = 2
            p2 += 50
        elif power2 == 3:
            reload2 += 2
            p2 += 50
        elif power2 == 4:
            if shield1 > 0:
                shield1 -= 1
                shield2 += 1
                p2 += 50
            else:
                print(cf.red("Player 1 has no shields to steal."))
        elif power2 == 5:
            efectos["free2"] = True
            p2 += 50
        elif power2 == 6:
            efectos["reflect1"] = True
            p2 += 50
        elif power2 == 7:
            efectos["cancel1"] = True
            p2 += 50
        elif power2 == 8:
            efectos["skip1"] = True
            p2 += 50
        elif power2 == 9:
            shield1 = 0
            p2 += 50
        elif power2 == 10:
            efectos["inv2"] = True
            p2 += 50

    # Establish limits to actions for a fair game
    if shield1 > MAX_LIMIT:
        shield1 = 0
        p1 -= 20
    if reload1 > MAX_LIMIT:
        reload1 = 0
        p1 -= 20
    if shield2 > MAX_LIMIT:
        shield2 = 0
        p2 -= 20
    if reload2 > MAX_LIMIT:
        reload2 = 0
        p2 -= 20

    # Actions interactions updated with abilities
    if shot1:
        if efectos["cancel1"]:
            print(cf.purple("Player 1's shot was cancelled by Metallica!"))
            efectos["cancel1"] = False
            p2 += 150
        else:
            destino = 2
            if efectos["reflect1"]:
                print(cf.purple("C moon redirected Player 1's shot to himself!"))
                efectos["reflect1"] = False
                destino = 1
                p2 += 150
            for i in range(disparos1):
                if destino == 2:
                    shield2, hp2, efectos["free2"] = impacto(
                        shield2, hp2, 1, 2, efectos["inv2"], efectos["free2"]
                    )
                else:
                    shield1, hp1, efectos["free1"] = impacto(
                        shield1, hp1, 1, 1, efectos["inv1"], efectos["free1"]
                    )

    if shot2:
        if efectos["cancel2"]:
            print(cf.purple("Player 2's shot was cancelled by Metallica!"))
            efectos["cancel2"] = False
            p1 += 150
        else:
            destino = 1
            if efectos["reflect2"]:
                print(cf.purple("C moon redirected Player 2's shot to himself!"))
                efectos["reflect2"] = False
                destino = 2
                p1 += 150
            for i in range(disparos2):
                if destino == 1:
                    shield1, hp1, efectos["free1"] = impacto(
                        shield1, hp1, 2, 1, efectos["inv1"], efectos["free1"]
                    )
                else:
                    shield2, hp2, efectos["free2"] = impacto(
                        shield2, hp2, 2, 2, efectos["inv2"], efectos["free2"]
                    )

    # One turn duration for Kars and King Crimson
    efectos["inv1"] = False
    efectos["inv2"] = False
    efectos["free1"] = False
    efectos["free2"] = False

    r_count += 1
    return (reload1, shield1, hp1, reload2, shield2, hp2, r_count,
            player1_powers, player2_powers, habilidades,
            p1, p2, action1, action2)


#(For rubric) Test cases
def run_tests():
    """Run basic test cases to verify core game mechanics."""
    s_out, hp_out, _ = impacto(2, 100, 1, 2, False, False)
    assert s_out == 1 and hp_out == 100, "Test 1 (Block) failed" #assert validates if the output is true

    s_out, hp_out, _ = impacto(0, 100, 1, 2, False, False)
    assert s_out == 0 and hp_out == 0, "Test 2 (Direct hit) failed"

    _, _, habilidades = habilities()
    assert nombres_poderes([1, 8], habilidades) == ["White album", "The World"]
    print(cf.green("All test cases passed successfully!\n"))


def main():
    """Control menu display, mode selection, and play-again loop."""
    run_tests()  #Run tests before starting
    menu()
    while True:
        selection = leer_opcion(
            "Please enter (1) for normal mode, or (2) for powers mode: ", 1, 2)
        if selection == 1:
            gameplay()
        else:
            s_gameplay()

        #Ask to play again
        jugar_otra = leer_opcion("\nDo you want to play again? (1: Yes, 2: No): ", 1, 2)
        if jugar_otra == 1:
            print("Let's play again!")
        elif jugar_otra == 2:
            print("Thanks for playing VA-QUE-RI-TOS!")
            break

main()
