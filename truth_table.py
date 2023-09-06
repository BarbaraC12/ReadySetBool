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

def print_truth_table(formula: str) -> bool:
    verity = []
    for c in formula:
        match c:
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
                verity.append(c)
    return verity[0]
