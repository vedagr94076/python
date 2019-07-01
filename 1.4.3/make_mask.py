import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import numpy as np
import PIL

def make_mask(rows, columns, radius):
    '''An example mask generator
    Makes slanted stripes of width stripe_width
    image
    returns an ndarray of an RGBA image rows by columns
    '''
    img = PIL.Image.new('RGBA', (columns, rows))
    image = np.array(img)
    for row in range(rows):
        for column in range(columns):
            if (column - (columns/2))**2 + (row - (rows/2))**2 <= radius**2:
                image[row][column] = [0, 0, 255, 200] # pale red, alpha=0
                cir2_rad = radius - 1
                if (column - (columns/2))**2 + (row - (rows/2))**2 <= cir2_rad**2:
                    image[row][column] = [0, 0, 0, 0]
            else:
                # Odd stripe
                image[row][column] = [255, 0, 255, 0] # magenta, alpha=255
            
            if column + row == 300:
                image[row][column] = [0, 0, 255, 200]
                
    return image
    
if __name__ == "__main__":
    image = make_mask(300,300,100)
    
    fig, ax = plt.subplots(1, 1)
    ax.imshow(image)
    fig.savefig('mask')