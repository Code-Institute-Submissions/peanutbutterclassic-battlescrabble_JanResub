import random 
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
    
board = [] 

for x in range(0, 10):
    board.append(["0"] * 10)

    # Create function to build grid for battle.
    def print_board(board):
        """
        Create function to build grid for battle.
        """

        for i in board:
            print(" ".join(i))
    print("You are entering battle perimetre!")
    print("Fire right away!\n")    
    print_board(board)

class Battle_Ships:
    """
    Create battleships length 3, 4 and 5
    """
    def battleships(self, ship_three, ship_four, ship_five):

    

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
battleships = []






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
    
three_letter_words()


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
    
four_letter_words()

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
     
five_letter_words()

# board = []

# for x in range(0, 10):
#     board.append(["0"] * 10)

# def print_board(board):
#     for i in board:
#         print(" ".join(i))
# print("You are entering battle perimetre!")
# print("Fire right away!\n")    
# print_board(board)

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
