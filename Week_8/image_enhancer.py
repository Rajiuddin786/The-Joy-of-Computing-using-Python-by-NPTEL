from PIL import Image
import cv2

#Flipping the Image
def flipping():
    img = Image.open('./Files/image_zoro.jpg')

    #Transposing
    transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

    #Save it to a understandable level of Human

    transposed_img.save('./Files/new_img.png')

    print('Done Flipping')

#Image Enhancement
def enhance():
    img=cv2.imread('./Files/image_zoro.jpg')

    #Preparation of CLAHE
    clahe = cv2.createCLAHE()

    #Convert img into grayscale image
    gray_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    #Apply Enhacement to gray_img
    enh_img=clahe.apply(gray_img)

    #Output
    cv2.imwrite('./Files/new_img.png',enh_img)

enhance()