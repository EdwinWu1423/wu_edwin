f = open('image.ppm','w')
f.write('P3\n500 500\n255\n')

for value in range (500):

    for secvalue in range (500):
        r = value +1
        g = value % 256
        b = secvalue % 256
        f.write(str(r)+ ' ' + str(g) + ' ' +str(b)+ "\n")
f.close()
