from PIL import Image
import numpy as np
import math
import os



# clear the terminal a lil
print("\n\n\n")
bm = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" # inits the chars in order of brightness

# opens the image and resizes accordingly
im = Image.open('n8.jpg','r')
print("image successfully loaded!\nSize: ", im.size)
im = im.resize((200,200)) 
size = im.size

# inits the two matrixes
im_matrix = np.array(im.getdata()) # holds the rgb tuples
val_matrix = np.empty(size[0]*size[1]) # holds the ascii representations of each pixel

# calculates each pixels brightness value, each indexed with x + y * (# of rows)
for x in range(0, size[0]): 
    for y in range(0, size[1]):
        pix = im_matrix[(x+ (y * size[0]))] # pix holds the pixel's rgb touple

        # val stores an int value of the brightness calculated by the formula:
        # R*0.12 + G*0.71 + B*0.07 - this maps brightness to human perception of color
        val = (pix[0]*0.12 + pix[1]*0.71 + pix[2]*0.07) 

        # total possible pixel values range from 0 -> 255, amount of ascii characters is 70
        # converts pixel value to a value between 0 and 69 to match with a ascii char
        val_matrix[x + y*size[0]] = int(((math.ceil(val))/255) * 70)

# prints the ascii chars out together
count = 0 # count is used to print the pixels out in a row.
for x in range(0, size[0]):
    for y in range(0, size[1]):
        # creates a new line for output when the end of the row is reached
        if count >= size[0]:
            count = 0
            print()
        
        # actually prints the martys out
        print(bm[int(val_matrix[x + y*size[0]])], end="")
        count += 1

# gives more space for output
print("\n\n\n")
