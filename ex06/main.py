from conjonctive_normal_form import conjunctive_normal_form

print("****** CONJONCTIVE NORMAL FORM ******")
print(conjunctive_normal_form("AB&!"))     # A!B!|
print(conjunctive_normal_form("AB|!"))     # A!B!&
print(conjunctive_normal_form("AB|C&"))    # AB|C&
print(conjunctive_normal_form("AB|C|D|"))  # ABCD|||
print(conjunctive_normal_form("AB&C&D&"))  # ABCD&&&
print(conjunctive_normal_form("AB&!C!|"))  # A!B!C!||
print(conjunctive_normal_form("AB|!C!&"))  # A!B!C!&&
