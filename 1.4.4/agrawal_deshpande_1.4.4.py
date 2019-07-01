'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7
PIL API Version 9/10/2013 '''

from __future__ import print_function
import matplotlib 
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import PIL
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
student_file = os.path.join(directory, 'student.jpg')

# Open and show the student image in a new Figure window
student_img = PIL.Image.open(student_file)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(student_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(student_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1050, 1400) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1100, 850)
fig.savefig('girl')

# Open, resize, and display earth
earth_file = os.path.join(directory, 'earth.png')
earth_img = PIL.Image.open(earth_file)
earth_small = earth_img.resize((89, 87)) #eye width and height measured in plt
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(earth_img)
axes2[1].imshow(earth_small)
fig2.savefig('resize_earth')

# Paste earth into right eye and display
# Uses alpha from mask
student_img.paste(earth_small, (1162, 966), mask=earth_small) 
student_img.paste(earth_small, (700, 940), mask=earth_small) 

# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(student_img, interpolation='none')
axes3[1].imshow(student_img, interpolation='none')
axes3[1].set_xlim(500, 1500)
axes3[1].set_ylim(1130, 850)
fig3.savefig('earth_eye')

earth_small.save('smallEarth.png')

print(earth_img.size)
print(earth_small.size)
print(earth_img.size[1])

'''Answers'''
#13.  matplotlib.pyplot (plt) - Used to edit images and change values of pixels
#     numpy (np) - Creates arrays
#     PIL - Used to create images
#15a.  Line 19 calls the function subplots from the plt library. The function is being called with 2 argument(s): 1 and 2. The function returns 2 object(s), which is/are being assigned to fig snd ax.
#15c.  (1162, 966)
#16.  (700, 940), (790, 1016); height = 76; width = 90
#17a.  Line 30 uses the join() method from the os.path module. It is being passed 2 arguments. The value it returns is being assigned to the variable earth_file.
#17b.  In line 31 the open() function of the PIL.Image module returns a new PIL.Image object, which is being assigned to the variable earth_img.
#17c.  One is to idetify the value as a tuple, and the other seet of parenthesis are to tell python that we are inputting an argument.
#17d.  The bounding box is the size of the iris, which also must be the siz of the earth.  This is why the tuple is (89, 87), the size of the iris.
#17fi.  box = (1000, 900, 90, 76)
#17fii.  box = None
#17h.  The first output is the height and width of the original image, the second output is the height and width of the second image, and the third output is the length of the larger image.
#17i.  The ticks are labled differently.
#18.  The image takes each pixel and then takes all of the pixels around it and takes an average color to display in the resized image.
#19a.  student_img bytes = 15667200
#      earth_small bytes = 30927
#19c.  student.jpg bytes = 206 KB
#      smallEarth.png bytes = 18.3 KB
#19d.  The units have been changed and when dowloaded, the image may need to have a bit of extra code behind it.
#19e.  The area specified will be replaced with an image.
#19g.  The first one specifies the file being pasted, the second one tells python the position, and the third one specifies the image is a mask.