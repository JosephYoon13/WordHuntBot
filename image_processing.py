import pytesseract as tess
from PIL import Image
import numpy as np


def processImage():
    im1 = Image.open('boardpic.jpg')
    im1 = im1.convert('RGB')

    width, height = im1.size
    for x in range(width):
        for y in range(height):
            r, g, b = im1.getpixel((x, y))
            gray = int(r * 299/1000 + g * 587/1000 + b * 114/1000)
            im1.putpixel((x, y), (gray, gray, gray))

    # im1.save('out.png')

    # im = Image.open('out.png')
    im1 = im1.convert('RGBA')
    data = np.array(im1)
    rgb = data[:, :, :3]
    black = [0, 0, 0]
    white = [255, 255, 255, 255]
    mask = np.all(rgb == black, axis=-1)
    data[np.logical_not(mask)] = white
    new_im = Image.fromarray(data)
    # new_im.save('black_image.png')

    text = tess.image_to_string(new_im, config='--psm 6')
    text = ''.join(text.splitlines())
    text = text.replace(' ', '')
    text = text.replace('|', 'I')
    text = text.lower()

    if len(text) != 16:
        print("Invalid; enter board: ")
        text = input()
    print(text)

    return text


# processImage()
