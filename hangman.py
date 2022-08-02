
# Write your code here
import random
import string

times_won, times_lost = 0, 0


# Runs the game, it's the main masterpiece. It returns the number of wins and loses
def play(wins, loses):
    words = ["python", "java", "swift", "javascript"]
    word_choice = random.choice(words)
    hint = "-" * len(word_choice)
    print('H A N G M A N -- 1.0.0')
    guess_value = 1
    guess_list, fail_list = [], []
    while guess_value <= 8:  # gives the player 8 chances only for guessing the characters
        print("\n{}".format(hint))
        guess_letter = input("Input a letter: ")
        if len(guess_letter) != 1:
            print("Please, input a single letter.")
        elif guess_letter not in string.ascii_lowercase:
            print("Please, enter a lowercase letter from the English alphabet.")
        else:
            if guess_letter not in word_choice:
                if guess_letter not in fail_list:
                    fail_list.append(guess_letter)
                    print("That letter doesn't appear in the word.")
                    guess_value += 1
                else:
                    print("You've already guessed this letter.")
            else:
                if guess_letter in guess_list:
                    print("You've already guessed this letter.")
                else:
                    guess_list.append(guess_letter)
                    hint = "".join([a_char if a_char in guess_list else "-" for a_char in word_choice])
                    if hint == word_choice:
                        print(f"\nYou guessed the word {hint}!")
                        break

    if hint == word_choice:
        print("You survived!")
        wins += 1
    else:
        print("\nYou lost!")
        loses += 1
    return wins, loses


# The game call, controls the menu and its activities
def the_game(wins, loses):
    while True:
        selection_list = ['1', '2', '3']
        print('Type \n1. To play the game, \n2. To show the scoreboard, and \n3. To quit: ')
        selection = input()
        if selection in selection_list:
            if selection == selection_list[0]:
                wins, loses = play(wins, loses)
            elif selection == selection_list[1]:
                print(f"You won: {wins} times\nYou lost: {loses} times")
            else:
                print("Exiting...")
                break


# Execution call
if __name__ == "__main__":
    the_game(times_won, times_lost)
