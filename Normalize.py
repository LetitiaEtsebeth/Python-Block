# 15597601
import re
punc = re.compile(r'[^a-zA-Z0-9\s]')

name = raw_input('Enter the file name: ')
newname = raw_input('Enter the name to create the file: ')

textfile = open(name)
newfile = open(newname,'w')                                 # Creates a newfile in which to store output

for line in textfile:
    line = line.lower()                                     # Only adds the words to a list
    line = punc.sub('',line)                                # Removes all the punctuation
    linelist = line.split()

    if linelist:                                            # If the list is not empty it writes it to the new file with a single space in between
        newfile.write(' '.join(linelist)+' ')               # Writes to the new file

textfile.close()
newfile.close()


