from sat import sat

print("********** SAT **********")
print(sat("AB|"))   # true
print(sat("AB&"))   # true
print(sat("AA!&"))  # false
print(sat("AA^"))   # false
