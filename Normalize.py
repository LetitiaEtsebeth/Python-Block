name = raw_input('Enter the file name: ')
newname = raw_input('Enter the name to create the file: ')

file = open(name)
newfile = open(newname,'w')                     # Creates a newfile in which to store output

for line in file:
    linelist = line.lower().split()             # Only adds the words to a list                   
    if linelist:                                # If the list is not empty it writes it to the new file with a single space in between
        newfile.write(' '.join(linelist)+' ')
