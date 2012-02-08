__author__ = '15597601'
import re, time
vow_punc = re.compile(r'(\B[aeuoi]\B)|[^a-zA-Z0-9\s]')      # Matches non-alphanumeric and spaces chars or vowels not on the word boundaries           
doubles = re.compile(r'([a-z])\1')                          # Matches the same alphabetic chars next to each other

def sms(text):
    text = text.lower().strip()                             # Changes the text into all lowercase and strips the whitespace
    strip = vow_punc.sub('',text)                           # Replace punctuation and the vowels with an empty string
    strip = doubles.sub(r'\1',strip)                        # Replace duplicates with one of the same character
    return strip          


text = raw_input('Enter the text you want to add to the dictionary: ')
sms_dict = {}

inputfile = open(text)
for line in inputfile:
    for word in line.split():                               # Splits the line into words
        sms_dict.update({sms(word):word})                   # Translates the word to sms and then adds it to the dictionary if the key can not be found

print sms_dict

inputfile.close()
