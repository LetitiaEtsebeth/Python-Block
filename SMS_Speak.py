__author__ = '15597601'
import re, time
vow_punc = re.compile(r'(\B[aeuoi]\B)|[^a-zA-Z0-9\s]')  # Matches non-alphanumeric and spaces chars or vowels not on the word boundaries           
doubles = re.compile(r'([a-z])\1')                      # Matches the same alphabetic chars next to each other

name = raw_input('Enter the file name you want to encode: ')

book = open(name)
newbook = open('sms'+name,'w')

start_time = time.clock()                               # Set a variable with the starting time
stripwords = []
for text in book:
    text = text.lower().strip()                         # Changes the text into all lowercase and strips the whitespace
    strip = vow_punc.sub('',text)                       # Replace punctuation and the vowels with an empty string
    strip = doubles.sub(r'\1',strip)                    # Replace duplicates with one of the same character
    newbook.write(strip)

book.close()
newbook.close()

print time.clock() - start_time, "seconds"              # Minus the current time from the start time
