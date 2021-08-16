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

# Create battle grid (10x10) using initial empty sting.
# board = []

# for x in range(0, 10):
#     board.append(["0"] * 10)

#     # Create function to build grid for battle.
#     def print_board(board):
#         """
#         Create function to build grid for battle.
#         """

#         for i in board:
#             print(" ".join(i))
#     print("You are entering the battle perimetre!")
#     print("Fire right away!\n")    
#     print_board(board)

# class Battle_Ships:
#     """
#     Create battleships length 3, 4 and 5
#     """
#     def battleships(self, ship_three, ship_four, ship_five):


    

#     while num_of_ships_placed != num_of_ships:
#         random_row = random.randint(0, rows - 1)
#         random_col = random.randint(0, cols - 1)
#         direction = random.choice(["left", "right", "up", "down"])
#         ship_size = random.randint(3, 5)
#         if try_to_place_ship_on_grid(random_row, random_col, direction, ship_size):
#             num_of_ships_placed += 1

# battle_perimeter()

# Create battle ships.
# Three types of ships: (1) ship with length = 3 (2) ship with length = 4 (3) ship with length = 5.
# battleships = []

# Create a function to retrieve a random word from each column in the worksheet.
"""
Function is duplicated three times for (1) three letter word (2) four letter word (3) five letter word.
"""

def three_letter_words():
    """
    Retrieve a randomised three letter word from data in google sheet.
    Get user to select a word from the list provided to sink the ship completely.
    If selection matches the word, the ship will sink. If not, user is given another chance until the right word is selected.
    """
    print("Select one word from the list to sink the ship.")
    print("The number of letters in the word must match the number of grids that the ship in target occupies.")
    print("For example: arc\n")

    battle_words = SHEET.worksheet("battle-words")
    data = battle_words.col_values(1)
    print(data)

    # Input method shall have \n for heroku compatibility.
    user_three_str = input("Choose your word wisely to sink the ship: \n")
    print(f"You have selected {user_three_str}") 


def four_letter_words():
    """
    Retrieve a randomised three letter word from data in google sheet.
    Get user to select a word from the list provided to sink the ship completely.
    If selection matches the word, the ship will sink. If not, user is given another chance until the right word is selected.
    """
    print("Select one word from the list to sink the ship.")
    print("The number of letters in the word must match the number of grids that the ship in target occupies.")
    print("For example: arc\n")

    battle_words = SHEET.worksheet("battle-words")
    data = battle_words.col_values(2)
    print(data)
    
    # Input method shall have \n for heroku compatibility.
    user_four_str = input("Choose your word wisely to sink the ship: \n")
    print(f"You have selected {user_four_str}")


def five_letter_words():
    """
    Retrieve a randomised three letter word from data in google sheet.
    Get user to select a word from the list provided to sink the ship completely.
    If selection matches the word, the ship will sink. If not, user is given another chance until the right word is selected.
    """
    print("Select one word from the list to sink the ship.")
    print("The number of letters in the word must match the number of grids that the ship in target occupies.")
    print("For example: arc\n")

    battle_words = SHEET.worksheet("battle-words")
    data = battle_words.col_values(3)
    print(data)
    
    # Input method shall have \n for heroku compatibility.
    user_five_str = input("Choose your word wisely to sink the ship: \n")
    print(f"You have selected {user_five_str}")
    has_five = user_five_str in data


# three_letter_words()
# five_letter_words()
# four_letter_words()

def get_random_word(word_length):
    battle_words = SHEET.worksheet("battle-words")
    words = battle_words.col_values(word_length-2)
    return random.choice(words[1:])

# FIVE_LETTER_WORDS = get_words(3)
# word = random.choice(FIVE_LETTER_WORDS[1:])
# jumble = ""
# while word:
#     position = random.randrange(len(word))
#     jumble += word[position]
#     word = word[:position] + word[(position + 1):]
# print(
# """
#       Welcome to WORD JUMBLE!!!

#       Unscramble the leters to make a word.
#       (press the enter key at prompt to quit)
#       """
#       )
# print("The jumble is:", jumble)


# def print_grid():
#     """Will print the grid with rows A-J and columns 0-9"""
#     global grid
#     global alphabet

#     debug_mode = True

#     alphabet = alphabet[0: len(grid) + 1]

#     for row in range(len(grid)):
#         print(alphabet[row], end=") ")
#         for col in range(len(grid[row])):
#             if grid[row][col] == "O":
#                 if debug_mode:
#                     print("O", end=" ")
#                 else:
#                     print(".", end=" ")
#             else:
#                 print(grid[row][col], end=" ")
#         print("")

#     print("  ", end=" ")
#     for i in range(len(grid[0])):
#         print(str(i), end=" ")
#     print("")

def validate_grid_and_place_ship(start_row, end_row, start_col, end_col):
    """Will check the row or column to see if it is safe to place a ship there"""
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
    """Based on direction will call helper method to try and place a ship on the grid"""
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
            linked_words.append({ 'row': random_row, 'col': random_col, 'word': linked_word })



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
    create_grid()
    print_grid()
    print(linked_words)


if __name__ == '__main__':
    main()