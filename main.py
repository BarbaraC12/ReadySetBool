from adder import adder
from multiplier import multiplier
from gray_code import gray_code
from boolean_eval import eval_formula
from truth_table import print_truth_table

print(adder(21, 2))
print(adder(1, 42))
print(adder(123, 321))
print(adder(1, 0))

print(multiplier(21, 2))
print(multiplier(1, 42))
print(multiplier(123, 321))
print(multiplier(1, 0))

print(gray_code(2))
print(gray_code(3))
print(gray_code(4))
print(gray_code(5))
print(gray_code(6))
print(gray_code(7))
print(gray_code(8))
print(gray_code(21))
print(gray_code(42))
print(gray_code(44))

print(eval_formula("1!"));       # false
print(eval_formula("10&"));      # false
print(eval_formula("11&"));      # true
print(eval_formula("00^"));      # false
print(eval_formula("01^"));      # true
print(eval_formula("10|"));      # true
print(eval_formula("11>"));      # true
print(eval_formula("10="));      # false
print(eval_formula("1011||="));  # true

print(print_truth_table("AB&C|"));
# | A | B | C | = |$
# |---|---|---|---|$
# | 0 | 0 | 0 | 0 |$
# | 0 | 0 | 1 | 1 |$
# | 0 | 1 | 0 | 0 |$
# | 0 | 1 | 1 | 1 |$
# | 1 | 0 | 0 | 0 |$
# | 1 | 0 | 1 | 1 |$
# | 1 | 1 | 0 | 1 |$
# | 1 | 1 | 1 | 1 |$
