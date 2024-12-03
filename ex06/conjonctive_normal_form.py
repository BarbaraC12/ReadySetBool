# Program who take a string to evaluate veracity without using arithmetic operator
# Allowed operator: 
#    • & (bitwise AND)
#    • | (bitwise OR)
#    • ! (negation operators)
#    • ++ or += 1 allowed only to increment index

def negation_normal_form_S(formula: str) -> str:
    """Convertion en NNF slim."""
    stack = []
    operators = {'!', '&', '|'}
    for char in formula:
        if char.isalpha():  # Variables
            stack.append(char)
        elif char in operators:
            if char == '!':
                operand = stack.pop()
                if operand.endswith('&'):  # !(A & B) -> A! B! |
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(f"{a}!{b}!|")
                elif operand.endswith('|'):  # !(A | B) -> A! B! &
                    b = stack.pop()
                    a = stack.pop()
                    stack.append(f"{a}!{b}!&")
                else:
                    stack.append(f"{operand}!")
            elif char == '&':
                b = stack.pop()
                a = stack.pop()
                stack.append(f"{a}{b}&")
            elif char == '|':
                b = stack.pop()
                a = stack.pop()
                stack.append(f"{a}{b}|")
    return stack.pop()


def distribute_and_over_or(a: str, b: str) -> str:
    """Décomposition et distribution de la formule"""
    if '&' in b:  # CONJONCTION
        # Extraction des composants
        components = []
        stack = []
        for char in b:
            if char.isalpha():
                stack.append(char)
            elif char == '&':
                r = stack.pop()
                l = stack.pop()
                components.append(f"{l}{r}")
            else:
                stack.append(char)
        distributed = [f"{a}{comp}|" for comp in components]
        return f"{'&'.join(distributed)}"
    return f"{a}{b}|"  # Normal disjunction


def conjunctive_normal_form(formula: str) -> str:
    """Conversion en CNF"""
    # 1) Conversion en NNF simplifié
    nnf_formula = negation_normal_form_S(formula)

    # 2) Conversion en CNF à l'aide de la stack
    stack = []
    for char in nnf_formula:
        if char.isalpha():  # VARIABLES
            stack.append(char)
        elif char == '!':  # Negation
            operand = stack.pop()
            stack.append(f"{operand}!")
        elif char == '&':  # CONJONCTION
            b = stack.pop()
            a = stack.pop()
            stack.append(f"{a}{b}&")
        elif char == '|':  # DISJONCTION
            b = stack.pop()
            a = stack.pop()
            if '&' in a or '&' in b:
                stack.append(distribute_and_over_or(a, b))
            else:
                stack.append(f"{a}{b}|")
   
    return stack.pop()
