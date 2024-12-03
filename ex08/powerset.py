def powerset(s: list[int]) -> list[list[int]]:
    """Genere le jeu de donnée de set."""
    n = len(s)
    result = []

    # Parcours de toutes les combinaisons possible (2^n sous-set)
    for i in range(2**n):
        subset = []
        for j in range(n):
            if (i >> j) & 1:
                subset.append(s[j])
        result.append(subset)

    return result

# print(powerset([1, 2, 3]));  # [[], [1], [2], [3], [1, 2], [1, 3], [2, 3], [1, 2, 3]]
# print(powerset([]));         # [[]]
# print(powerset([5]));        # [[], [5]]
