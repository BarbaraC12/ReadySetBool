# Program who take a string to evaluate veracity without using arithmetic operator
# Allowed operator: 
#    • & (bitwise AND)
#    • | (bitwise OR)
#    • = (assignment)
#    • > (implication)
#    • ! (negation operators)
#    • ++ or += 1 allowed only to increment index

def negation_normal_form(formula: str) -> str:
    # Stockage des sous-formules transformées
    stack = []

    # Opérateurs valides
    operators = {'!', '&', '|', '>', '='}

    for char in formula:
        if char.isalpha():  # VARIABLE
            stack.append(char)
        elif char in operators:
            if char == '!':  # NEGATION
                operand = stack.pop()
                if operand.endswith('&'):    # Negation with Conjonction (AND)
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(f"{a}!{b}!|")
                elif operand.endswith('|'):  # Negation with Disjonction (OR)
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(f"{a}!{b}!&")
                else:  # Negation
                    stack.append(f"{operand}!")
            elif char == '&':  # CONJONCTION
                b = stack.pop()
                a = stack.pop()
                stack.append(f"{a}{b}&")
            elif char == '|':  # DISJONCTION
                b = stack.pop()
                a = stack.pop()
                stack.append(f"{a}{b}|")
            elif char == '>':  # IMPLICATION
                b = stack.pop()
                a = stack.pop()
                stack.append(f"{a}!{b}|")
            elif char == '=':  # ASSIGNMENT
                b = stack.pop()
                a = stack.pop()
                stack.append(f"{a}{b}&{a}!{b}!&|")
        else:
            return "Invalid formula."

    return stack.pop()
