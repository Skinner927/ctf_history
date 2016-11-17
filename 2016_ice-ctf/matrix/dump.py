from PIL import Image

f = open('matrix.txt', 'r')

lines = f.read().splitlines()



def pad_bin(b):
	return '{0:032b}'.format(b)

p = []
i = False
j = -1
for line in lines:
	j = j + 1

	l = [int(i) if x == '1' else int(not i) for x in pad_bin(int(line, 16))]
	p.extend(l)


o = Image.new('1', (32, len(lines)))
o.putdata(p)

o.save('qr.png')

for lin in lines:
	print pad_bin(int(lin, 16))