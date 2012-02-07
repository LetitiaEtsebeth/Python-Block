__author__ = '15597601'
import re, time

text = raw_input('Enter some text: ')
start_time = time.time()                            # Set a variable with the starting time

vow_punc = re.compile(r'(\B[aeuoi]\B)|\W')          # Matches non-alphanumeric character and all vowels not on the word boundaries           
doubles = re.compile(r'([a-z])\1')                  # Matches the same alphabetic chars next to each other

text = text.lower()                                 # Changes the text into all lowercase
words = text.split()                                # Creates a list
stripwords = []
for word in words:                                  # For every word
    strip = vow_punc.sub('',word)                   # Replace punctuation and the vowels with an empty string
    strip = doubles.sub(r'\1',strip)                # Replace duplicates with one of the same character
    stripwords.append(strip)

print ' '.join(stripwords)                          # Display the new list with spaces in between.

print time.time() - start_time, "seconds"           # Minus the current time from the start time
