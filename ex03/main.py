from boolean_eval import eval_formula

print("********* EVAL FORM *********")
print(eval_formula("hdh!"))     # false
print(eval_formula("1!"))       # false
print(eval_formula("10&"))      # false
print(eval_formula("11&"))      # true
print(eval_formula("00^"))      # false
print(eval_formula("01^"))      # true
print(eval_formula("10|"))      # true
print(eval_formula("11>"))      # true
print(eval_formula("10="))      # false
print(eval_formula("1011||="))  # true
