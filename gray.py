"""
Vaughn Johnson
10 September 2015

4 tone grayscale using two colors

the promised land of zion
"""
from PIL import Image
from random import randint

#Prerequisite that image has even dimensions. If not, handled here
pic = Image.open('kittens.jpg')
if pic.size[0]%2:
    pic = pic.crop( (0, 0, pic.size[0]-1, pic.size[0]) )
if pic.size[1]%2:
    pic = pic.crop( (0, 0, pic.size[0], pic.size[1]-1) )

pix = pic.load()
#av = 0
cubes = []
zones = {}
zavg = []

def avg(a):
    return sum(a)/len(a)

for i in range(0,16):
    x = [int(j) for j in str("{:04b}".format(i))]
    for j in range (0,4):
        cubes.append( 3*(x[j]*256,))
cubes = [ (cubes[0+4*i], cubes[1+4*i], cubes[2+4*i], cubes[3+4*i]) for i in range(0,16)]
zavg = [avg( [avg(j) for j in i]) for i in cubes]
cubes = sorted(zip(zavg, cubes), key=lambda x: x[0])
cubes = [i[1] for i in cubes]

for x in range(0, pic.size[0]):
    for y in range(0, pic.size[1]):
        a = avg(pix[x,y])
        #av += a
        pix[x,y] = (a,a,a)

#av = av/(pic.size[0] * pic.size[1])

for x in xrange(0, pic.size[0], 2):
    for y in xrange(0, pic.size[1], 2):
        zones[str("{:05}".format(x))+str("{:05}".format(y))] = avg([pix[x,y][0], pix[x+1,y][0], pix[x,y+1][0], pix[x+1,y+1][0]])

for x in xrange(0, pic.size[0], 2):
    for y in xrange(0, pic.size[1], 2):
        compare = zones[str("{:05}".format(x))+str("{:05}".format(y))]
        if compare < 32:
            index = 0
        elif compare < 96:
            index = randint(1,4)
        elif compare < 160:
            index = randint(5,10)
        elif compare < 224:
            index = randint(11,14)
        else:
            index = 15
        pix[x,y] = cubes[index][0]
        pix[x+1,y] = cubes[index][1]
        pix[x,y+1] = cubes[index][2]
        pix[x+1,y+1] = cubes[index][3]

pic.show()
