from __future__ import print_function
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os.path
import PIL
import PIL.Image
import time
import numpy as np
import PIL.ImageDraw

def border_one_img(original_img, thickness, shape):
    width, height = original_img.size
    bor_mask = PIL.Image.new('RGBA', (width, height), (0,0,0,0))
    drawing_layer = PIL.ImageDraw.Draw(bor_mask)
    if shape == 'rectangle':
        drawing_layer.polygon([(thickness, thickness), (thickness, height-thickness), (width-thickness, height-thickness), (width-thickness, thickness)], fill = (0, 0, 0, 255))
    if shape == 'circle':
        drawing_layer.ellipse([(thickness, thickness), (width-thickness, height-thickness)], fill = (0, 0, 0, 255))
    result = PIL.Image.new('RGBA', original_img.size, (0,0,0,255))
    result.paste(original_img, (0,0), mask = bor_mask)
    return result

def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified
        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list

def border_and_shape_all_images(bor_thickness, img_shape, directory = None):
    if directory == None:
        directory = os.getcwd()

    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    
    image_list, file_list = get_images(directory)  

    for n in range(len(image_list)):
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        
        curr_image = image_list[n]
        new_image = border_one_img(curr_image, bor_thickness, img_shape) 
        
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)



print('Please insert all images into the project_images folder.')
time.sleep(1)
img_in_fol = raw_input('Are all of your images in the folder?  ')
if img_in_fol != 'yes':
    print('System exiting...')
    raise SystemExit(0)
    
border_and_shape_all_images(10, 'c') #you can change the thickness of the 
# border by increasing or decreasing the value 10, 20 will result in a thicker border


'''bor_mask = PIL.Image.new('RGBA', (width, height), (0, 0, 0, 0))
    image_mask = np.array(bor_mask)
    for row in range(height):
        for column in range(width):
            if row >= thickness and row <= height-thickness and column >= thickness and column <= width-thickness:
                image_mask[row][column] = [0, 0, 0, 255]
            else:
                image_mask[row][column] = [0, 0, 0, 0]'''




originaimg = plt.imread(filename)