# DO NOT modify or add any import statements
from support import *

ALL_WORDS = load_words("words.txt")

# Name: Nikki de Roos
# Student Number: 50195808
# Favorite Word: Petrichor
# -----------------------------------------------------------------------------


def main() -> None:
    pass


def num_hours() -> float:
    """
        Returns the number of hours spent on the assignment.
        
        Returns:
            (float): The total number of hours spent on the assignment.
    """
    return 52.0


def has_won(guess: str, target: str) -> bool:
    """
        Determines whether a guess matches the target word.

        Preconditions:
            Comparison will be case sensitive.
            There must be no numbers in the guess.
            There must be no special characters in the guess.

        Args:
            guess (str): The word guessed by the user.
            target (str): The secret word the user is trying to guess.        

        Returns:
            (bool): True if the guess matches the target, False otherwise.

        Examples:
            >>> has_won("Password", "password")
            False
    """
    return guess == target


def get_max_guesses() -> int:
    """
        Prompts user for a valid number of guesses between 5 and 9.
        
        Preconditions:
            Number must be a whole number between 5 and 9 (inclusive).
            Repeatedly prompts the user until a valid number is entered.

        Returns:
            (int): The validated number of guesses.

        Examples:
            >>> get_max_guesses()
            Please enter the number of guesses you require to guess
            the secret word. Your input must be a number between 5
            and 9: 6.0
            Please enter the number of guesses you require to guess
            the secret word. Your input must be a number between 5
            and 9: 6
            6
    """
    input_guess = input(GET_NUM_GUESSES_MESSAGE)

    while not (input_guess.isdigit() and 5 <= int(input_guess) <= 9):
        input_guess = input(GET_NUM_GUESSES_MESSAGE)

    return int(input_guess)


def create_board(max_guesses: int) -> list[tuple[str, str]]:
    """
        Generates an empty board to support the given number of guesses.

        Preconditions:
            board_size will not be negative.

        Args:
            max_guesses (int): The number of rows (turns) to create for the board.
            
        Returns:
            (list[tuple[str, str]]): A list of tuples, where each tuple contains
              two strings representing an empty guess and empty feedback.

        Examples:
            >>> create_board(6)
            [('------', '------'),
            ('------', '------'),
            ('------', '------'),
            ('------', '------'),
            ('------', '------'),
            ('------', '------')]
    """
    board = []
    empty_guess_str = EMPTY * GUESS_LENGTH
    
    for i in range(max_guesses):
        board.append((empty_guess_str, empty_guess_str))

    return board


def display_board(board: list[tuple[str, str]]) -> None :
    """
        Prints the given board to the screen in a visually appealing format.
        
        Preconditions:
            All entries in the board have exactly six characters.

        Args:
            board (list[tuple[str, str]]): A list of (guess, feedback) tuples
              showing the game state.
    """
    # Iterate through the list using enumerate to track guess numbers
    for index, (guess, feedback) in enumerate(board):
        print(SEP)
        print(f"Guess {index + 1}:  {guess}")
        print(f"Feedback: {feedback}")

    print(SEP)


def generate_secret_word() -> str:
    """
        Randomly selects a secret word from the provided word list.

        Returns:
            (str): A randomly selected word from the provided list.
    """
    random_num = randint(0, len(ALL_WORDS)-1)
    return ALL_WORDS[random_num]


def validate_input(command: str) -> bool:
    """
        Validates if a command or guess follows the required game rules.

        Preconditions:
            Command has the correct length.
            Command contains only lowercase letters.
            All letters in command are unique.
            Command is one of the words in the game’s vocabulary.

        Args:
            command (str): The string input provided by the user.
        
        Returns:
            (bool): True if the command is valid, False otherwise.

        Examples:
            >>> validate_input("Help")
            Invalid guess! Guess must be 6 alphabetic characters
            False
    """
    if command in (HELP_COMMAND + QUIT_COMMAND + KEYBOARD_COMMAND):
        return True

    # Check for correct length and alphabetic characters
    if len(command) != GUESS_LENGTH or not command.isalpha():
        print(INVALID_FORMAT_MESSAGE)
        return False

    # Check for 6 unique characters and lowercase letters
    if len(set(command)) != GUESS_LENGTH or not command.islower():
        print(INVALID_CHARACTERS_MESSAGE)
        return False

    # Check if the word is from the provided list
    if command not in ALL_WORDS:
        print(INVALID_GUESS_MESSAGE)
        return False

    return True


def get_command() -> str:
    """
        Repeatedly prompts the user until a valid command or guess is entered.
        
        Returns:
            (str): A validated string representing a game command or a 6-letter word.
    """
    while True:
        command = input(ENTER_COMMAND_MESSAGE)

        if validate_input(command):
            return command


def get_feedback(guess: str, target: str) -> str:
    """
        Compares a guess against a target word and returns feedback.
        
        Determines if the letters match in position (Green), exist elsewhere in the
          word (Yellow), or are absent (Black).

        Args:
            guess (str): The 6-letter word guessed by the player.
            target (str): The 6-letter secret word to compare against.
        
        Returns:
            (str): A string of color codes (G, Y, B) showimg the feedback.

        Examples:
            >>> get_feedback("forest", "bright")
            'BBYBBG'
    """
    feedback = ""

    for index, char in enumerate(guess):

        # Check if character is in the same position 
        if char == target[index]:
            feedback += GREEN

        # Check if character is in a different position    
        elif char in target:
            feedback += YELLOW

        # When the character is not in target word 
        else:
            feedback += BLACK

    return feedback


def update_board(board: list[tuple], guess_num: int, guess: str, target: str) -> None:
    """
        Updates the board at a specific index with the new guess and feedback.
        
        Args:
            board (list[tuple]): The list of (guess, feedback) tuples to be updated.
            guess_num (int): The current turn number (1-indexed).
            guess (str): The player's current word guess.
            target (str): The secret word used to generate feedback.
    """
    feedback = get_feedback(guess, target)
    
    index = guess_num - 1

    board[index] = (guess, feedback)


def display_keyboard(keyboard: dict[str, str]) -> None:
    """
        Prints the keyboard dictionary in a formatted 3-column layout.

        Args:
            keyboard (dict[str, str]): A dictionary mapping characters
              to their current game status.
    """
    print("Keyboard:")
    print(SEP)

    display_row = ""

    for i, char in enumerate(keyboard):

        display_row = display_row + str(char) + ": " + str(keyboard[char]) + "    "

        # For every 3 items in the dictionary
        if (i + 1) % 3 == 0:
            print(display_row)

            # Clear the list for the next row   
            display_row = ""

    # If the number of letters wasn't divisible by 3, print the final row
    if len(display_row) > 0:
        print(display_row)
            
    print(SEP)


def update_keyboard(board: list[tuple], keyboard: dict[str, str], guess_num: int) -> None:
    """
        Updates the keyboard dictionary based on the most recent guess and feedback.

        Preconditions:
            Letters already marked GREEN stay GREEN and cannot be changed.
        
        Args: 
            board (list[tuple]): The list containing all guesses and feedback tuples.
            keyboard (dict[str, str]): The dictionary tracking the status of each
              letter (a-z).
            guess_num (int): The most recent turn number used to retrieve the latest guess.
    """
    guess, feedback = board[guess_num - 1]

    for index, char in enumerate(guess):
        status = feedback[index]
        
        # Update keyboard only if the letter isn't GREEN
        if keyboard[char] != GREEN:
            keyboard[char] = status
    

def play_game() -> None:
    """
        Coordinates the gameplay loop for one game of Weirdle.

        Consists of a gamme setup phase and a game play phase.
    """
    # Initiate game setup phase
    print(WELCOME_MESSAGE)
    
    # Determine desired number of guesses
    max_guesses = get_max_guesses()

    # Generate the secret word
    target = generate_secret_word()

    # Create the game board and keyboard
    board = create_board(max_guesses)
    keyboard = create_keyboard()

    # Display current game state
    display_board(board)

    # Initiate gamme play phase loop
    guess_num = 1
    
    while guess_num <= max_guesses:
        command = get_command()

        if command in HELP_COMMAND:
            print(HELP_MESSAGE)
            continue
        
        elif command in KEYBOARD_COMMAND:
            display_keyboard(keyboard)
            continue
        
        # Return player out of the game play loop
        elif command in QUIT_COMMAND:
            return

        update_board(board, guess_num, command, target)
        update_keyboard(board, keyboard, guess_num)
        display_board(board)

        if has_won(command, target):
            print(WIN_MESSAGE)
            return

        guess_num += 1

    print(LOST_MESSAGE + f" The word was: {target}")


def main() -> None:
    """
        The entry point of the script that starts the game.
        Repeatedly launches play_game until the user decides to stop.
    """
    play_game()

    # The user is prompted to play again after every play_game()
    while True:
        
        # Ask the player if they want to play again
        retry = input(RETRY_MESSAGE)
    
        # If the player wants to play again, call play_game
        if retry in ("Y", "y"):
            play_game()

        # If the player wants to quit, break the loop and end the program
        elif retry in ("N", "n"):
            break

        
if __name__ == "__main__":
    main()    





