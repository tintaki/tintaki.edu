a = True
b = False

print(a & b)
print ((a & b) | b)
print((a & b) ^ (a & b))
print(a & b ^ (a & b) | b)
print(b & b ^ a & (a | b | a) ^ (a | b))
print(1 << 2)
print(1 & 0 | 1 >> 1)
print(1 & 0 | 1 >> 0)
print(0b101 & 0b111 ^ 0b111 | 0b010)
       