# Program to miltiplier two numbers without using arithmetic operator
# Allowed operator: 
#    • & (bitwise AND)
#    • | (bitwise OR)
#    • ^ (bitwise XOR)
#    • << (left shift)
#    • >> (right shift)
#    • = (assignment)
#    • ==, !=, <, >, <=, >= (comparison operators)
#    • ++ or += 1 allowed only to increment index
from adder import Adder as add

def Multiplier(a, b):
    r = 0                   # in case of multiply by 0 r is always 0
    while (b > 0):
        if (b & 1):         # if b !% 2 r = a + r
            r = add(r, a)
        a = a << 1          # 1 bitshift of a to the left
        b = b >> 1          # 1 bitshift of b to the right
    return r

 
print(Multiplier(21, 2))
print(Multiplier(1, 42))

# | oper | 16 | 8 | 4 | 2 | 1 |
# |------|----|---|---|---|---|
# | a    |  0 | 0 | 1 | 0 | 0 | -> a = 4
# | b    |  0 | 0 | 0 | 1 | 1 | -> b = 3
# | & b1 |  0 | 0 | 1 | 0 | 0 | -> r = 4
# | << a |  0 | 1 | 0 | 0 | 0 | -> a = 8
# | >> b |  0 | 0 | 0 | 0 | 1 | -> b = 1
# | & b1 |  0 | 1 | 1 | 0 | 0 | -> r = 12
# | << a |  1 | 0 | 0 | 0 | 1 | -> a = 16
# | >> r |  0 | 0 | 0 | 0 | 0 | -> b = 0 --> QUIT r = 12

