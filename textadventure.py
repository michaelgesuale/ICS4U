import random
import os


def greeting():
    print("\nWelcome to the forest of horrors. You are an explorer looking for gold, which is hidden inside a cave.")
    print("However, each cave is guarded by a dragon. Dragons may be either friendly or hungry. If you encounter a")
    print("hungry dragon, you will be eaten and die. If the dragon is friendly, you win.")
    print('')
    input("Choose a cave -- enter number 1 or 2: ")


def num_gen(x, y):
    return random.randint(x, y)


def main():
    greeting()
    if num_gen(1, 2) == 1:
        print("\nYou have been eaten by a hungry dragon.")
    else:
        print("\nYou have encountered a friendly dragon. You survive and get out with your treasure.")
    again = input("\nPlay again? [Y or N]: ")
    if again == 'Y':
        clear = lambda: os.system('cls')
        clear()
        main()


main()
