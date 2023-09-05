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
    evaluate = []

    for c in string:
        match c:
            case '1':
                verity.append(True)
            case '0':
                verity.append(False)
            case _:
                evaluate.append(c)
        
    return a

print(eval_formula("10&"));      # false
print(eval_formula("10|"));      # true
print(eval_formula("11>"));      # true
print(eval_formula("10="));      # false
print(eval_formula("1011||="));  # true
