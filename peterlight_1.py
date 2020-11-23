from itertools import permutations
def compute_n_p(num, n):
    return int(str.join("",list(sorted(permutations(num, len(num))))[int(n)-1]))

digits = input()
n = input()
print(compute_n_p(digits, n))