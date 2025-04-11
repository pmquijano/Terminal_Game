import sys, random, time

# Combat function
def combat_scene(player_name, player_health, monster_health):
    print("\n⚔️ A hostile creature approaches!")
    while player_health > 0 and monster_health > 0:
        print(f"\n🧟 Monster HP: {monster_health}")
        print(f"🧑 {player_name}'s HP: {player_health}")
        action = input("[1] Attack  [2] Heal: ")

        if action == "1":
            monster_health -= 30
            print("\n🔫 You fire your blaster! The monster screeches in pain.")
            if monster_health > 0:
                player_health -= 30
                print("💢 The monster counters and claws at you!")
        elif action == "2":
            player_health += 30
            monster_damage = random.randint(20, 30)
            player_health -= monster_damage
            print("\n🩹 You quickly patch yourself up...")
            print("But the monster leaps forward and lands a hit!")
        else:
            print("❌ Invalid input. Exiting game.")
            sys.exit()

    # Outcome of the battle
    if player_health <= 0:
        print(f"\n💀 {player_name} has fallen in battle. Game over.")
        sys.exit()
    else:
        print("\n✅ The monster collapses. You survive... for now.")
        print("🛸 You regain your breath and prepare to move deeper into the ship.")
        return player_health  # Updated health to continue
# SCENE 2
def scene_2(player_name, player_health, monster_health):
    print('You enter a dark corridor. A terminal flickers.')
    print('hack the terminal?')
    action = input("[1] Hack it [2] Go dive deeper: ")
    print('===============')
    player_health = 100
    monster_health = 200

    if action == "1":
        print("hacking terminal, loading resources")
        time.sleep(1.5)
        print("success! I think control dock is accesible now")

    elif action == "2":
        print("\nYou venture deeper into the ship...")
        time.sleep(1.5)
        print("You saw a black box along your path way")
        print('===============')
        action = input("What will you do? [1] get black box [2] Ignore")

        if action == "1":
            print("you found the data source and blueprint of the previous ship..")
        elif action == "2":
            print("your scanner picks up another movement")
            print("A creature was able to regrow.. and stronger this time")
            # Call combat scene function
            player_health = combat_scene(player_name, player_health, monster_health)
            #proceed to scene 3
        else:
            print("❌ Invalid input. Exiting game. _scene2_b")
            sys.exit()
    else:
        print("❌ Invalid input. Exiting game. _scene2_a")
        sys.exit()
# SCENE 2

# SCENE 3
def scene_3 (player_name, player_health, monster_health):
    print("\n🛸 You reach the control deck of the Pioneer...")
    print("Screens flicker. The main terminal lights up.")
    print("A log begins to play automatically...\n")
    input("...")
    time.sleep(2)

    print("=== Ship Log: Year 2348 ===")
    print("FTL jump failed. Coordinates mismatched. A rift opened mid-jump.")
    print("Crew suspected sabotage. Unknown entity may have boarded during transit.")
    print("Attempts to reverse jump failed. Life support failing... End log.")
    print("=====================================")
    time.sleep(2)

    print("\nYou now understand why the Pioneer vanished 17 years ago.")
    time.sleep(1.5)
    print("\nWhat do you want to do next?")
    action = input("[1] review further [2] Return to the hub")
    if action == "1":
        print("\nYou dig deeper into the system...")
        time.sleep(1.5)
        print("More encrypted files begin to decrypt...")
        print("To be continued... 🔍")
    elif action == "2":
        print("\nYou return to the shuttle hub...")
        time.sleep(1.5)
        print("Mission ending triggered. Debriefing will begin.")
        print("Well done, Explorer.")
        print("THE END")
        sys.exit()
    else:
        print("❌ Invalid input. Exiting game. _scene2_b")
        sys.exit()

#check inventory:
#medkits: 5
#ocation: shipwreck

# Main game flow
def start_game():
    print("Welcome, Explorer!")
    player_name = input("Enter your name, Explorer: ")
    print('Your are about to explore the future')
    time.sleep(1.5)
    print('===============')
    print('The Pioneer has suddenly reappeared—drifting near a dead planet, powered on, but no life signs detected.')
    time.sleep(1.5)
    print(f'We sent you {player_name} to investigate a distress signal from the colony ship Pioneer')
    time.sleep(1.5)
    print('which vanished 17 years ago during faster-than-light travel.')
    print('===============')
    time.sleep(1.5)

    player_health = 100
    monster_health = 90

    #combat start
    print('INCOMING DISTRESS SIGNAL — ORIGIN: PIONEER-9 STABILIZED ORBIT DETECTED. CREW STATUS: UNKNOWN')
    time.sleep(1.5)
    action = input("\nYou arrive on the lost ship. Do you want to [1] Explore or [2] Stay in your shuttle? ")

    if action == "1":
        print("\n>> Prepare to Explore! <<")
        print("Your shuttle touches down in a lost ship, and your scanner picks up movement.")
        print("A creature approaches!")
        
        # Call combat scene function
        player_health = combat_scene(player_name, player_health, monster_health)

        # Continue after battle
        print("\nYou survived the battle, but what's next?")
        #Call scene 2 function
        player_health= scene_2(player_name, player_health, monster_health)

        # Continue scene 3
        print("\nYou survived the battle, but what's next?")
        player_health= scene_3(player_name, player_health, monster_health)


    elif action == "2":
        print("\nYou decide to stay in the shuttle and watch through the viewport.")
        time.sleep(1.5)
        print("Suddenly, the hatch bangs violently.")
        time.sleep(1.5)
        print("Something is outside.")
        time.sleep(1.5)
        # Handle other actions, such as defending or escaping
    else:
        print("❌ Invalid input. Exiting game.")
        sys.exit()
if __name__ == "__main__":
    start_game()
# End of Main game*