# 15597601
import cPickle as pickle                                # Import the module to steralize & desteralize objects

sms_dict = pickle.load( open( "Dictionary.p", "rb" ) )  # Imports the 'external' dictionary

name = raw_input('Enter the encoded file name: ')

code = open(name)
decode = open('trans'+name,'w')

for line in code:
    line = line.split()                                 # Words in the line
    newline =''
    for word in line:
        newline += sms_dict[word]                       # Uses the dictionary to add the english word to a new line
        newline += ' '
    decode.write(newline+'\n')                          # Writes the line to a file

code.close()
decode.close()
        
