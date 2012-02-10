__author__ = '15597601'

# Letitia Etsebeth
''' Research
express = re.compile("[A-Z]+", re.IGNORECASE)
objek = express.finditer(',tempo,temp')
for item in objek:
    print item.group(),',',
#[\w^0-9] # Alphanumeric [A-N]*
([A-M])([N-Z])

print re.search(r'[a-z]+', re.IGNORECASE,'Tempo').group()
express = re.compile("((?:[A-M]*)|(?:[N-Z]*)*)", re.IGNORECASE)
print express.sub(lambdax:dict[x],',tempo:)')
print express.search('TEMFFFZPO').groups()
line = 'hello'
p = re.compile('^rot13:(.*)')
print p.search('hello')
print line.encode('rot13')'''

# Question 2
'''
original = raw_input('Enter the string you want to encode/decode: ')
code = ''

for letter in original:
    if letter.upper() >= 'A' and letter.upper() <= 'M':
        code += chr(ord(letter)+13)
    elif letter.upper() >= 'N' and letter.upper() <= 'Z':
        code += chr(ord(letter)-13)
    else:
        code += letter

print 'Result:', code
'''

# Question 3
'''
import re

def rot13(text):
    letter = text.group().upper()
    if letter >= 'A' and letter <= 'M':
        return chr(ord(text.group())+13)
    elif letter >= 'N' and letter <= 'Z':
        return chr(ord(text.group())-13)

express = re.compile('[A-Z]', re.IGNORECASE)
print 'Result: ', express.sub(rot13,original)
'''

# Question 4

def en_asciibit(original):
    code = ''
    for letter in original:                     # To add all the binary numbers to one long string
        binary = bin(ord(letter))               # Converts the ascii number to the binary representation in string starting with 0b
        code += binary[2:].rjust(8,'0')         # Padds the number from the 2d index to the end with 0's to the left to make a byte and adds it to the string

    if len(code) % 3 == 0:                      # If the length is devisible by 3 nothing needs to be added.
        return code
    elif len(code)%3 == 1:                      # If there was only one byte out of three, that byte is padded with 0's to make it 6bits long and 1 '=' to account for the other two bytes
        code += ('0'*(6-(len(code)%6)))+'='
        return code
    elif len(code)%3 == 2:                      # If there was two byte present, the late byte is padded with 0's to make it 6bits long and 2 '=' to account for the other missing byte
        code += ('0'*(6-(len(code)%6)))+'=='
        return code
    

def en_basebit(code):
    binaryli = list(code)               # Splits the string of code into a list 
    bit6 = ''
    baseli = []

    while len(binaryli) > 0:
        if len(binaryli) >= 6:
            for x in range(6):          # Adds 6 bits together
               bit6 += binaryli[0]   
               del binaryli[0]
            baseli.append(bit6)
            bit6 = ''
        else:                           # If there are less than 6 bits left it just appends the last items and deletes them
            bit6 = binaryli[0]
            del binaryli[0]
            baseli.append(bit6)
    return baseli                       #Containing the items of 6 bits each

def en_message(baselist):
    encode = ''
    for byte in baselist:
        if byte != '=':
            num = int(byte,base=2)              # Converts the binary into an integer
            if num == 62:                       # '+' ascii: 43 Base64: 62
                encode += chr(43)
            elif num == 63:                     # '/' ascii: 47 Base64: 63
                encode += chr(47)
            elif num >= 0 and num <= 25:        # 'A' - 'Z' ascii: 65 - 90 Base64: 0 - 25
                encode += chr(num + 65)
            elif num >= 26 and num <= 51:       # 'a' - 'z' ascii: 97 - 122 Base64: 26 - 51
                encode += chr(num + 71)
            elif num >= 52 and num <= 61:       #  '0' - '9' ascii: 48 - 57 Base64: 52 - 61
                encode += chr(num - 4)
        else:
            encode += byte                      # Adds the '=' sign to the end of the encoded message
    return encode

def encode(text):
    asciibitpattern = en_asciibit(text)                 # Step1 - Convert the chars into a string containing their binary representation in 8 bits each             
    basebitpattern = en_basebit(asciibitpattern)        # Step2 - Divide the ascii bitpattern into blocks of 6 bits
    return en_message(basebitpattern)                   # Step3 - Convert the 6bits into integers and get their Base64 Representation Chars

    
def de_index(text):
    index = []
    for letter in text:
        ascii = ord(letter)                     # Gets the ascii value of the integer
        if ascii == 43:                         # '+' ascii: 43 Base64: 62                         
            index.append(62)
        elif ascii == 47:                       # '/' ascii: 47 Base64: 63
            index.append(63)                    
        elif ascii >= 65 and ascii <= 90:       #'A' - 'Z' ascii: 65 - 90 Base64: 0 - 25
            index.append(ascii - 65)
        elif ascii >= 97 and ascii <= 122:      #'a' - 'z' ascii: 97 - 122 Base64: 26 - 51
            index.append(ascii -71)
        elif ascii >= 48 and ascii <= 57:       #'0' - '9' ascii: 48 - 57 Base64: 52 - 61
            index.append(ascii+ 4)
    return index

def de_basebit(indexlist):
    code = ''
    for item in indexlist:                      # To add all the binary numbers to one long string
        binary = bin(item)                      # Converts the integer to the binary representation in string starting with 0b
        code += binary[2:].rjust(6,'0')         # Padds the number from the 2d index to the end with 0's to the left to make 6 bits and adds it to the string
    return code

def de_asciibit(code):
    binaryli = list(code)               # Split the bit pattern into a list
    byte = ''
    byteli = []

    while len(binaryli) >= 8:           # While there are more than 7 bits in the list
        for x in range(8):              # Concatenate the first 8 bits together 
            byte += binaryli[0]
            del binaryli[0]
        byteli.append(byte)             # Add the byte to a new list
        byte = ''
    return byteli

def de_message(bytelist):
    message = ''
    for item in bytelist:
        ascii = int(item,base=2)        # Convert the binary numbers to integers
        message += chr(ascii)           # Get the appropriate ASCII character and concatenate them together
    return message
        
    
def decode(text):
    index = de_index(text)                      # Step1 - Acquires the Base64 index numbers 
    basepattern = de_basebit(index)             # Step2 - Convert the index numbers into binary 6bit bytes, padding 0's to the front if neccesary
    asciipattern = de_asciibit(basepattern)     # Step3 - Reconsturct 8 bit bytes from the pit pattern
    return de_message(asciipattern)             # Step4 - Convert the bytes to integers and then to the ascii character

while True:
    text =''
    print 'What do you want to do?'
    print 'Enter 1 to encode the file'
    print 'Enter 2 to decode the file'
    print 'Type "exit" to exit'
    userinput = raw_input('>> ')

    if userinput == '1':
        original = open('original.txt')
        for line in original:                   # Reads all the text out of the file
            text += line
        original.close()
        
        encoding = open('encoding.txt','w')
        encoding.write(encode(text))            # Writes the encoded text to a new textfile
        print 'Encoding has been successful'
        encoding.close()
    elif userinput == '2':
        original = open('original.txt')         # Reads all the text out of the file
        for line in original:
            text += line
        original.close()

        decoding = open('decoding.txt','w')
        decoding.write(decode(text))            # Writes the encoded text to a new textfile
        print 'Decoding has been successful'
        decoding.close()
    elif userinput == 'exit':
        break
    else:
        print 'You entered an invalid option.'
    print '\n'
  





