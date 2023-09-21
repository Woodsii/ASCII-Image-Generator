from PIL import Image
import numpy as np
import math

# maps pixel to brightness value based on RGB average
def avg(pixel):
    return (pixel[0] + pixel[1] + pixel[2])/3

# maps pixel to brightness value based on average of the extremes in RGB of pixel
def bright(pixel):
    return (max(pixel) + min(pixel))/2

# maps pixel to brightness based on luminosity
def lumin(pixel):
    return (pixel[0]*0.12 + pixel[1]*0.71 + pixel[2]*0.07) 

# clear the terminal a lil
print("\n\n\n")
bm = "`^\",:;Il!i~+_-?][}{1)(|\\/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$" # inits the chars in order of brightness
# prompts the user for an image
file_in = input("Input the filename: ")

# tests user input for errors
try: 
    im = Image.open(file_in,'r')
except: 
    print("file name not recognized, input an image in this repository!")
    exit(1) # not best practice (I think), but I wanted the output to be pretty

# prompts the user for a method of brightness mapping
mode = -1
mode = input("input 1,2 or 3 to select a method of mapping:\n1: average of each pixels RGB values\n\
2: average of the brightest and dimmest RGB values\n\
3: luminosity based on human perception\n:")

while (mode not in ['1','2','3']) : # yummy error correction
    print("\nInput error: expected a value from 1 to 3")
    mode = input("input 1,2 or 3 to select a method of mapping:\n1: average of each pixels RGB values\n\
2: average of the brightest and dimmest RGB values\n\
3: luminosity based on human perception\n:")

# casting the string user input as an int
mode = int(mode)

# resizes the image to fit a command line interface
print("\nimage successfully loaded!\nSize: ", im.size)
im = im.resize((200,200)) 
size = im.size

# inits the two matrixes
im_matrix = np.array(im.getdata()) # holds the rgb tuples
val_matrix = np.empty(size[0]*size[1]) # holds the ascii representations of each pixel

# calculates each pixels brightness value, each indexed with x + y * (# of rows)
for x in range(0, size[0]): 
    for y in range(0, size[1]):
        pix = im_matrix[(x+ (y * size[0]))] # pix holds the pixel's rgb touple

        # val stores an int value of the brightness calculated by the formula set by the user input
        if (mode == 1):
            val = avg(pix)
        elif (mode == 2):
            val = bright(pix)
        else:
            val = lumin(pix)

        # total possible pixel values range from 0 -> 255, amount of ascii characters is 70
        # converts pixel value to a value between 0 and 69 to match with a ascii char
        val_matrix[x + y*size[0]] = int(((math.ceil(val))/255) * 64)

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
