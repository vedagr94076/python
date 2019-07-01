from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations
import PIL

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)
height = len(img)
width = len(img[0])
for r in range(155):
    for c in range(width):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[255,0,255] # R + B = magenta
        
for r in range(420, 476):
    for c in range(130, 160):
        if sum(img[r][c])>500: # brightness R+G+B goes up to 3*255=765
            img[r][c]=[0,255,0] # R + B = magenta

def make_mask(rows, columns, radius):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    img2 = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img2)
    for row in range(rows):
        for column in range(columns):
            if (column - (columns/2))**2 + (row - (rows/2))**2 <= radius**2:
                #(r+c)/w says how many stripes above/below line y=x
                # The % 2 says whether it is an even or odd stripe
                image[row][column] = [0, 0, 255, 200] # pale red, alpha=0
                cir2_rad = radius - 1
                if (column - (columns/2))**2 + (row - (rows/2))**2 <= cir2_rad**2:
                    image[row][column] = [0, 0, 0, 0]
            
            else:
                # Odd stripe
                image[row][column] = [255, 0, 255, 0] # magenta, alpha=255
    return image

if __name__ == "__main__":
    image = make_mask(300,300,100)

# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(image, interpolation = 'none')
###
# Change a region if condition is True
###




###
# Show the image data
###

# Saves the figure
fig.savefig('women_and_mask')

print(type(img))
print(img)
print(len(img))
print(len(img[0]))
print(img[5][9][1])
print(img[4][10][0])
print(img[49][24][0])

'''Answers'''
#4.  Arrays are all the same data type, whereas losts and tuples can mix daata types.  Arrays are also multidimentional.  Both arrays and lists/tuples group data together.
#5.  the image height = the number of rows of pixels = 960
#	 the image width = the number of columns = 584
#	 the green intensity at (5,9) = 94
#    the red intensity at (4,10) = 62
#    the red intensity of the 25th pixel in the 50th row = 71
#7a.  A region of the image is selected, certain pixels in that region is selected, and changes the data in those pixels.