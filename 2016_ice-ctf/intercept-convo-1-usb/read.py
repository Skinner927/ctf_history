import os
from keys import keys as key_map

f = open('dump2.txt', 'r')

whole_out = ''
for line in f.read().splitlines():
	c = line.split(':')

	modifier = int(c[0])
	keys = c[2:]

	mod = ''
	if  modifier &  0b00000001:
		mod = '[ctrl]'
	elif modifier & 0b00000010:
		mod = '[shift]'
	elif modifier & 0b00000100:
		mod = '[alt]'	
	elif modifier & 0b00001000:
		mod = '[win]'
	elif modifier & 0b00010000:
		mod = '[ctrl]'
	elif modifier & 0b00100000:
		mod = '[shift]'	
	elif modifier & 0b01000000:
		mod = '[alt]'	
	elif modifier & 0b10000000:
		mod = '[win]'	

	mod = mod.ljust(7)

	out = '';
	for k in keys:
		j = key_map.get(int(k, 16), '?')	
		if mod == '[shift]':
			out += j + ' '		
		else:
			out += j.lower() + ' '

	
	#print mod + ' ' + out
	whole_out += out.strip()

print whole_out