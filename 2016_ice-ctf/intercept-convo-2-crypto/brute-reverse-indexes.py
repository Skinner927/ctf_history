import random
import base64
import os
P = [27, 35, 50, 11, 8, 20, 44, 30, 6, 1, 5, 2, 33, 16, 36, 64, 3, 61, 54, 25, 12, 21, 26, 10, 57, 53, 38, 56, 58, 37, 43, 17, 42, 47, 4, 14, 7, 46, 34, 19, 23, 40, 63, 18, 45, 60, 13, 15, 22, 9, 62, 51, 32, 55, 29, 24, 41, 39, 49, 52, 48, 28, 31, 59]
S = [68, 172, 225, 210, 148, 172, 72, 38, 208, 227, 0, 240, 193, 67, 122, 108, 252, 57, 174, 197, 83, 236, 16, 226, 133, 94, 104, 228, 135, 251, 150, 52, 85, 56, 174, 105, 215, 251, 111, 77, 44, 116, 128, 196, 43, 210, 214, 203, 109, 65, 157, 222, 93, 74, 209, 50, 11, 172, 247, 111, 80, 143, 70, 89]

ans = ['' for i in range(64*4)]
rev_index = [-1 for _ in range(64*4)]
rev_i = [-1 for _ in range(64*4)]
rev_j = [-1 for _ in range(64*4)]
for j in range(0, 64*4, 64):
    for i in range(64):
    	dex = j + P[i] - 1
    	ans[dex] = ', '.join(['dex:' + str(dex), 'i:'+str(i), 'j:'+str(j), 'p:'+str(P[i]), 's:'+str(S[i])])
    	index = i + (int(j / 64)) * 64
    	rev_index[dex] = index
    	rev_i[dex] = i
    	rev_j[dex] = j
        

print('rev_index = ' + str(rev_index))
print('')
print('rev_i = ' + str(rev_i))
print('')
print('rev_j = ' + str(rev_j))
print('')