import random
import time
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("battleship-words")

# Create game introduction 
def battle_intro():
    print("----------Welcome to BattleScrabble!----------")
    name = input("What's your name? \n")
    age = int(input("What's your age: \n"))
    if age >= 18:
        print("You are eligible to enter the battlefield.")
    else:
        print(f"Hello {name.capitalize()}, you are too young to play this game. Please check with your parents first.")


def enter_battle_perimeter():
    print("YOU ARE ENTERING THE BATTLE PERIMETER!\n")


def three_letter_words():
    """
    Retrieve a randomised three letter word from data in google sheet.
    """
    print("Select one word from the list to sink the ship.")
    print("Guess the word with #letter = length of ship.")
    print("For example: arc\n")

    battle_words = SHEET.worksheet("battle-words")
    data = battle_words.col_values(1)
    print(data)

    # Input method shall have \n for heroku compatibility.
    user_three_str = input("Choose your word wisely to sink the ship: \n")
    print(f"You have selected {user_three_str}")
    if user_three_str == linked_words:
        print("You sunk the ship")
    else:
        print("You missed!")


def four_letter_words():
    """
    Retrieve a randomised three letter word from data in google sheet.
    """
    print("Select one word from the list to sink the ship.")
    print("Guess the word with #letter = length of ship.")
    print("For example: beer\n")

    battle_words = SHEET.worksheet("battle-words")
    data = battle_words.col_values(2)
    print(data)
    # Input method shall have \n for heroku compatibility.
    user_four_str = input("Choose your word wisely to sink the ship: \n")
    print(f"You have selected {user_four_str}")
    if user_four_str == linked_words:
        print("You sunk the ship")
    else:
        print("You missed!")


def five_letter_words():
    """
    Retrieve a randomised three letter word from data in google sheet.
    """
    print("Select one word from the list to sink the ship.")
    print("Guess the word with #letter = length of ship.")
    print("For example: break\n")

    battle_words = SHEET.worksheet("battle-words")
    data = battle_words.col_values(3)
    print(data)
    # Input method shall have \n for heroku compatibility.
    user_five_str = input("Choose your word wisely to sink the ship: \n")
    print(f"You have selected {user_five_str}")
    if user_five_str == linked_words:
        print("You sunk the ship")
    else:
        print("You missed!")


def get_random_word(word_length):
    """
    Randomise words to be selected by player to completely sink the ship(s).
    """
    battle_words = SHEET.worksheet("battle-words")
    words = battle_words.col_values(word_length-2)
    return random.choice(words[1:])


def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """
    Will check the row or column to see if it is safe to place a ship there
    """
    global grid
    global ship_positions

    all_valid = True
    for r in range(start_row, end_row):
        for c in range(start_col, end_col):
            if grid[r][c] != ".":
                all_valid = False
                break
    if all_valid:
        ship_positions.append([start_row, end_row, start_col, end_col])
        for r in range(start_row, end_row):
            for c in range(start_col, end_col):
                grid[r][c] = "O"
    return all_valid


def try_to_place_ship_on_grid(row, col, direction, length):
    """
    Call helper method to try and place a ships on the grid.
    """
    global grid_size

    start_row, end_row, start_col, end_col = row, row + 1, col, col + 1
    if direction == "left":
        if col - length < 0:
            return False
        start_col = col - length + 1

    elif direction == "right":
        if col + length >= grid_size:
            return False
        end_col = col + length

    elif direction == "up":
        if row - length < 0:
            return False
        start_row = row - length + 1

    elif direction == "down":
        if row + length >= grid_size:
            return False
        end_row = row + length

    return validate_grid_and_place_ship(start_row, end_row, start_col, end_col)


def create_grid():
    """Will create a 10x10 grid and randomly place down ships
       of different sizes in different directions"""
    global grid
    global grid_size
    global num_of_ships
    global ship_positions
    global linked_words

    random.seed(time.time())

    rows, cols = (grid_size, grid_size)

    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(".")
        grid.append(row)

    num_of_ships_placed = 0

    ship_positions = []

    while num_of_ships_placed != num_of_ships:
        random_row = random.randint(0, rows - 1)
        random_col = random.randint(0, cols - 1)
        direction = random.choice(["left", "right", "up", "down"])
        ship_size = random.randint(3, 5)
        if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
            num_of_ships_placed += 1
            linked_word = get_random_word(ship_size)
            linked_words.append({'row': random_row, 'col': random_col, 'word': linked_word})


def print_grid():
    """Will print the grid with rows A-J and columns 0-9"""
    global grid
    global alphabet

    debug_mode = True

    alphabet = alphabet[0: len(grid) + 1]

    for row in range(len(grid)):
        print(alphabet[row], end=") ")
        for col in range(len(grid[row])):
            if grid[row][col] == "O":
                if debug_mode:
                    print("O", end=" ")
                else:
                    print(".", end=" ")
            else:
                print(grid[row][col], end=" ")
        print("")

    print("  ", end=" ")
    for i in range(len(grid[0])):
        print(str(i), end=" ")
    print("")

# Firing


# Global variable for grid
grid = [[]]
# Global variable for grid size
grid_size = 10
# Global variable for number of ships to place
num_of_ships = 3
# Global variable for bullets left
bullets_left = 50
# Global variable for game over
game_over = False
# Global variable for number of ships sunk
num_of_ships_sunk = 0
# Global variable for ship positions
ship_positions = [[]]
# Global variable for alphabet
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

linked_words = []


def main():
    battle_intro()
    enter_battle_perimeter()
    create_grid()
    print_grid()
    print(linked_words)
    three_letter_words()
    four_letter_words()
    five_letter_words()


if __name__ == '__main__':
    main()