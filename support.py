from random import randint, seed
import string

seed(7030)
GUESS_LENGTH = 6
FEEDBACK_LENGTH = 6


YELLOW = 'Y'
BLACK = 'B'
GREEN = 'G'

EMPTY = '-' 
SEP = '-----------------------'


HELP_COMMAND = ["h", "H"]
QUIT_COMMAND = ["q", "Q"]
KEYBOARD_COMMAND = ["a", "A"]

WELCOME_MESSAGE = "Welcome to Weirdle!"

ENTER_COMMAND_MESSAGE = "Please enter your guess (h to see valid format): "

HELP_MESSAGE = """Valid commands: 
- Provide a 6-character word with unique lowercase letters
- a/A: Display keyboard
- h/H: Display help text
- q/Q: Quit current game\n"""

GET_NUM_GUESSES_MESSAGE = (
    "\nPlease enter the number of guesses you require to guess the secret word. "
    "Your input must be a number between 5 and 9: "
)

INVALID_FORMAT_MESSAGE = "\nInvalid guess! Guess must be 6 alphabetic characters\n"
INVALID_CHARACTERS_MESSAGE = "\nInvalid guess! Guess must consist of unique lowercase characters\n"
INVALID_GUESS_MESSAGE = "\nInvalid guess! Guess must be a word from the given file\n "

WIN_MESSAGE = "\nCongratulations! You guessed the word!"
RETRY_MESSAGE = "\n Would you like to retry? "
LOST_MESSAGE = "\nSorry, you've lost the game."

def load_words(fname: str) -> list[str]:
    """
        Load words from a text file which each line in the file is treated as a single word.
        
        Args:
            fname (str): Path to the file containing the words.

        Returns:
            (list[str]): A list of words read from the file.
    """

    all_words = []
    with open(fname, 'r') as file:
        for line in file:
            all_words.append(line.strip()) 
    return all_words


def create_keyboard() -> dict[str, str]:
    """
        Create a hint keyboard.

        Returns:
            (dict[str, str]): a hint keyboard
    """
    
    keyboard = dict()
    for letter in string.ascii_lowercase:
        keyboard[letter] = EMPTY
    return keyboard
