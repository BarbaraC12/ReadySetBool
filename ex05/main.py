from negation_normal_form import negation_normal_form

print("****** NEGATION NORMAL FORM ******")
print(negation_normal_form("7!"))      # Invalid formula
print(negation_normal_form("AD%"))     # Invalid formula
print(negation_normal_form("AB&!"))    # A!B!|
print(negation_normal_form("AB|!"))    # A!B!&
print(negation_normal_form("AB>"))     # A!B|
print(negation_normal_form("AB="))     # AB&A!B!&|
print(negation_normal_form("AB|C&!"))  # A!B!&C!|
