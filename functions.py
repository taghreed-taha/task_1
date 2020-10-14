'''
Import here most important libraries
'''
import matplotlib.pyplot as plt
import numpy as np
from cv2 import cv2


def zero_channel(image, channel):
     """ Return image **excluding** the rgb channel specified
    Args:
        image: numpy array of shape(image_height, image_width, 3)
        channel: number specifying the channel (0 for B, 1 for G, 2 for R)
    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """
     image[:,:,channel] = 0
     return image




def draw_solid_square_slow(image, x, y, l, color):
    """ Returns image after drawing a square on the image using python nested loops
    Args:
        image: numpy array of shape(image_height, image_width, 3)
        (x,y): a tuple specifying upper left corner
        l: square edge length
        color: a tuple specifying (B,G,R)
    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """
    #(x1,y1) = x , y
    #(x2,y2) = x+l , y-l

     


def draw_solid_square_fast(image, x, y, l, color):
    """ Returns image after drawing a square on the image using numpy arrays operations
    Args:
        image: numpy array of shape(image_height, image_width, 3)
        (x,y): a tuple specifying upper left corner
        l: square edge length
        color: a tuple specifying (B,G,R)
    Returns:
        out: numpy array of shape(image_height, image_width, 3)
    """
    (x1,y1) = x , y
    (x2,y2) = x+l , y-l
    image = cv2.rectangle(image,(x1,y1),(x2,y2),color,2)
    return image
     



def combine_images_h(img1, img2):
    """ Return 2 images combined horizontally. If the heights of images are different, you
    may set additional space to black
Args:
    img1: numpy array of shape(image_height, image_width, 3)
    img2: numpy array of shape(image_height, image_width, 3)
Returns:
    out: numpy array
""" 
 if (img1.shape[0] == img2.shape[0]):
     im_h = cv2.hconcat([img2, img2])
 elif (img1.shape[0]<img2.shape[0]):
     old_height = img1.shape[0]
     new_size = (img2.shape[0],img1.shape[1])
     img1 = cv2.resize(img1,new_size)
     img1[old_height:img2.shape[0],:,0] = 0
     img1[old_height:img2.shape[0],:,1] = 0
     img1[old_height:img2.shape[0],:,2] = 0
     im_h = cv2.hconcat([img2, img2])
 else:
     old_height = img2.shape[0]
     new_size = (img1.shape[0],img2.shape[1])
     img2 = cv2.resize(img1,new_size)
     img2[old_height:img1.shape[0],:,0] = 0
     img2[old_height:img1.shape[0],:,1] = 0
     img2[old_height:img1.shape[0],:,2] = 0
     im_h = cv2.hconcat([img2, img2])   
 return im_h    


     


def combine_images_v(img1, img2):
    """ Return 2 images combined vetically. If the widths of images are different, you
    may set additional space to black
Args:
    img1: numpy array of shape(image_height, image_width, 3)
    img2: numpy array of shape(image_height, image_width, 3)
Returns:
    out: numpy array
"""
 if (img1.shape[1] == img2.shape[1]):
     im_h = cv2.vconcat([img2, img2])
 elif (img1.shape[1]<img2.shape[1]):
     old_width = img1.shape[1]
     new_size = (img1.shape[0],img2.shape[1])
     img1 = cv2.resize(img1,new_size)
     img1[:,old_width:img1.shape[1],0] = 0
     img1[:,old_width:img1.shape[1],1] = 0
     img1[:,old_width:img1.shape[1],2] = 0
     im_h = cv2.vconcat([img2, img2])
 else:
     old_width = img2.shape[1]
     new_size = (img2.shape[0],img1.shape[1])
     img2 = cv2.resize(img2,new_size)
     img2[:,old_width:img2.shape[1],0] = 0
     img2[:,old_width:img2.shape[1],1] = 0
     img2[:,old_width:img2.shape[1],2] = 0
     im_h = cv2.hconcat([img2, img2])   
 return im_h    



def my_bgr2gray(image):
    """
    Returns a grayscale image where each pixel value = (B+G+R)/3
Args:
    image: numpy array of shape(image_height, image_width, 3)
Returns:
    out: numpy array of shape(image_height, image_width, 3)
"""
 k = image
 height = image.shape[0]
 widths = image.shape[1]
 image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
 for i in range(height):
     for t in range(widths):
         image[i,t] = np.sum(k[i,t])
 return image        


def normalize_img(image):
    """
    normalize each channel independently according to the following formula
    pixel = (channel_value - channel_mean)/channel_std
Args:
    image: numpy array of shape(image_height, image_width, 3)
Returns:
    out: numpy array of shape(image_height, image_width, 3)
"""
 image=(image-np.mean(image, axis=(0,1)))/np.std(image, axis=(0,1))
 return image
