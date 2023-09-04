# Program to add two numbers without using arithmetic operator
# Allowed operator: 
#    • & (bitwise AND)
#    • | (bitwise OR)
#    • ^ (bitwise XOR)
#    • << (left shift)
#    • >> (right shift)
#    • = (assignment)
#    • ==, !=, <, >, <=, >= (comparison operators)
#    • ++ or += 1 allowed only to increment index

def Adder(a, b):
    while (b != 0):
        r = a & b # bitwise AND between a and b
        a = a ^ b # bitwise XOR between a and b
        b = r << 1 # 1 bitshift of r to the left
    return a # when b = 0 return result of a

 
print(Adder(11, 31))

# | oper | 8 | 4 | 2 | 1 |
# |------|---|---|---|---|
# | a    | 0 | 1 | 0 | 0 | -> a = 4
# | b    | 0 | 1 | 0 | 1 | -> b = 5
# | & ab | 0 | 1 | 0 | 0 | -> r = 4
# | ^ ab | 0 | 0 | 0 | 1 | -> a = 1
# | << r | 1 | 0 | 0 | 0 | -> b = 8
# | & ab | 0 | 0 | 0 | 0 | -> r = 0
# | ^ ab | 1 | 0 | 0 | 1 | -> a = 9
# | << r | 0 | 0 | 0 | 0 | -> b = 0 --> QUIT

