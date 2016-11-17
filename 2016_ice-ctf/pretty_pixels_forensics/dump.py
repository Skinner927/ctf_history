from PIL import Image

im = Image.open('img.png')



bb = []
for b in list(im.getdata()):
	r, g, b = b
	bb.append(r)
	bb.append(g)
	bb.append(b)

arr = bytearray(bb)

out = open('out.png', 'wb')

out.write(arr)

out.close()


