from importlib import import_module
import games
from games import hangsman
from games import guessing



def choice_game():

    print("\n*********************************")
    print("******  Choice your game!  ******")
    print("*********************************\n")

    game_list = [pkg[1] for pkg in enumerate(dir(games)) if pkg[0] > 6]
    game_index = [i for i in range(len(game_list))]

    for i in game_index:
        print("({}) {}".format(i + 1, game_list[i]))

    while True:
        choice = int(input("which game do you want to play? "))
        if choice - 1 not in game_index:
            print("\nJust type:")
            for i in game_index:
                print("  ({}) {}".format(i, game_list[i]))
            print()
            continue
        break

    print("\nPlaying {} game".format(game_list[choice -1]))

    module = import_module("games.{}".format(game_list[choice -1]))
    play = getattr(module, "Game")()
    play()
    play_again()

        
def play_again():
    while True:
        choice = input("\nDo you want to play again?  (Y/N) ").upper()
        if choice != "Y" and choice != "N":
            print("\nJust type (Y) for YES (N) to NO!\n")
            continue
        break
    if choice == "Y":
        choice_game()


if __name__ == "__main__":
    choice_game()