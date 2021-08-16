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

# Create a function to retrieve a random word from each column in the worksheet.

def get_battle_words():
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

    user_three_str = input("Choose your word wisely to sink the ship: ")
    print(f"You have selected {user_three_str}\n")
    
get_battle_words()

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
