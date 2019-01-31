f = open('image.ppm','w')
f.write('P3 500 500 255')
for value in range (500):
    for secvalue in range (500):
        r = 255
        g = value % 256
        b = secvalue % 256
        f.write(str(r)+ ' ' + str(g) + ' '+ str(b) + ' ')
f.close()
