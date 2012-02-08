# 15597601

original_name = raw_input('Enter the original file name: ')
sms_name = raw_input('Enter the decoded file name: ')

original = open(original_name)
sms = open(sms_name)
wordcount = 0                                                   # Counts the amount of words
correctcount = 0                                                # Counts the amount of correct words

originallines = original.readlines()                            # Creates a list containing each line from the file
smslines = sms.readlines()
for lineno in range(len(originallines)):                        # Generates index numbers
    originalwords = originallines[lineno].split()               # Creates a list containing the words in each line
    smswords = smslines[lineno].split()
    for word in range(len(originalwords)):                      # Generates index numbers
        if originalwords[word] == smswords[word]:               # Words in the same position
            wordcount += 1
            correctcount += 1
        else:
            wordcount += 1

accuracy = correctcount/float(wordcount)*100
print accuracy,'%'

    
