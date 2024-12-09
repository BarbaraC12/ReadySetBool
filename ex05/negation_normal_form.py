# Program who take a str and change to neg without using arithmetic operator
# Allowed operator:
#    • & (bitwise AND)
#    • | (bitwise OR)
#    • = (assignment)
#    • > (implication)
#    • ! (negation operators)
#    • ++ or += 1 allowed only to increment index

def negation_normal_form(formula: str) -> str:
    """Conversion en NNF"""
    # Stockage des sous-formules transformées
    stack = []

    # Opérateurs valides
    operators = {'!', '&', '|', '>', '='}

    for char in formula:
        if char.isalpha():  # VARIABLE
            stack.append(char)
        elif char in operators:
            if char == '&':  # CONJONCTION
                b = stack.pop()
                a = stack.pop()
                if formula.endswith('!'):
                    stack.append(f"{a}!{b}!|")
                else:
                    stack.append(f"{a}{b}&")
            elif char == '|':  # DISJONCTION
                b = stack.pop()
                a = stack.pop()
                if formula.endswith('!'):
                    stack.append(f"{a}!{b}!&")
                else:
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
