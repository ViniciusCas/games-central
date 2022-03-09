from random import randint

class Game():

    def __init__(self, lifes=16, offset=5, pontuation=100):

        num = randint(1, 100)
        self.lifes = lifes
        self.offset = offset
        self.pontuation = pontuation
        print(num)
        self.openning_msg()

        tries = self.difficulty_selector(lifes)

        self.game_loop(tries, num, self.offset, self.pontuation)
        
    def openning_msg(self):
        print("\n*************************************")
        print("***   Welcome to Game game!   ***")
        print("*************************************\n")

    def difficulty_selector(self, lifes):
        print("What is your difficulty? ")
        print("(1) easy\n(2) medium\n(3) hard\n")

        tries = 0
        while tries == 0:
            lvl = int(input("Type your difficulty: "))

            if lvl != 1 and lvl != 2 and lvl != 3:
                print("\nJust type (1) for easy, (2) for medium or (3) for hard!\n")
                continue
            tries = int(lifes / lvl)
        return tries

    def game_loop(self, tries, num, offset, pontuation):
        while tries != 0:
            print(f"Tries: {tries}")

            user_inp = int(input("Enter which number you think is between 1 and 100: "))
            print()

            if user_inp < 1 or user_inp > 100:
                print("Enter a number between 1 and 100!\n")
                continue

            matched = user_inp == num
            greater_than = user_inp > num
            less_than = user_inp < num

            if matched:
                print(f"You got it right, and you did {pontuation} points!")
                break
            else:
                lost_points = abs(num - user_inp)
                pontuation -= lost_points
                if greater_than and user_inp - offset <= num:
                    print("your number was close but still smaller\n")
                elif greater_than and user_inp - offset >= num:
                    print("your number was much higher\n")
                elif less_than and user_inp + offset >= num:
                    print("your number was close but still higher\n")
                elif less_than and user_inp + offset <= num:
                    print("your number was much smaller\n")
                
                tries -= 1

        if not tries:
            print("Your attempts are over, you lost!")
            print(f"The number was {num}")


if __name__ == "__main__":
    Game()