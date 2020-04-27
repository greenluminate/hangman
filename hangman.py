from random import choice
from string import ascii_letters
import requests
from bs4 import BeautifulSoup


class Hangman:
    def __init__(self):
        self.lives = 9
        self.word = ""
        self.len_of_word = None
        self.visible = []
        self.not_guessed_letters = None
        self.already_guessed = []

    def welcome(self):
        print("Welcome to the game! Good luck!")
        self.ask_for_word_type()

    def ask_for_word_type(self):
        word_type_options = ("adjective", "noun", "verb")
        print("Please choose by enter one of the following word types or random:")
        print(f"{', '.join(word_type_options)}, random\n>", end=" ")
        word_type = input()

        if word_type in word_type_options:
            self.get_word(word_type)
        elif word_type in ("random", "rnd", "r"):
            word_type = choice(word_type_options)
            self.get_word(word_type)
        else:
            print("You entered an invalid option, please verify.")
            self.ask_for_word_type()

    def get_word(self, word_type):
        url = f"https://randomword.com/{word_type}"
        response = requests.get(url)
        content = response.content

        soup = BeautifulSoup(content, "html.parser")
        tag_name = "div"
        query = {"id": "random_word"}
        element = soup.find(tag_name, query)
        word = element.text.strip()
        self.set_up_game(word, word_type)

    def set_up_game(self, word, word_type):
        self.word = word.upper()
        self.len_of_word = len(self.word)
        self.visible = [False] * self.len_of_word
        self.not_guessed_letters = self.len_of_word

        underlines = " ".join(["_"] * self.len_of_word)

        print(f"Guessing begins! The type of the word is: {word_type}")
        print(underlines + f" \tLives: {self.lives}\t Your guesses: still nothing.")
        print("Write any ascii letters a-z or A-Z, then press enter.")
        self.guess_validator(self.lives)

    def guess_validator(self, lives):
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
                return self.game_won(lives)
            return self.guess_validator(lives)
        left_lives = lives - 1
        print(f"Letter: '{letter}' is NOT in word. :(")
        print(f"Left lives: {left_lives}")
        if left_lives == 0:
            return self.game_over()
        return self.guess_validator(left_lives)

    def game_over(self):
        print("\n\nGame over!")
        print(f"The word was: {self.word}")
        print("Good luck next time!")
        return self.restart_question()

    def game_won(self, lives):
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

    def restart_question(self):
        print("\nDo you want to start a new game? Press: y.")
        print("Do you want to exit the program? Press: n.")
        print("> ", end="")
        is_restart = input()
        if is_restart == "y":
            print("\n")
            self.__init__()
            return self.ask_for_word_type()
        elif is_restart == "n":
            print("\nBye bye! I hope you will come back to play again!")
            exit()
        else:
            print("Please press 'y' if you want to start a new game or press 'n' if you want to exit the program.")
            return self.restart_question()


hangman = Hangman()
hangman.welcome()
