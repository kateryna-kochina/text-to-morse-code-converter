from morse_code_converter import convert_text


# Getting user input for the text to be converted
text_to_convert = input(
    'Please enter text you\'d like to be converted to the Morse code: ')

try:
    # Attempting to convert the input text to Morse code
    print(f'Your converted text is: {convert_text(text_to_convert)}')

except KeyError:
    # Handling the KeyError exception if a character cannot be found in the Morse alphabet
    print('Entered text cannot be converted because one of characters cannot be found in the Morse alphabet.')
