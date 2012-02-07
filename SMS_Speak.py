__author__ = '15597601'
import re
spaces = re.compile(r'\s')                          # Matches whitespace chars
punctuation = re.compile(r'\W')                     # Matches non-alphanumeric character
vowels = re.compile(r'\B[aeuoi]\B')                 # Matches all vowels not on the word boundaries
doubles = re.compile(r'([a-z])\1')                  # Matches the same alphabetic chars next to each other

text = raw_input('Enter some text: ')
text = text.lower()                                 # Changes the text into all lowercase

words = spaces.split(text)                          # Creates a list, separating words based on whitespace
stripwords = []
for word in words:                                  # For every word
    nopunct = punctuation.sub('',word)              # Remove punctuation
    novowels = vowels.sub('',nopunct)               # Remove the vowels
    double = doubles.search(novowels)               # Search for duplicate chars
    if double:
        nodoubles = doubles.sub(r'\1',novowels)     # If duplicates found, replace it with one of the same character
        stripwords.append(nodoubles)                # Add the modified word to a new list
    else:
        stripwords.append(novowels)


print ' '.join(stripwords)                          # Display the new list with spaces in between.
