def rotate(digits, n,x = "",id=0):
    global list_rotations
    if id == 0:
        list_rotations=list()
    for id, num in enumerate(digits):
        if len(x + num) == n and not "0" in (x + num):
            list_rotations.append(int(x+num))
        else:
            cloned_dig = list(digits).copy()
            cloned_dig.pop(id)
            rotate("".join(cloned_dig), n,x+num, id+1)
    return sorted(list_rotations)

def check_prime(x):
    if x == 2 or x==3:
        return True
    for num in range(2, int((x ** 0.5))+1):
        if x % num == 0:
            return False
    return True

def compute_circular_primes(number):
    return list([i for i in range(2,number) if check_prime(i) if not False in [check_prime(j) for j in rotate(str(i), len(str(i)))]])

print(len(compute_circular_primes(int(input()))))
