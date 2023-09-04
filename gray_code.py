# Program to convert a number to gray code without using arithmetic operator
# https://www.youtube.com/watch?v=s-abLOm2MXk What is gray code 
# Allowed operator: 
#    • & (bitwise AND)
#    • | (bitwise OR)
#    • ^ (bitwise XOR)
#    • << (left shift)
#    • >> (right shift)
#    • = (assignment)
#    • ==, !=, <, >, <=, >= (comparison operators)
#    • ++ or += 1 allowed only to increment index

def Gray_code(a):
    r = a >> 1
    a ^= r
    return a

# | oper | 4 | 2 | 1 |
# |------|---|---|---|
# | a    | 1 | 0 | 0 | -> a = 4
# | >> a | 0 | 1 | 0 | -> r = 3
# | ^ ar | 1 | 1 | 0 | -> a = 6 --> QUIT

print(Gray_code(2))
print(Gray_code(3))
print(Gray_code(4))
print(Gray_code(5))
print(Gray_code(6))
print(Gray_code(7))
print(Gray_code(8))
print(Gray_code(21))
print(Gray_code(44))
