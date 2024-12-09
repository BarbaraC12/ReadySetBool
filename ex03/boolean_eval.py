# Program who take a str to evaluate verity without using arithmetic operator
# Allowed operator:
#    • & (bitwise AND)
#    • | (bitwise OR)
#    • ^ (bitwise XOR)
#    • << (left shift)
#    • >> (right shift)
#    • = (assignment)
#    • ==, !=, <, >, <=, >= (comparison operators)
#    • ++ or += 1 allowed only to increment index

def eval_formula(formula: str) -> bool:
    truth = []
    for c in formula:
        match c:
            case '1':  # True
                truth.append(True)
            case '0':  # False
                truth.append(False)
            case '!':  # Negation
                tmp = truth.pop()
                truth.append(not tmp)
            case '&':  # conjonction
                tmp = truth.pop()
                truth[-1] &= tmp
            case '|':  # disjonction
                tmp = truth.pop()
                truth[-1] |= tmp
            case '^':  # exclusive disjonction
                tmp = truth.pop()
                truth[-1] ^= tmp
            case '>':  # material contition
                tmp = truth.pop()
                truth[-1] >= tmp
            case '=':  # logical equivalence
                tmp = truth.pop()
                truth[-1] = tmp
            case _:
                return False
    return truth[0]
