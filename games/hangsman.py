from random import randrange


class Game: 

    def __init__(self) :
        lifes = 7

        self.opennig_msg()
        self.path = "hangsman\words.txt"
        secret_word = self.read_words(self.path)

        ans = self.start_answer(secret_word)
        self.gameloop(lifes, ans, secret_word)


    def gameloop(self, lifes, ans, word):
        hanged = False
        won = False

        while not hanged and not won:
            print("Word: ", end="")
            self.write_ui(ans, lifes)

            user_inp = input("\nWhat letter are you thinking? ").strip().lower()

            if user_inp in word:
                for i in enumerate(word):
                    if user_inp == i[1]:
                        ans[i[0]] = i[1]
            else:
                lifes -= 1
            
            self.draw_hangman(lifes)
            hanged = lifes == 0
            won = "_" not in ans

        self.write_ui(ans, lifes)
        
        if won:
            self.winner_msg()
        elif hanged:
            self.loser_msg(word)

    def read_words(self, path):
        with open(path, "r") as archive:
            words = []
            for i in archive:
                words.append(i.strip())

        return words[randrange(0, len(words))].lower()

    def start_answer(self, secret_word):
        return ["_"]*len(secret_word)

    def write_ui(self, ans, lifes):
        for i in ans:
            print(f"{i} ", end="")
        print(f"\nLifes: {lifes}")

    def draw_hangman(self, errors):
        print("  _______     ")
        print(" |/      |    ")

        if(errors == 7):
            print(" |            ")
            print(" |            ")
            print(" |            ")
            print(" |            ")
        elif(errors == 6):
            print(" |      (_)   ")
            print(" |            ")
            print(" |            ")
            print(" |            ")

        elif(errors == 5):
            print(" |      (_)   ")
            print(" |      \     ")
            print(" |            ")
            print(" |            ")

        elif(errors == 4):
            print(" |      (_)   ")
            print(" |      \|    ")
            print(" |            ")
            print(" |            ")

        elif(errors == 3):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |            ")
            print(" |            ")

        elif(errors == 2):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |            ")

        elif(errors == 1):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      /     ")

        elif (errors == 0):
            print(" |      (_)   ")
            print(" |      \|/   ")
            print(" |       |    ")
            print(" |      / \   ")

        print(" |            ")
        print("_|___         ")
        print()

    def loser_msg(self, word):
        print("\nGosh, you've been hanged!")
        print(f"The word was {word}")
        print("    _______________         ")
        print("   /               \       ")
        print("  /                 \      ")
        print("//                   \/\  ")
        print("\|   XXXX     XXXX   | /   ")
        print(" |   XXXX     XXXX   |/     ")
        print(" |   XXX       XXX   |      ")
        print(" |                   |      ")
        print(" \__      XXX      __/     ")
        print("   |\     XXX     /|       ")
        print("   | |           | |        ")
        print("   | I I I I I I I |        ")
        print("   |  I I I I I I  |        ")
        print("   \_             _/       ")
        print("     \_         _/         ")
        print("       \_______/           ")

    def winner_msg(self):
        print("\nCongratulations, you won!")
        print("       ___________      ")
        print("      '._==_==_=_.'     ")
        print("      .-\\:      /-.    ")
        print("     | (|:.     |) |    ")
        print("      '-|:.     |-'     ")
        print("        \\::.    /      ")
        print("         '::. .'        ")
        print("           ) (          ")
        print("         _.' '._        ")
        print("        '-------'       ")

    def opennig_msg(self):
        print("\n*****************************************")
        print("***   Welcome to the Game game!   ***")
        print("*****************************************\n")


if __name__ == "__main__":
    Game()