'''
JDoe_JSmith_1_4_2: Read and show an image.
'''
import matplotlib 
'''This tells matplotlib to run in a non-GUI interface'''
matplotlib.use('Agg')
import matplotlib.pyplot as plt 
import os.path
import numpy as np      # 'as' lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

# Create a 1x2 grid of subplots
# fig is the Figure, and ax is an ndarray of AxesSubplots
# ax[0] and ax[1] are the two Axes Subplots
fig, ax = plt.subplots(1, 5)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
ax[2].imshow(img, interpolation='none')
ax[3].imshow(img, interpolation='none')
ax[4].imshow(img, interpolation='none')
# Show the figure on the screen
# fig.show()
fig.savefig('five_cats.png')

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
# Show the figure on the screen
# fig.show()
fig.savefig('leaf_earing')

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none') # Override the default
ax[1].imshow(img)
ax[0].set_xlim(135, 165)
ax[0].set_ylim(470, 420)
ax[1].set_xlim(135, 165)
ax[1].set_ylim(470, 420)
ax[0].axis('off')
ax[1].axis('off')
# Show the figure on the screen
# fig.show()
fig.savefig('experiment.png')

# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'cat1-a.gif')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 3)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation = 'none') # Override the default
ax[1].imshow(img, interpolation = 'none')
ax[2].imshow(img, interpolation = 'none')
ax[0].set_xlim(35, 45)
ax[0].set_ylim(80, 70)
ax[1].set_xlim(45, 55)
ax[1].set_ylim(80, 70)
ax[2].set_xlim(55, 65)
ax[2].set_ylim(80, 70)
# Show the figure on the screen
# fig.show()
fig.savefig('three_closeup.png')

# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__)) 
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'PCWmice1.jpg')
# Read the image data into an array
img = plt.imread(filename)

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 2)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation = 'none') # Override the default
ax[1].imshow(img, interpolation = 'none')
ax[1].plot(38, 49, 'ro')
ax[1].plot(117, 43, 'ro')
ax[1].plot(137, 42, 'ro')
# Show the figure on the screen
# fig.show()
fig.savefig('crazy_mice.png')

'''Answers'''
#4.  C:/Users/Student login/Desktop/nice.jpg
#5.  ../Student login/Desktop/nice.jpg
#6a.  This is an absolute filename
#6b.  No
#6c.  There is an u' (ubuntu)
#7a.  (262, 411)
#7b.  (231, 464)
#8a.  fig is an instance of the class figure, and ax isan instance o fthe class AxesSubplot.
#8b.  Similarly, in line 25, the method savefig is being called on the object fig. That method is being given 1 argument. That method is a method of the class Figure.
#8c.  The comment above the line of code explains the code.
#9a.  The method imshow is being called on the object ax[0].
#10.  The code take the image and inserts infered points to make the image clearer, interpolating it.
#12.  Axes.matshow().  Optianal argument:  origin.  Default value: 'upper'.