import numpy as np
from PIL import Image
import scipy.misc
import random

# width=5
# height=4

# array1=np.zeros([height,width,3],dtype=np.uint8)
# img1=Image.fromarray(array1)
# #img1.save('./Files/test_1.png')

# array2=np.zeros([100,200,3],dtype=np.uint8)
# array2[:,:100]=[255,128,0] #Orange Color
# array2[:,100:]=[0,0,255] #Blue Color
# img2=Image.fromarray(array2)
# img2.save('./Files/test_2.png')

# img=Image.open('./Files/test_2.png')
# rgb_img=img.convert('RGB')
# r,g,b=rgb_img.getpixel((1,1))

# print(r,g,b)

"""Method - 01"""

# img=scipy.misc.imread("map_01.png")
# count_pun=0
# count_ind=0
# count=0

# while count<=20000:
#     x=random.randint(0,2735)
#     y=random.randint(0,2480)
#     z=0

#     if img[x][y][z] == 60:
#         count_ind+=1
#         count+=1
#     else:
#         if img[x][y][z] == 80:
#             count_pun+=1
#         count+=1

# area_pun=(count_pun/count_ind)*32287263

# print(area_pun)

"""Method 2"""
img=Image.open('map-01.png')
rgb_img=img.convert("RGB")

count_in=0
count_pun=0
count=0

while count<=10000:
    x=random.randint(0,2480)
    y=random.randint(0,2735)
    z=0
    r,g,b=rgb_img.getpixel((x,y))
    if r==60:
        count_in += 1
        count+=1
    else:
        if r == 80:
            count_pun+=1
        count+=1

area_pun=(count_pun/count_in)*3287263

print(area_pun)