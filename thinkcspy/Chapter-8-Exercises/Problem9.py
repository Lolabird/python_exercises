# Runestone.Academy thinkcspy course
# Chapter 8
# Problem 9

import image

def greyScale (red, blue, green):
    return (red + blue + green)/3

def blackWhite (color):
    if color >= 255 / 2:
        return 255
    else:
        return 0

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(0)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
        
        pixelColor = greyScale(p.getRed(), p.getGreen(), p.getBlue())
        
        newblue = newgreen = newred = blackWhite(pixelColor)
        
        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()