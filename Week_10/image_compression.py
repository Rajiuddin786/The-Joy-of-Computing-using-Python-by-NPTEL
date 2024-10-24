import numpy as np
from PIL import Image as img

im = img.open('./Files/image_zoro.jpg')
pixelMap = im.load()


new_im = img.new(im.mode, im.size)
new_pixelMap = new_im.load()


for i in range(im.size[0]):
    for j in range(im.size[1]):
        pixel_value = pixelMap[i, j]

        if isinstance(pixel_value, tuple):  
            r, g, b = pixel_value

            
            if 0 <= r <= 31:
                new_pixelMap[i, j] = (0, g, b)
            elif 32 <= r <= 63:
                new_pixelMap[i, j] = (1, g, b)
            elif 64 <= r <= 95:
                new_pixelMap[i, j] = (2, g, b)
            elif 96 <= r <= 127:
                new_pixelMap[i, j] = (3, g, b)
            elif 128 <= r <= 159:
                new_pixelMap[i, j] = (4, g, b)
            elif 160 <= r <= 223:
                new_pixelMap[i, j] = (0, g, b)
            elif 224 <= r <= 255:
                new_pixelMap[i, j] = (7, g, b)
        else:  
            if 0 <= pixel_value <= 31:
                new_pixelMap[i, j] = 0
            elif 32 <= pixel_value <= 63:
                new_pixelMap[i, j] = 1
            elif 64 <= pixel_value <= 95:
                new_pixelMap[i, j] = 2
            elif 96 <= pixel_value <= 127:
                new_pixelMap[i, j] = 3
            elif 128 <= pixel_value <= 159:
                new_pixelMap[i, j] = 4
            elif 160 <= pixel_value <= 223:
                new_pixelMap[i, j] = 0
            elif 224 <= pixel_value <= 255:
                new_pixelMap[i, j] = 7

# Save the new image
new_im.save('./Files/new_zoro_img.jpg')
