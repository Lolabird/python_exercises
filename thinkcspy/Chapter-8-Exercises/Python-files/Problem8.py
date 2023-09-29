# Runestone.Academy thinkcspy course
# Chapter 8
# Problem 8

import image

def greyScale (red, blue, green):    
    return (red + blue + green)/3

img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(0)   # setDelay(0) turns off animation

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
        
        pixelColor = greyScale(p.getRed(), p.getGreen(), p.getBlue())

        newblue = newgreen = newred = pixelColor
        
        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()