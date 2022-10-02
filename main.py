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

# Translate full input string to a python list of characters
for letter in input_str:
    letter_list.append(letter)

# Translate each letter to morse code equivalent
for char in letter_list:
    if char == ' ':
        char = 'word_space'
    morse_list.append(morse_dict[f'{char}'])

# Join and append morse code list
morse_str = morse_dict['char_space'].join(morse_list)
print(morse_str)
