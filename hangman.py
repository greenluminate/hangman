from random import choice
from string import ascii_letters


class Hangman:
    def __init__(self):
        self.lives = 9
        self.word = ""
        self.len_of_word = None
        self.visible = []
        self.not_guessed_letters = None
        self.already_guessed = []

    def start(self):

        dict_of_words = ["brain", "mind", "tree", "key", "bicycle"]

        self.word = choice(dict_of_words).upper()
        self.len_of_word = len(self.word)
        self.visible = [False] * self.len_of_word
        self.not_guessed_letters = self.len_of_word

        underlines = " ".join(["_"] * self.len_of_word)
        print("Guessing begins!")
        print(underlines + f" \tLives: {self.lives}\t Your guesses: still nothing.")
        print("Write any ascii letters a-z or A-Z, then press enter.")
        return self.guess_validator(self.lives)

    def guess_validator(self, lives):
        if lives == 0:
            print("\n\nGame over!")
            print(f"The word was: {self.word}")
            print("Good luck next time!")
            return self.restart_question()

        letter = input("\nYour choice is: ").capitalize()
        if letter in self.already_guessed:
            print("You guess a character you already sent, please write an other character.")
            return self.guess_validator(lives)
        elif letter in ascii_letters and letter != "":
            self.already_guessed.append(letter)
            return self.guess_comparison(letter, lives)
        else:
            print("You sent an invalid character, please write a character a-z or A-Z.")
            return self.guess_validator(lives)

    def guess_comparison(self, letter=None, lives=9, succeeded=False):
        for index in range(self.len_of_word):
            if self.visible[index]:
                print(self.word[index], end=" ")
            elif self.visible[index] is False:
                if self.word[index] == letter.upper():
                    self.visible[index] = True
                    succeeded = True
                    self.not_guessed_letters -= 1
                    print(self.word[index], end=" ")
                else:
                    print("_", end=" ")
        print(f"\tLives: {lives}\tYour guesses: {', '.join(self.already_guessed)}")
        if succeeded:
            if self.not_guessed_letters == 0:
                print("")
                win_beer = "Congratulation, You WON a virtual beer!"
                len_win_beer = len(win_beer)
                print(f"{win_beer}\n{win_beer}")
                for i in range(1, len_win_beer // 3):
                    beer_width = f"{' ' * i}{win_beer[i:-i]}"
                    print(f"{beer_width}\n{beer_width}")
                for i in range(len_win_beer // 3 - 1, 5, -1):
                    beer_width = f"{' ' * i}{win_beer[i:-i]}"
                    print(f"{beer_width}\n{beer_width}")
                print(f"\nThe word was: {self.word}")
                if lives == 9:
                    print("WOW, You did not lose any life!")
                return self.restart_question()

            return self.guess_validator(lives)
        print(f"Letter: '{letter}' is NOT in word. :(")
        print(f"Left lives: {lives - 1}")
        return self.guess_validator(lives - 1)

    def restart_question(self):
        print("\nDo you want to start a new game? Press: y.")
        print("Do you want to exit the program? Press: n.")
        print("> ", end="")
        is_restart = input()
        if is_restart == "y":
            print("\n")
            self.__init__()
            return self.start()
        elif is_restart == "n":
            exit()
        else:
            print("Please press 'y' if you want to start a new game or press 'n' if you want to exit the program.")
            return self.restart_question()


hangman = Hangman()
hangman.start()
