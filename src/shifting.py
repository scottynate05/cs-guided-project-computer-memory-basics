a = 0b00001010
b = 0b00000001

c = a & b
a = a >> 1
c = a & b
a = a >> 1
c = a & b
a = a >> 1
c = a & b
a = a >> 1
c = a & b

counter = 0
counter += 1
counter += 1

print('Counter', counter)

print(c)