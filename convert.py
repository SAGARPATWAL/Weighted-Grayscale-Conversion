from scipy import misc
import numpy as np
import cv2
import matplotlib.pyplot as plt # import
import matplotlib.cm as cm

image = misc.imread('img/4.1.01.tiff')


def Weightedaverage(pixel):
    red,green,blue=[float(pixel[0]),float(pixel[1]),float(pixel[2])]
    #return 0.299*red + 0.587*green + 0.114*blue 
    c1=red-green
    c2=green-blue
    c3=red-blue
    if c1>0 and c3>0:
        return (red+abs(c1)/100 +abs(c3)/100 )*0.2126 + 0.7152*green + 0.0722*blue
    elif c2<0 and c3<0:
        return (blue+abs(c2)/100  +abs(c3)/100 )*0.0722 + 0.7152*green + 0.2126*red
    elif c1<0 and c2>0:
        return (green+abs(c1)/100  +abs(c2)/100 )*0.7152 + 0.2126*red + 0.0722*blue
    else: return red*0.2126 + 0.7152*green + 0.0722*blue
    

def average(pixel):
    red,green,blue=[float(pixel[0]),float(pixel[1]),float(pixel[2])]
    return red*0.2126 + 0.7152*green + 0.0722*blue
    #return 0.299*red + 0.587*green + 0.114*blue
    


def main():
    gray=np.zeros((image.shape[0], image.shape[1]))
    gray2=np.zeros((image.shape[0], image.shape[1]))
    for rownum in range(len(image)):
        for colnum in range(len(image[rownum])):
           gray[rownum][colnum] = Weightedaverage(image[rownum][colnum])
           gray2[rownum][colnum] = average(image[rownum][colnum])
    '''f = open('img_data.txt','w')
    for i in gray:
        f.write(str(i))'''

    plt.subplot(2,2,1)
    plt.imshow(gray, cmap = cm.Greys_r)
    plt.title('Weighted CIE')
    im1=misc.imsave('1.jpg',gray)

    plt.subplot(2,2,2)
    plt.imshow(gray2, cmap = cm.Greys_r)
    plt.title('simple CIE')
    im2=misc.imsave('2.jpg',gray2)


    plt.subplot(2,2,3)
    
    hi1=plt.hist(gray)

    plt.subplot(2,2,4)
    hi2=plt.hist(gray2)
    plt.show()

if __name__=='__main__':
    main()

    

