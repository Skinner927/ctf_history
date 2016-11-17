import random
import base64
import os

# Ciphertext to solve
c = 'Wmkvw680HDzDqMK6UBXChDXCtC7CosKmw7R9w7JLwr/CoT44UcKNwp7DllpPwo3DtsOID8OPTcOWwrzDpi3CtMOKw4PColrCpXUYRhXChMK9w6PDhxfDicOdwoAgwpgNw5/Cvw=='

P = [27, 35, 50, 11, 8, 20, 44, 30, 6, 1, 5, 2, 33, 16, 36, 64, 3, 61, 54, 25, 12, 21, 26, 10, 57, 53, 38, 56, 58, 37, 43, 17, 42, 47, 4, 14, 7, 46, 34, 19, 23, 40, 63, 18, 45, 60, 13, 15, 22, 9, 62, 51, 32, 55, 29, 24, 41, 39, 49, 52, 48, 28, 31, 59]
S = [68, 172, 225, 210, 148, 172, 72, 38, 208, 227, 0, 240, 193, 67, 122, 108, 252, 57, 174, 197, 83, 236, 16, 226, 133, 94, 104, 228, 135, 251, 150, 52, 85, 56, 174, 105, 215, 251, 111, 77, 44, 116, 128, 196, 43, 210, 214, 203, 109, 65, 157, 222, 93, 74, 209, 50, 11, 172, 247, 111, 80, 143, 70, 89]

# Get real lazy and just generate reverse tables for values at output indexes
rev_index = [-1 for _ in range(64*4)]
rev_i = [-1 for _ in range(64*4)]
rev_j = [-1 for _ in range(64*4)]
for j in range(0, 64*4, 64):
    for i in range(64):
    	dex = j + P[i] - 1
    	index = i + (int(j / 64)) * 64
    	rev_index[dex] = index
    	rev_i[dex] = i
    	rev_j[dex] = j

# This will brute force the original character
chars = range(0x20, 0x7E)
#o is the ordinal, s is the S[i] lookup
def brute(o, s):
	for c in chars:
		#ord(inp[j + i]) + S[i]) % 256
		if (ord(chr(c)) + s) % 256 == o:
			return chr(c)
	
	return '?'

# Reverse!
#c = c.encode('utf8')
d = base64.b64decode(c)
d = d.decode('utf8')

# create the ans array
a = list(d)

#out
fix = ['' for _ in range(64*4)]

'''
orig
for j in range(0, len(inp), 64):
	# 0 64 128 192 256
    for i in range(64):
        ans[j + P[i] - 1] = chr((ord(inp[j + i]) + S[i]) % 256)
'''
# reverse the above
for x in range(len(a)):
	i = rev_index[x]
	theirI = rev_i[i]
	theirJ = rev_j[i]
	
	o = a[i]
	#reverse chr()
	o = ord(o)
	o = brute(o, S[theirI])
	fix[theirI + theirJ] = o
	
print(''.join(fix))