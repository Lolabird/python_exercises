# Runestone.Academy thinkcspy course
# Chapter 8
# Problem 10

import image


img = image.Image("luther.jpg")
win = image.ImageWin(img.getWidth(), img.getHeight())
img.draw(win)
img.setDelay(0)   # setDelay(0) turns off animation
        

for row in range(img.getHeight()):
    for col in range(img.getWidth()):
        p = img.getPixel(col, row)
        
        R = p.getRed()
        G = p.getGreen()
        B = p.getBlue()
        
        newred = (R * 0.393 + G * 0.769 + B * 0.189)
        newgreen = (R * 0.349 + G * 0.686 + B * 0.168)
        newblue = (R * 0.272 + G * 0.534 + B * 0.131)
        
        newpixel = image.Pixel(newred, newgreen, newblue)

        img.setPixel(col, row, newpixel)

img.draw(win)
win.exitonclick()