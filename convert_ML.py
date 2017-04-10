from scipy import misc
import numpy as np
import cv2
import matplotlib.pyplot as plt # import
import matplotlib.cm as cm
import convert as conv

image= misc.imread('img/4.1.05.tiff')
dict_img ={}
'''
pic1=218
pic2=88
pic4=127
for img in os.listdir(impath):
    image = misc.imread(impath)
    gray=np.zeros((image.shape[0], image.shape[1]))
    for rownum in range(len(image)):
        for colnum in range(len(image[rownum])):
           gray[rownum][colnum] = Weightedaverage(image[rownum][colnum])
    dict_img[]'''
def Weightedaverage(pixel):
    red,green,blue=[float(pixel[0]),float(pixel[1]),float(pixel[2])]
    #return 0.299*red + 0.587*green + 0.114*blue 
    c1=red-green
    c2=green-blue
    c3=red-blue
    difer=abs(c1)+abs(c2)+abs(c3)
    if difer < 101:
        return red*0.2126 + 0.7152*green + 0.0722*blue
    elif c1>0 and c3>0:
        return (red+abs(c1)/100 +abs(c3)/100 )*0.2126 + 0.7152*green + 0.0722*blue
    elif c2<0 and c3<0:
        return (blue+abs(c2)/100  +abs(c3)/100 )*0.0722 + 0.7152*green + 0.2126*red
    elif c1<0 and c2>0:
        return (green+abs(c1)/100  +abs(c2)/100 )*0.7152 + 0.2126*red + 0.0722*blue

def main():
    gray=np.zeros((image.shape[0], image.shape[1]))
    
    for rownum in range(len(image)):
        for colnum in range(len(image[rownum])):
           gray[rownum][colnum] = Weightedaverage(image[rownum][colnum])
    f=open('pic5.txt','w')
    for i in gray:
        f.write(str(i))
    #f.write(str(127))
    
    plt.subplot(1,1,1)
    plt.imshow(gray, cmap = cm.Greys_r)
    plt.title('Weighted CIE')
    plt.show()

if __name__=='__main__':
    main()

