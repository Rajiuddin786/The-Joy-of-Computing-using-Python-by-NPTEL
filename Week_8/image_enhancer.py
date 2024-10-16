#Flipping the Image
from PIL import Image

img = Image.open('./Files/image_zoro.jpg')

#Transposing
transposed_img = img.transpose(Image.FLIP_LEFT_RIGHT)

#Save it to a understandable level of Human

transposed_img.save('./Files/new_img.png')

print('Done Flipping')