# Hangman
This is a text-based Hangman game.

## Version 2.0
Changes

Added:
- messages like greetings
- get word from: https://randomword.com/
- option to choose exact word types
- option to choose random word type

Modified:
- object partition

### Prerequisites
Download and Install python 3.8.2.

Do not forget to add to the path.
```
https://www.python.org/downloads/
```

New required packages to install:
- requests
- beautifulsoup4

## Game description
First, you have to chose a word type or ask the program to randomly chose one for you.

It will print "_" for each letter in that word.

Then you can write any letter a-z or A-Z to guess that word.

At the start, you have a total of 9 lives.

When you enter a letter that is not in the chosen word, you lose 1 life.
If you guess correctly all the containing letters before you lose all of your lives, you won the game and a virtual beer.