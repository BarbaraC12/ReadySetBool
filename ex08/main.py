from powerset import powerset

print("********** POWERSET **********")
print(powerset([1, 2, 3]))
# [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
print(powerset([]))
# [[]]
print(powerset([5]))
# [[], [5]]
