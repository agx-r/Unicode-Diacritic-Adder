import unicodedata
import pyperclip

def add_diacritics(base_character):
    """
    Adds combinable diacritics to a base character using Unicode codes.
    Copies the result to the clipboard.

    Parameters:
    - base_character: The base character to which diacritics will be added.

    Example:
    add_diacritics('a')  # Adds diacritics to 'a'
    """
    # Define the range of diacritic codes
    diacritic_range = range(0x0300, 0x036F + 1)

    # Combine diacritics with the base character
    combined_character = base_character + ''.join(chr(code) for code in diacritic_range)

    # Copy the result to the clipboard
    pyperclip.copy(combined_character)

if __name__ == "__main__":
    # Example usage
    base_character = input("Base character: ")

    add_diacritics(base_character)
    result = pyperclip.paste()
    print(f"Result: {result}")  # Output the result from the clipboard
