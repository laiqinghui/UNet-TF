import sys, time
import numpy as np
from PIL import Image

if __name__ == '__main__':

    np.set_printoptions(threshold=sys.maxsize)
    seg_image = Image.open("data_set/VOCdevkit/person/SegmentationClass/009649.png")
    sun_image = Image.open("sun.png")
    print("seg_image.size = ", seg_image.size)


    rgb = [
           [0, 0, 0],  # void
           [128, 64, 128],  # Bed
           [244, 35, 232],  # Books
           [70, 70, 70],    # Ceiling
           [102, 102, 156], # Chair
           [190, 153, 153], # Floor
           [153, 153, 153], # Furniture
           [250, 170, 30],  # Objects
           [220, 220, 0],   # Picture
           [107, 142, 35],  # Sofa
           [152, 251, 152], # Table
           [70, 130, 180],  # TV
           [220, 20, 60],   # Wall
           [255, 0, 0]      # Window
           ]

    
    # Get a color palette
    palette = seg_image.getpalette()
    print(len(palette))
    print("Palette: ", palette[0], ", ", palette[1], ", ", palette[2])
    palette[15] = 255
    palette[16] = 128
    palette[17] = 0
    palette[21] = 255
    palette[22] = 255
    palette[23] = 0

    index = 0
    for i in range(len(rgb)):
        palette[index] = rgb[i][0]
        palette[index+1] = rgb[i][1]
        palette[index+2] = rgb[i][2]
        index += 3

    indexed = np.array(seg_image)

    # print(indexed.shape)
    # print(indexed[0])

    print(palette[:42])
    sun_image.putpalette(palette)
    # sun_image = sun_image.convert("RGB")


    sun_image.save("palette.png")

    pal_img = Image.open("palette.png")
    new_palette = pal_img.getpalette()
    print(new_palette[:42])





