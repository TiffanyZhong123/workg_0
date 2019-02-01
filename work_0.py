pic = open('pic.ppm','w')
pic.write('P3\n500 500\n255\n')
red = 0
green = 0
blue = 255
side = 500
for row in range(side):
    for col in range(side):
        if (col < 250):
            if (col%3 == 0):
                red += col%5
                green += col%60
            pic.write(str(red)+' '+str(green)+' '+str(blue)+' ')
        else:
            if (col%3 == 0):
                red -= col%5
                green -= col%60
            pic.write(str(red)+' '+str(green)+' '+str(blue)+' ')
pic.close()
