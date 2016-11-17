#inspiration http://incoherency.co.uk/image-steganography/#unhide
from PIL import Image
import numpy as np

im = Image.open('vape-nation.png')
r, g, b = im.split()

c = list(g.getdata())
#lsb mask
p = [int(x & 0b00000001 == 1) for x in c]

o = Image.new('1', (g.width, g.height))
o.putdata(p)
o.show()



### BEGIN OLD AND SCRATCH

exit()

im = Image.open('vape-nation.png')

r, g, b = im.split()

g.save('green.png')

# lsb mask
#c = [ a & 0b00000001 for a in list(g.getdata())]
c = np.asarray(g, dtype=int)

#p = [[(255,255,255) if c[x][y] & 0b00000001 == 1 else (255,255,0) for y in range(len(c[0]))] for x in range(len(c))]

#p = [[255 if c[x][y] & 0b00000001 == 1 else 0 for y in range(len(c[0]))] for x in range(len(c))]

#p = [[1 if c[x][y] & 0b00000001 == 1 else 0 for y in range(len(c[0]))] for x in range(len(c))]

#q = Image.fromarray(np.uint8(cm.gist_earth(myarray)*255))

# I can't get the damn thing to accept an array for 
o = Image.new('1', (g.width, g.height))
pix = o.load()
for x in xrange(len(c)):
	for y in xrange(len(c[0])):
		#lsb mask
		if c[x][y] & 0b00000001 == 1:
			pix[y,x] = 1
		else:
			pix[y,x] = 0

o.save('output.png')
o.show()




########



# split array by width of image
#chunks = [c[x:x+im.width] for x in xrange(0, len(c), im.width)]

#Image.fromarray(np.asarray(chunks), mode='1')