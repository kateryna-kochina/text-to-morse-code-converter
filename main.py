# Morse code dictionary mapping characters to their Morse code representation
morse_alphabet = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    '.': '.-.-.-',
    ',': '--..--',
    '?': '..--..',
    "'": '.-..-.',
    '!': '-.-.--',
    ':': '---...',
    ';': '-.-.-.',
    '"': '.-..-.',
    '-': '-....-',
    '/': '-..-.'
}


# Function to convert input text to Morse code
def convert_text(text):
    '''
    Convert a given text to Morse code.

    Args:
    text (str): The input text to be converted to Morse code.

    Returns:
    str: The Morse code representation of the input text.
    '''

    # Using list comprehension to convert characters to Morse code, adding 7 spaces for word separation
    return ' '.join([' '*7 if char == ' ' else morse_alphabet[char.upper()] for char in text])


# Getting user input for the text to be converted
text = input(
    'Please enter text you\'d like to be converted to the Morse code: ')
try:
    # Attempting to convert the input text to Morse code
    converted_text = convert_text(text)
    print(f'Your converted text is: {converted_text}')
except KeyError:
    # Handling the KeyError exception if a character cannot be found in the Morse alphabet
    print('Entered text cannot be converted because one of characters cannot be found in the Morse alphabet.')
