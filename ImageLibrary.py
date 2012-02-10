import Image, ImageFilter, ImageEnhance


def saveimage(newpic):
    newname = raw_input('To save enter a new picture name (none to exit): ')
    if newname != 'none':
        newpic.save(newname)                                                    # Saves the changed picture under a new name                                               
        print 'New picture saves successfully'
    

print 'Welcome!'
picname = raw_input('Enter the name of the pic you want to manipulate: ')
try:
    pic = Image.open(picname)                                                       # Create the object
    pic.show()
    user = ' '
except:
    print 'The image does not exist'
    user == 'exit'
            
while user != 'exit':
    
    print 'Choose a option: '
    print 'Press (1) to open another picture'
    print 'Press (2) to convert to Greyscale'
    print 'Press (3) to Crop'
    print 'Press (4) to Filter'
    print 'Press (5) to Transpose'
    print 'Press (6) to enhance the Color'
    print 'Press (7) to blend with another picture'
    print ''

    user = raw_input('>> ')
    if user == '1':
        picname = raw_input('Enter the name of the pic you want to manipulate: ')
        try:                                                                        # Exception clause if the file can't be found    
            pic = Image.open(picname)                                               # Create the object
            pic.show()
        except:
            print 'The image does not exist'
            user == 'exit'
    elif user == '2':
        greypic = pic.convert('L')                                                  # 'L' = Greyscale
        greypic.show()
        saveimage(greypic)                                                          # Calls function to save the changed picture
    elif user == '3':
        left = raw_input('Enter the top left coordinate: ')                     
        right = raw_input('Enter the bottom right coordinate: ')
        if left.isdigit() and right.isdigit():
            left = int(left)
            right = int(right)
            if left > right:                                                        # Ensure that two points can be found
                box = (left,left,right,right)                                       # Coordinates to ensure symetry
            else:
                box = (left, left, right+50, right+50)
        else:
            box = (50,50,100,100)                                                   # Uses the default if user does not enter a valid argument
        region = pic.crop(box)
        region.show()
        saveimage(region)                                                           
    elif user == '4':                                                               # The filter module is used to apply a blurred or embossed effect on the image
        print 'Press (1) to display a Blurred picture'
        print 'Press (2) to display a Embossed picture'
        choice = raw_input('>> ')
        if choice == '1':
            picblr = pic.filter(ImageFilter.BLUR)
            picblr.show()
            saveimage(picblr)
        elif choice == '2':
            piceb = pic.filter(ImageFilter.EMBOSS)
            piceb.show()
            saveimage(piceb)
    elif user == '5':                                                               # This will either transpose, rotate or resize an image  
        print 'Press (1) to Rotate 90'
        print 'Press (2) flip on Horisontal axis'
        print 'Press (3) flip on Vertical axis'
        print 'Press (4) to Resize'
        choice = raw_input('>> ')
        if choice == '1':
            rotate = pic.transpose(Image.ROTATE_90)                                 # The image is rotated 90 anti-clockwise
            rotate.show()
            saveimage(rotate)
        elif choice == '2':
            fliph = pic.transpose(Image.FLIP_TOP_BOTTOM)                            # The image is fliped top over end
            fliph.show()
            saveimage(fliph)
        elif choice == '3':
            flipv = pic.transpose(Image.FLIP_LEFT_RIGHT)                            # The image is flipped on its y-axis
            flipv.show()
            saveimage(flipv)
        elif choice == '4':
            width = raw_input('Enter the new height: ')
            height = raw_input('Enter the new width: ')
            if height.isdigit() and width.isdigit():
                size = pic.resize((int(width),int(height)))                         # The width and height values are used to determine the image size
                size.show()
                saveimage(size)
            else:
                pic.show()
    elif user == '6':
        color = ImageEnhance.Color(pic)
        for index in range(4):
            factor = index/4.0                                                      # Adjusts + integers to descimal between 0.0 and 1.0
            color.enhance(factor).show()
        saveimage(color)
    elif user == '7':
        name = raw_input('Enter the second image name: ')
        try:
            pic2 = Image.open(name)
        except:
            pass
        print 'Blended images need to be the same size...'
        width = raw_input('Enter the new height: ')
        height = raw_input('Enter the new width: ')
        if height.isdigit() and width.isdigit():
            size1 = pic.resize((int(width),int(height)))                         # The width and height values are used to determine the image size
            size2 = pic2.resize((int(width),int(height)))
        else:
            print 'You need to enter integers'
            pass                                                                 # If the user did not enter integers
        blended = Image.blend(size1,size2,10)
        blended.show()
            
        
 
        
        
        

