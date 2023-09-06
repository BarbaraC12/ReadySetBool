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

def print_truth_table(formula: str):
    truth = []
    for c in formula:
        match c:
            case '!': # Negation
                tmp = truth.pop()
                truth.append(not tmp)
            case '&': # conjonction
                tmp = truth.pop()
                truth[-1] &= tmp
            case '|': # disjonction
                tmp = truth.pop()
                truth[-1] |= tmp
            case '^': # exclusive disjonction
                tmp = truth.pop()
                truth[-1] ^= tmp
            case '>': # material contition
                tmp = truth.pop()
                truth[-1] >= tmp
            case '=': # logical equivalence
                tmp = truth.pop()
                truth[-1] = tmp
            case _:
                truth.append(c) # hum don't work on str i need more info
    return truth[0]

