from __future__ import print_function
'''Below are all of the libraries we used in this code '''
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import os.path
import PIL
import PIL.Image
import time
import numpy as np
import PIL.ImageDraw
from PIL import ImageFont

def border_one_img(original_img, thickness, shape):
    '''This function takes three parameters, original_img, thickness, and shape.
This function creates a border by creating a mask. It includes all of the possible
shapes for the border, octagon, triangle, rectangle and oval. These shapes are
taken from the user based on their choice through raw_input. The result creates 
a new image and pastes the border mask on top of the original image. The result is
then returned. '''
    width, height = original_img.size
    bor_mask = PIL.Image.new('RGBA', (width, height), (132, 112, 255, 0))
    drawing_layer = PIL.ImageDraw.Draw(bor_mask)
    if shape == 'octagon':
        drawing_layer.polygon([(thickness, height/4), (thickness, 3*(height/4)), 
        (width/4, height-thickness), (3*(width/4), height-thickness), (width-thickness, 3*(height/4)), 
        (width-thickness, height/4), (3*(width/4), thickness), (width/4, thickness)], fill = (0, 0, 0, 255))
    if shape == 'triangle':
        drawing_layer.polygon([(thickness, height-thickness), (width/2, thickness), 
        (width-thickness, height-thickness)], fill = (0, 0, 0, 255))
    if shape == 'rectangle':
        drawing_layer.polygon([(thickness, thickness), (thickness, height-thickness), 
        (width-thickness, height-thickness), (width-thickness, thickness)], fill = (0, 0, 0, 255))
    if shape == 'oval':
        drawing_layer.ellipse([(thickness, thickness), (width-thickness, height-thickness)], fill = (0, 0, 0, 255))
    #You can change the border color with the line below, the rgb values must be changed 
    # so make sure that whatever color you wish is in rgb format 
    result = PIL.Image.new('RGBA', original_img.size, (0, 0, 0, 255))
    result.paste(original_img, (0, 0), mask = bor_mask)
    return result
def get_images(directory=None):
    '''This function returns PIL.Image objects for all the images in directory. If 
directory is not specified, uses current directory. Returns a 2-tuple containing
a list with a  PIL.Image object for each image file in root_directory, and a list
with a string filename for each image file in root_directory. There is one
parameter which is directory and is set to none. '''
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
    '''This function applies the border to all of the images instead of the function
only being applied to a single image. There are three parameters, bor_thickness,
img_shape and directory. bor_thickness is for setting the thickness of the border
in pixels and img_shape is the shape of the image. This can be an oval, a rectangle,
an octagon, or a triangle based off of the user's choice. '''
    if directory == None:
        directory = os.getcwd()

    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    
    image_list, file_list = get_images(directory)  
# The for-loop below is specifically for pasting on all images using a list derived 
# from the length of image_list 
    for n in range(len(image_list)):
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        
        curr_image = image_list[n]
        new_image = border_one_img(curr_image, bor_thickness, img_shape) 
        
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)


def logo_paste(original_img):
    '''This function takes one paramter, original_img. Through this function, the logo
is pasted onto an image.This is again done by resizing the logo so that it doesn't 
take up too much of the image and then pasting. Because this function only applies
for one image, the function that applies this for all of the images is the next function '''
    width, height = original_img.size
    directory = os.path.dirname(os.path.abspath(__file__))  
    logo = os.path.join(directory, 'project_images/logo.png')
    logo_img = PIL.Image.open(logo)
    # You can change how big or how small the logo is with the line below 
    logo_small = logo_img.resize((50, 50))
    # You can change the location of the logo on the images with the numbers below 
    original_img.paste(logo_small, (width - 65, height - 65), 
    mask=logo_small)
    return original_img
    
def logo_paste_all():
    '''This function takes no parameters. Unlike the previous function, this function
pastes the logo after resizing onto all images. This is accomplished using another
for loop which goes the list of all images. '''
    directory = os.path.abspath('modified')
    new_directory = os.path.join(directory, 'with_logo')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    
    image_list, file_list = get_images(directory)  

    for n in range(len(image_list)):
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        curr_image = image_list[n]
        new_image = logo_paste(curr_image)
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)

def get_avg(x):
    '''This function takes one parameter x. Through this function, the avg pixel
    color is found so that the image can be turned to black and white. The avg
    also helps the image look cleaner than having black spots all over the image. '''
    sum_ = int(x[0])
    sum_ += int(x[1])
    sum_ += int(x[2])
    color_average = int(sum_ / 3.)
    pixel = [color_average for value in range(3)]
    pixel.append(255)
    return pixel


def grayscale(original_img):
    '''This function takes one parameter which is the original image. Through this 
function, the image is grayscaled. '''
    img_copy = PIL.Image.new('RGBA', original_img.size)
    img_array = np.asarray(img_copy).copy()
    array = np.asarray(original_img)
    y = 0
    for row in array:
        x = 0
        for column in array[0]:
            img_array[y][x] = get_avg(array[y][x])
            x += 1
        y += 1
    return PIL.Image.fromarray(img_array)
def grayscale_all_imgs():
    '''This function grayscales all images unlike the previous function which only affects
a single image. The modified images are saved in a different folder. Any OSError 
is passed through a try except block. '''
    directory = os.path.abspath('modified/with_logo/with_txt')
    new_directory = os.path.join(directory, 'black_and_white')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    
    image_list, file_list = get_images(directory)  

    for n in range(len(image_list)):
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        curr_image = image_list[n]
        new_image = grayscale(curr_image)
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
        
def txt_on_image(original_img, txt, location, color, font_size):
    '''This function applies text onto an image. There are 5 parameters, original_img,
txt, location, color and font_size. Through raw_input, the client's choices are
applied onto the image. '''
    # To change the font of the text, you would need to download that font and change 
    # the '../pacifico.ttf' to that font 
    font = ImageFont.truetype("../pacifico.ttf", font_size)
    width, height = original_img.size
    location_x, location_y = location
    location_x = int((location_x/100.0)*width)
    location_y = int((location_y/100.0)*height)
    location = (location_x, location_y)
    img = PIL.Image.new('RGBA', (width, height), (0, 0, 0, 0))
    img.paste(original_img, (0, 0))
    text_layer = PIL.ImageDraw.ImageDraw(img)
    text_layer.text(location,txt,color, font = font)
    return img
def text_on_all_images(text, loc, clr, font_size):
    '''This function applies the same text of the same color and location as well as
size onto all images. There are four parameters, text, loc, clr and font_size. 
Loc and clor are the location and color of the text. '''    
    directory = os.path.abspath('modified/with_logo')
    new_directory = os.path.join(directory, 'with_txt')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass
    
    image_list, file_list = get_images(directory)  

    for n in range(len(image_list)):
        print(n)
        filename, filetype = os.path.splitext(file_list[n])
        curr_image = image_list[n]
        new_image = txt_on_image(curr_image, text, loc, clr, font_size)
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
        
def use_minor():
    '''This function contains the raw_input for the border options as well as the
text options and grayscaling, these are based off of the client's choices. '''
    global satisfied
    #Below are the raw_input border options 
    border_option = raw_input('Would you like a border?:  ')
    if border_option == 'yes':
        border_shape = raw_input('What shape would you like your border to be?  We\
 have a rectangle, oval, triangle and octagon:  ')
        border_width = int(raw_input('How thick would you like your border to be? \
(pixels)?:  '))
        border_and_shape_all_images(border_width, border_shape)
        logo_paste_all()
    #Below are the raw_input text options 
    txt_option = raw_input('Would you like some text?:  ')
    if txt_option == 'yes':
        txt = raw_input('What text would you like to print onto your image?:    ')
        x, y = int(raw_input('What x-value would you like to put your text at(Please\
 choose a value between 0 and 100)?:  ')), int(raw_input('What y-value would you \
like to put your text at(Please choose a value between 0 and 100)?:  '))
        loc = (x, y)
        r, g, b = (int(x) for x in raw_input('What color would you like the text to \
be? r, g, b format (no parenthesis):  ').split(', '))
        rgb = (r, g, b)
        font_size = int(raw_input('What size would you like the text to be? (integer):  '))
        text_on_all_images(txt, loc, rgb, font_size)
    # Below is the raw_input for grayscaling the images, if the client wishes, 
    # then the images can be turned to black and white 
    grayscale_option = raw_input('Would you like to turn your images black and \
white? (experimental):  ')
    if grayscale_option == 'yes':
        grayscale_all_imgs()
    #T he satisfied is for the client to see if they like the end product 
    satisfied = raw_input('You can take a look at the images now.  Are you satisfied \
with the results?:  ')

def use_major():
    ''' This function is for client satisfaction. If the response is not yes, then
    the interface restarts at the border so the client can edit their pictures once
    again. This will continue until the client either exits or responds yes. '''
    use_minor()
    while satisfied != 'yes':
        use_minor()
# Below is for the client to insert their wished images into the correct folder  
# for the code to work. 
print('Please insert all images into the project_images folder.')
img_in_fol = raw_input('Are all of your images in the folder?  ')
if img_in_fol != 'yes':
    print('System exiting...')
    raise SystemExit(0)

print('')
# Below, we let the client know that all modifications will be applied the same 
# to all images. 
print('Disclaimer:  Changes apply to all images.  You can press control + c to \
exit the editor.  Change your directory to project_images if not already there. \
If you make a spelling error, immediatly hit control+c and restart.')

proceed = raw_input('Would you like to proceed?:  ')
# If the client is fine with the changes being applied to all images, then the  
# interface continues, else the program is exited. 
if proceed == 'yes':
    use_major()