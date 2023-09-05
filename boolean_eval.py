# Program who take a string to evaluate veracity without using arithmetic operator
# Allowed operator: 
#    • & (bitwise AND)
#    • | (bitwise OR)
#    • ^ (bitwise XOR)
#    • << (left shift)
#    • >> (right shift)
#    • = (assignment)
#    • ==, !=, <, >, <=, >= (comparison operators)
#    • ++ or += 1 allowed only to increment index

def eval_formula(string):
    verity = []
    for c in string:
        match c:
            case '1': # True
                verity.append(True)
            case '0': # False
                verity.append(False)
            case '!': # Negation
                verity[-1] = False if verity[-1] is True else True
            case '&': # conjonction
                r = True if verity[-1] == verity[-2] else False
                verity.pop()
                verity.pop()
                verity.append(r)
            case '|': # disjonction
                r = True if verity[-1] or verity[-2] is True else False
                verity.pop()
                verity.pop()
                verity.append(r)
            case '^': # exclusive disjonction
                r = False if verity[-1] == verity[-2] else True
                verity.pop()
                verity.pop()
                verity.append(r)
            case '>': # material contition
                r = True if verity[-1] == verity[-2] or verity[-1] is True else False
                verity.pop()
                verity.pop()
                verity.append(r)
            case '=': # logical equivalence
                r = True if verity[-1] == verity[-2] else False
                verity.pop()
                verity.pop()
                verity.append(r)
            case _:
                break
    return verity[0]


print(eval_formula("1!"));       # false
print(eval_formula("10&"));      # false
print(eval_formula("00^"));      # false
print(eval_formula("01^"));      # true
print(eval_formula("10|"));      # true
print(eval_formula("11>"));      # true
print(eval_formula("10="));      # false
print(eval_formula("1011||="));  # true
