def evaluate_formula(formula, values):
    """Evaluation de la formule"""
    stack = []
    for char in formula:
        if char.isalpha():  # VARIABLE
            stack.append(values[char])
        elif char == '!':  # NEGATIoN
            stack.append(not stack.pop())
        elif char == '&':  # CONJONCTION
            b = stack.pop()
            a = stack.pop()
            stack.append(a and b)
        elif char == '|':  # DISJONCTION
            b = stack.pop()
            a = stack.pop()
            stack.append(a or b)
        elif char == '^':  # XOR
            b = stack.pop()
            a = stack.pop()
            stack.append(a != b)
    return stack.pop()

def sat(formula: str) -> bool:
    """Vérifie que l'équation est satifaisable Opti"""
    variables = sorted(set(char for char in formula if char.isalpha()))
    num_vars = len(variables)

    # Parcourir toutes les solutions possible
    for i in range(2**num_vars):
        values = {var: bool((i >> j) & 1) for j, var in enumerate(variables)}

        # Evaluation de l'équation
        if evaluate_formula(formula, values):
            return True  # Retourne dés que c'est possible pour Opti

    return False
  
