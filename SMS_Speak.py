__author__ = '15597601'
import re                  
vow_punc = re.compile(r'(\B[aeuoi]\B)|\W')          # Matches non-alphanumeric character and all vowels not on the word boundaries           
doubles = re.compile(r'([a-z])\1')                  # Matches the same alphabetic chars next to each other

text = raw_input('Enter some text: ')
text = text.lower()                                 # Changes the text into all lowercase

words = text.split()                                # Creates a list
stripwords = []
for word in words:                                  # For every word
    strip = vow_punc.sub('',word)                   # Remove punctuation and the vowels
    double = doubles.search(strip)               # Search for duplicate chars
    if double:
        nodoubles = doubles.sub(r'\1',strip)     # If duplicates found, replace it with one of the same character
        stripwords.append(nodoubles)                # Add the modified word to a new list
    else:
        stripwords.append(strip)


print ' '.join(stripwords)                          # Display the new list with spaces in between.
