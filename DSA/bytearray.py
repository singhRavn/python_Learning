'''
python bytearray gives a mutuable sequence of integer in range 0<=x<256
'''

a = bytearray((12,8,25,2))
print(a)

a[1] = 3
print(a)

# Append element

a.append(30)
print(a)