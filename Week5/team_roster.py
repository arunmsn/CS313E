"""Program to manage a soccer team roster."""

ROSTER = {}

def add_to_roster():
    """Adds the players to the roster"""
    for _ in range(5):
        print(f"Enter player {_ + 1}'s jersey number:")
        player_jersey = int(input())
        print(f"Enter player {_ + 1}'s rating:")
        player_rating = int(input())
        if (0 <= player_jersey <= 99 and 1 <= player_rating <= 9):
            ROSTER[player_jersey] = player_rating
        print()
    return ROSTER

def output_roster():
    """Prints the Roster"""
    ordered_roster = sorted(ROSTER)
    print("ROSTER")
    for jersey in ordered_roster:
        print(f"Jersey number: {jersey}, Rating: {ROSTER.get(jersey)}")

def add_player():
    """Allows the user to add a new player"""
    print("Enter a new player's jersey number:")
    player_jersey = int(input())
    print("Enter the player's rating:")
    player_rating = int(input())
    print()
    if (0 <= player_jersey <= 99 and 1 <= player_rating <= 9):
        ROSTER[player_jersey] = player_rating

def remove_player():
    """Allows the user to remove a player"""
    print("Enter a jersey number:")
    jersey = int(input())
    ROSTER.pop(jersey)

def update_player_rating():
    """Allows the user to update a player's rating"""
    print("Enter a jersey number:")
    jersey = int(input())
    print("Enter a new rating for player:")
    new_rating = int(input())
    ROSTER[jersey] = new_rating

def output_player_above_rating():
    """Allows the user to input a rating and outputs the player above said rating"""
    print("Enter a rating:")
    rating = int(input())
    print()

    print(f"ABOVE {rating}")
    ordered_roster = sorted(ROSTER)
    for jersey in ordered_roster:
        if ROSTER.get(jersey) > rating:
            print(f"Jersey number: {jersey}, Rating: {ROSTER.get(jersey)}")

def menu():
    """Outputs the menu for the user to access"""
    print("MENU")
    print("a - Add player")
    print("d - Remove player")
    print("u - Update player rating")
    print("r - Output players above a rating")
    print("o - Output roster")
    print("q - Quit")
    print()
    print("Choose an option:")

    choice = input()
    if choice == "q" or choice == "Q":
        return
    elif choice == "o" or choice == "O":
        output_roster()
        print()
        menu()
    elif choice == "a" or choice == "A":
        add_player()
        print()
        menu()
    elif choice == "d" or choice == "D":
        remove_player()
        print()
        menu()
    elif choice == "u" or choice == "U":
        update_player_rating()
        print()
        menu()
    elif choice == "r" or choice == "R":
        output_player_above_rating()
        print()
        menu()
    else:
        return

def main():
    """Main method"""
    add_to_roster()
    output_roster()
    print()
    menu()

main()
