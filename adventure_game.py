import time
import random


def print_pause(string):
    print(string)
    time.sleep(2)


def validate_input(prompt, option1, option2, items):
    while True:
        response = input(prompt).lower()
        if response == option1:
            break
        elif response == option2:
            break
        elif response == "check inventory":
            print_pause("You are carrying the following objects:")
            print(items)
        else:
            print_pause("Sorry, I don't understand your command.")
    return response


def gearcheck(items, weak_monster, dragon_name):
    if "Tiamat" in items:
        island1_dragon(items, weak_monster, dragon_name)
    elif "Leviathan" in items:
        island2_dragon(items, weak_monster, dragon_name)
    else:
        dragon_fail()


def start_game():
    items = ["Compass", "Steel sword"]
    weak_monster = random.choice(['goblin', 'slime',
                                  'orc', 'zombie', 'pixie', 'golem'])
    dragon_name = random.choice(['Vilgas', 'Vangus', 'Raglion',
                                 'Waiyir', 'Ze Wir', 'Ferdia'])
    intro(items, weak_monster, dragon_name)


def intro(items, weak_monster, dragon_name):
    print_pause("You are a skyfaring adventurer, here preparing to travel\n"
                "the myriad floating islands of this in search for "
                "new discoveries and treasure.")
    print_pause("You stand on the deck of your airship, "
                "gazing out to the blue horizon.")
    print_pause("To the east, you see a bright green island\n"
                "off in the distance, grassy and mountainous.")
    print_pause("To the west, another island, this one with\n"
                "a massive ocean, glinting in the sunshine.")
    print_pause("In one hand you hold your trusty compass,\n"
                "and in the other you hold a basic steel sword.")
    print_pause("(You can type 'check inventory' at any time "
                "to view what you're carrying.)")
    response = validate_input("Do you set out for the grassy island, "
                              "or the ocean island?\n",
                              'grassy', 'ocean', items)
    if 'grassy' in response:
        island1(items, weak_monster, dragon_name)
    elif 'ocean' in response:
        island2(items, weak_monster, dragon_name)


def island1(items, weak_monster, dragon_name):
    print_pause("You stand on a grassy knoll, "
                "a light breeze blowing over you.")
    print_pause("In the distance, you spot a small, rocky hill,\n"
                "a dark cave set into the mountain.")
    print_pause("In another direction, you see a huge forest, tall,\n"
                "intimidating trees blocking out the sun.")
    response = validate_input("Would you like to investigate the cave, "
                              "or head towards the forest?\n",
                              'cave', 'forest', items)
    if 'cave' in response:
        cave(items, weak_monster, dragon_name)
    elif 'forest' in response:
        forest(items, weak_monster, dragon_name)


def cave(items, weak_monster, dragon_name):
    if "Tiamat" in items:
        print_pause("You've already looted the cave for everything it has. "
                    "No point going back there.")
        island1(items, weak_monster, dragon_name)
    print_pause("In the cave, you find an old torch lying on the floor.\n"
                "It lights easily, allowing you to easily travel deeper in.")
    print_pause("The cave is cold and damp, "
                "and traversing it is no easy feat.")
    print_pause("Suddenly, you hear a snarl behind you!")
    print_pause(f"It's a {weak_monster}! And it's coming after you!")
    response = validate_input("Will you fight, or will you run?\n",
                              'fight', 'run', items)
    if 'fight' in response:
        cave_combat(items, weak_monster, dragon_name)
    if 'run' in response:
        print_pause("You turn tail and flee!")
        island1(items, weak_monster, dragon_name)


def cave_combat(items, weak_monster, dragon_name):
    print_pause("Despite getting the jump on you, the pitiful creature\n"
                "still falls easily to your steel blade.")
    print_pause("You can't seem to find anything useful off its body,\n"
                "so you decide to leave it lying there and push on.")
    print_pause("Eventually, you reach the back of the cave.\n"
                "A small, gold treasure chest lies, embedded in the soil.")
    print_pause("Kicking it open, you pull out a small, "
                "glowing dagger with a green hilt.\n"
                "An inscription on the hilt reads 'Tiamat.'")
    print_pause("Satisfied with your findings, you decide to leave the cave.")
    items.append("Tiamat")
    island1(items, weak_monster, dragon_name)


def forest(items, weak_monster, dragon_name):
    print_pause("You wander into the forest. "
                "Though not as dark as the cave appeared,\n"
                "the tall trees bunched tight together block out "
                "most of the sun from the forest floor.")
    print_pause("You stumble over stones, roots, "
                "and things that feel disturbingly wet,\n"
                "but in the end, you come out into a large "
                "clearing in the middle of the field.")
    print_pause("A massive, lumbering creature stands before you, head--\n"
                "no, three heads bent low, gazing at you. "
                "Massive, green wings beating against the sky.")
    print_pause("It's a huge three-headed dragon! "
                "You hear a voice in your head...")
    print_pause(f"I am the dread hydra, {dragon_name}!\n"
                "Those who wish to seek the fortunes of this place "
                "must test your might against mine!")
    response = validate_input("You gulp instinctively. "
                              "Will you fight, or will you run?\n",
                              "fight", "run", items)
    if 'fight' in response:
        gearcheck(items, weak_monster, dragon_name)
    elif 'run' in response:
        print_pause("You turn tail and flee!")
        island1(items, weak_monster, dragon_name)


def island1_dragon(items, weak_monster, dragon_name):
    print_pause("The dragon lashes out at you fiercefully,\n"
                "a massive breath of fire bearing down upon you.")
    print_pause("However, the Dagger of Tiamat seems to "
                "grant you newfound speed,\n"
                "allowing you to effortlessly dodge the attack!")
    print_pause("As it lunges forth at you, you slip to the side and\n"
                "gracefully sink your dagger into "
                "the base of the beast's three necks!")
    print_pause("With an unearthly screech in your ears, "
                "the beast falls to the ground,\n"
                "flesh dissolving before your eyes.")
    print_pause("At the center of its decaying body... You find a massive,\n"
                "unwieldy golden egg! It's so heavy you can barely lift it!")
    print_pause("With this, you smile to yourself and "
                "decide to head back to your airship,\n"
                "lugging the massive piece of gold all the way there.")
    print_pause("You win!")
    play_again()


def island2(items, weak_monster, dragon_name):
    print_pause("You stand on the ocean island in a field, "
                "gazing out at the vast depths of the sea.")
    print_pause("If you head straight north, you'll arrive at the beach, "
                "able to investigate the shore.")
    print_pause("Yet south lies a mysterious hut, A "
                "single man-made construct in the middle of a deserted land.")
    print_pause("As the gentle ocean breeze washes over you, "
                "you ponder over where to go next.")
    response = validate_input("Will you head to the beach, "
                              "or investigate the hut?\n",
                              "beach", "hut", items)
    if 'beach' in response:
        beach(items, weak_monster, dragon_name)
    elif 'hut' in response:
        hut(items, weak_monster, dragon_name)


def hut(items, weak_monster, dragon_name):
    if "Leviathan" in items:
        print_pause("You've already looted the hut for everything it has. "
                    "No point going back there.")
        island2(items, weak_monster, dragon_name)
    else:
        print_pause("You walk over to the hut... "
                    "And as you approach, it's clear\n"
                    "that its been long abandoned, "
                    "the walls derelict and broken.")
        print_pause("You gingerly push open the front door, "
                    "the hinges creaking...")
        print_pause("And find yourself met with two glowing eyes, "
                    "staring right back at you.")
        print_pause(f"It's a {weak_monster}! "
                    "And it looks like it's not happy to see visitors!")
        response = validate_input("Will you stay and fight, "
                                  "or will you run?\n",
                                  'fight', 'run', items)
        if 'fight' in response:
            hut_combat(items, weak_monster, dragon_name)
        elif 'run' in response:
            print_pause("You turn tail and flee!")
            island2(items, weak_monster, dragon_name)


def hut_combat(items, weak_monster, dragon_name):
    print_pause("The monster lunges at you, hungering in its eyes.")
    print_pause("You hold your steel sword in front of you, "
                "and the beast impales itself on your blade!")
    print_pause("As you clean your blade of the creature's filth, "
                "you survey your surroundings.")
    print_pause("Save for the destroyed furniture littering the interior,\n"
                "you notice a small golden chest hidden away "
                "in the corner of the room, battered but intact.")
    print_pause("You walk over and kick it open...\n"
                "and are greeted with a shining blue pair of gauntlets, "
                "made of some unearthly metal.")
    print_pause("An inscription on them reads 'Leviathan.'")
    print_pause("You put them on, and satsisfied with your findings, "
                "you return to the field.")
    items.append('Leviathan')
    island2(items, weak_monster, dragon_name)


def beach(items, weak_monster, dragon_name):
    print_pause("You stand on the beach, "
                "a moment of calm passing over you as\n"
                "you breathe in the ocean air, listening to the waves.")
    print_pause("Soon, however, that feeling is "
                "replaced with an odd sense of dread.")
    print_pause("Readying your weapon, "
                "you see ripples forming in the ocean...")
    print_pause("A massive, scaled head rears out fron the water, "
                "a serpentine torso\n"
                "with huge, blue wings following, "
                "throwing tidal waves towards you! It's a dragon!")
    print_pause("A voice rings inside your head...")
    print_pause(f"'I am the dread serpent, {dragon_name}!\n"
                "Those who wish to seek the fortunes of this place "
                "must test your might against mine!'")
    response = validate_input("You gulp, but the dragon stays wary as well, "
                              "refusing to come too close.\n"
                              "Will you fight, or will you run?\n",
                              'fight', 'run', items)
    if 'fight' in response:
        gearcheck(items, weak_monster, dragon_name)
    elif 'run' in response:
        print_pause("You turn tail and flee!")
        island2(items, weak_monster, dragon_name)


def island2_dragon(items, weak_monster, dragon_name):
    print_pause("The dragon lashes out at you fiercefully,\n"
                "a massive breath of fire bearing down upon you.")
    print_pause("As you raise your sword to face the beast,\n"
                "your gauntlets of Leviathan begin to glow!")
    print_pause("The oceans part before you, and the dragon becomes unsteady\n"
                "as it struggles to move on the dry land.")
    print_pause("You take this chance to leap forward and "
                "strike the massive monster in the head,\n"
                "your sword sinking into its flesh!")
    print_pause("With an unearthly screech in your ears, "
                "the beast falls to the ground,\n"
                "flesh dissolving before your eyes.")
    print_pause("At the center of its decaying body... You find a massive,\n"
                "unwieldy golden egg! It's so heavy you can barely lift it!")
    print_pause("With this, you smile to yourself and "
                "decide to head back to your airship,\n"
                "lugging the massive piece of gold all the way there.")
    print_pause("You win!")
    play_again()


def dragon_fail():
    print_pause("The dragon lashes out at you fiercefully,\n"
                "a massive breath of fire bearing down upon you.")
    print_pause("Sadly, you have no way of avoiding the attack!\n"
                "The fire surrounds you in a blazing inferno, "
                "and within moments, it's over.")
    print_pause("As your life fades away, "
                "you wonder if there was something you could've done...")
    print_pause("You lose!")
    play_again()


def play_again():
    response = input("Would you like to play again? y/n\n")
    if response == "y":
        start_game()
    elif response == "n":
        print_pause("Thanks for playing!")
    else:
        "Please enter y or n."


start_game()
