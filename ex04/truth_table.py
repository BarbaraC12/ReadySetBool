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

def is_valid_formula(formula):
    """Vérifie la syntaxe de la formule"""
    valid_chars = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ&|^>=!')
    stack = []
    for char in formula:
        if char.isalpha():
            stack.append(char)
        elif char in valid_chars:
            if char in '&|^>=':
                if len(stack) < 2:
                    return False
                stack.pop()
                stack.pop()
            elif char == '!':
                if len(stack) < 1:
                    return false
                stack.pop()
            stack.append('x')
        else:
            return False
    return len(stack) == 1


def evaluate_formula(formula, values):
    """Evalue la formule de la table de vérité"""
    stack = []
    for char in formula:
        if char.isalpha():  # Variable
            stack.append(values[char])
        elif char == '&':  # Conjonction (AND)
            b = stack.pop()
            a = stack.pop()
            stack.append(a & b)
        elif char == '|':  # Disjonction (OR)
            b = stack.pop()
            a = stack.pop()
            stack.append(a | b)
        elif char == '^':  # Disjonction exclusive (XOR)
            b = stack.pop()
            a = stack.pop()
            stack.append(a ^ b)
        elif char == '!':  # Négation (NOT)
            a = stack.pop()
            stack.append(not a)
        elif char == '>':  # Implication
            b = stack.pop()
            a = stack.pop()
            stack.append((not a) | b)
        elif char == '=':  # Équivalence
            b = stack.pop()
            a = stack.pop()
            stack.append(a == b)
    return stack.pop()
 
def print_truth_table(formula: str):
    """Imprime la table de vérité formalisé"""
    if not is_valid_formula(formula):
        return("Formule invalide.")
        
    # Liste des variables distinctes dans la formule
    variables = sorted(set([char for char in formula if char.isalpha()]))

    # Nombre de variables
    num_variables = len(variables)

    # En-tête de la table
    header = "| " + " | ".join(variables) + " | = |"
    print(header)
    print("|" + "---|" * (num_variables + 1))

    # Génération des combinaisons de valeurs pour les variables
    for i in range(2 ** num_variables):
        # Conversion de l'indice en binaire
        binary = bin(i)[2:].zfill(num_variables)

        # Dictionnaire pour stocker les valeurs des variables
        values = {variables[j]: int(binary[j]) for j in range(num_variables)}

        # Calcul de la valeur de la formule pour les valeurs actuelles des variables
        result = evaluate_formula(formula, values)

        # Création de la ligne de la table
        row = "| " + " | ".join([str(values[var]) for var in variables]) + " | " + str(result) + " |"
        print(row)

    return("|" + "---|" * (num_variables + 1))


# Exemple d'utilisation

