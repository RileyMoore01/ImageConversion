from PIL import Image, ImageChops

img1 = Image.open("IMG_5362.jpg")
img2 = Image.open("IMG_5363.jpg")

diff = ImageChops.difference(img1, img2)

if diff.getbbox():
    diff.show()
