from adder import adder
from multiplier import multiplier
from gray_code import gray_code
from boolean_eval import eval_formula
from truth_table import print_truth_table
from negation_normal_form import negation_normal_form

print("********* ADDER *********")
print(adder(21, 2))
print(adder(1, 42))
print(adder(123, 321))
print(adder(1, 0))

print("********* MULTIPLIER *********")
print(multiplier(21, 2))
print(multiplier(1, 42))
print(multiplier(123, 321))
print(multiplier(1, 0))

print("********* GRAY CODE *********")
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

print("********* EVAL FORM *********")
print(eval_formula("1!"));       # false
print(eval_formula("10&"));      # false
print(eval_formula("11&"));      # true
print(eval_formula("00^"));      # false
print(eval_formula("01^"));      # true
print(eval_formula("10|"));      # true
print(eval_formula("11>"));      # true
print(eval_formula("10="));      # false
print(eval_formula("1011||="));  # true

print("********* TRUTH TAB *********")
print(print_truth_table("A"));
print(print_truth_table("AB="));
print(print_truth_table("AB&C|"));
print(print_truth_table("A&B&C|"));
print(print_truth_table("ABCDE"));

print("****** NEGATION NORMAL FORM ******")
print(negation_normal_form("AB&!"));   # A!B!|
print(negation_normal_form("AB|!"));   # A!B!&
print(negation_normal_form("AB>"));    # A!B|
print(negation_normal_form("AB="));    # AB&A!B!&|
print(negation_normal_form("AB|C&!")); # A!B!&C!|
	
print("****** CONJONCTIVE NORMAL FORM ******")
print(conjunctive_normal_form("AB&!"));     #A!B!|
print(conjunctive_normal_form("AB|!"));     #A!B!&
print(conjunctive_normal_form("AB|C&"));    #AB|C&
print(conjunctive_normal_form("AB|C|D|"));  #ABCD|||
print(conjunctive_normal_form("AB&C&D&"));  #ABCD&&&
print(conjunctive_normal_form("AB&!C!|"));  #A!B!C!||
print(conjunctive_normal_form("AB|!C!&"));  #A!B!C!&&

print("********** SAT **********")
print(sat("AB|"));   # true
print(sat("AB&"));   # true
print(sat("AA!&"));  # false
print(sat("AA^"));   # false


