# Morse Code Translator Project

# Morse Code Dictionary
morse_dict = {
    'a': '=.===',
    'b': '===.=.=.=',
    'c': '===.=.===.=',
    'd': '===.=.=',
    'e': '=',
    'f': '=.=.===.=',
    'g': '===.===.=',
    'h': '=.=.=.=',
    'i': '=.=',
    'j': '=.===.===.===',
    'k': '===.=.===',
    'l': '=.===.=.=',
    'm': '===.===',
    'n': '===.=',
    'o': '===.===.===',
    'p': '=.===.===.=',
    'q': '===.===.=.===',
    'r': '=.===.=',
    's': '=.=.=',
    't': '===',
    'u': '=.=.===',
    'v': '=.=.=.===',
    'w': '=.===.===',
    'x': '===.=.=.===',
    'y': '===.=.===.===',
    'z': '===.===.=.=',
    '1': '=.===.===.===.===',
    '2': '=.=.===.===.===',
    '3': '=.=.=.===.===',
    '4': '=.=.=.=.===',
    '5': '=.=.=.=.=',
    '6': '===.=.=.=.=',
    '7': '===.===.=.=.=',
    '8': '===.===.===.=.=',
    '9': '===.===.===.===.=',
    '0': '===.===.===.===.===',
    '.': '=.===.=.===.=.===',
    ',': '===.===.=.=.===.===',
    '?': '=.=.===.===.=.=',
    "'": '=.===.===.===.===.=',
    '!': '===.=.===.=.===.===',
    '/': '===.=.=.===.=',
    '(': '===.=.===.===.=',
    ')': '===.=.===.===.=.===',
    '&': '=.===.=.=.=',
    ':': '===.===.===.=.=.=',
    ';': '===.=.===.=.===.=',
    '=': '===.=.=.=.===',
    '+': '=.===.=.===.=',
    '-': '===.=.=.=.=.===',
    '_': '=.=.===.===.=.===',
    '"': '=.===.=.=.===.=',
    '$': '=.=.=.===.=.=.===',
    '@': '=.===.===.=.===.=',
    'char_space': '...',
    'word_space': '.'
}

# Input a string, lowercase all letters
input_str = input("Enter the word/phrase/sentence to translate:\n")
input_str = input_str.lower()

# Lists to handle translation
letter_list = []
morse_list = []

# Translate full input string
for letter in input_str:

    # Replace blank spaces with word_space found in dictionary
    if letter == ' ':
        letter = 'word_space'

    # Add Letter to list of letters
    letter_list.append(letter)

    # Translate each letter to morse code and add to translated list
    morse_list.append(morse_dict[f'{letter}'])

# Join translated list into translated string
morse_str = morse_dict['char_space'].join(morse_list)
print(morse_str)
