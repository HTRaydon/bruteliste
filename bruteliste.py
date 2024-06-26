#!/usr/bin/python3
import argparse
import itertools
import string

# Define the command-line arguments
parser = argparse.ArgumentParser(description="Generates variations of words in an input file.",epilog="You can add wildcards just like hashcat in your input file: ?l for lowercases; ?u for uppercases; ?L for letter; ?d for digits; ?s for special characters; ?a for all characters")
parser.add_argument('-if', '--input-file', required=True, help='the file containing the words to generate variations for')
parser.add_argument('-of', '--output-file', required=True, help='the file to write the variations to')
args = parser.parse_args()

# Read the words from the input file
with open(args.input_file, 'r') as f:
    words = f.read().splitlines()

# The characters that each character in the words can be replaced with
REPLACEMENTS = {
    'a': 'aA4@',    #A
    'A': 'aA4@',
    'b': 'bB8',     #B
    'B': 'bB8',
    'c': 'cC',      #C
    'C': 'cC',
    'd': 'dD',      #D
    'D': 'dD',
    'e': 'eE3€',    #E
    'E': 'eE3€',
    'f': 'fF',      #F
    'F': 'fF',
    'g': 'gG6',     #G
    'G': 'gG6',
    'h': 'hH',      #H
    'H': 'hH',
    'i': 'iI1!|l',  #I
    'I': 'iI1!|l',
    'j': 'jJ',      #J
    'J': 'jJ',
    'k': 'kK',      #K
    'K': 'kK',
    'l': 'lLI£',    #L
    'L': 'lLI£',
    'm': 'mM',      #M
    'M': 'mM',
    'n': 'nN',      #N
    'N': 'nN',
    'o': 'oO0',     #O
    'O': 'oO0',
    'p': 'pP',      #P
    'P': 'pP',
    'q': 'qQ',      #Q
    'Q': 'qQ',
    'r': 'rR',      #R
    'R': 'rR',
    's': 'sS5$',    #S
    'S': 'sS5$',
    't': 'tT7+',    #T
    'T': 'tT7+',
    'u': 'uU',      #U
    'U': 'uU',
    'v': 'vV',      #V
    'V': 'vV',
    'w': 'wW',      #W
    'W': 'wW',
    'x': 'xX',      #X
    'X': 'xX',
    'y': 'yY',      #Y
    'Y': 'yY',
    'z': 'zZ',      #Z
    'Z': 'zZ',
    '?l': string.ascii_lowercase,                                       # Add all lowercase letters
    '?u': string.ascii_uppercase,                                       # Add all uppercase letters
    '?L': string.ascii_letters,                                         # Add all letters
    '?d': string.digits,                                                # Add all digits
    '?s': string.punctuation,                                           # Add all punctuation
    '?a': string.ascii_letters + string.digits + string.punctuation,    # Add all letters, digits, and punctuation
}

# Generate variations for every word in the input file
with open(args.output_file, 'w') as f:
    for word in words:
        # Create a list of the possible replacements for each character in the word
        variations = []
        next_char = ''
        index_modif = 0
        for index in range(len(word)):
            true_index = index + index_modif
            if (true_index == len(word)):
                break
            if true_index+1 == len(word):
                char = next_char
                next_char = ''
            else:
                char = word[true_index]
                next_char = word[true_index+1]
            if char == '?' and next_char in 'alusdL':
                # Prioritize the '?a', '?u', '?l', and '?d' replacements over the corresponding individual character replacements
                if next_char == 'a':
                    variations.append(list(REPLACEMENTS['?a']))
                    index_modif += 1
                elif next_char == 'l':
                    variations.append(list(REPLACEMENTS['?l']))
                    index_modif += 1
                elif next_char == 'u':
                    variations.append(list(REPLACEMENTS['?u']))
                    index_modif += 1
                elif next_char == 's':
                    variations.append(list(REPLACEMENTS['?s']))
                    index_modif += 1
                elif next_char == 'd':
                    variations.append(list(REPLACEMENTS['?d']))
                    index_modif += 1
                elif next_char == 'd':
                    variations.append(list(REPLACEMENTS['?L']))
                    index_modif += 1
            elif char in REPLACEMENTS:
                variations.append(list(REPLACEMENTS[char]))
            else:
                variations.append([char])
            

        # Generate all possible combinations of the variations
        for combination in itertools.product(*variations):
            f.write(''.join(combination) + '\n')
