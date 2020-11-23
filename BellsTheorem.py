def b_calculator(k):
    if k == 0 or k == 1:
        return 1
    else:
        ans_b = 0
        for num in range(0, k):
            if num == 0 or num == 1:
                ans_b += (1 * combination(k-1, num))
            else:
                ans_b += (b_calculator(num) * combination(k-1, num))
        return ans_b

def factorial(n):
    fact = 1
    for num in range(1,n+1):
        fact *= num
    return fact

def combination(n,r):
    return int((factorial(n))/(factorial(n-r)*factorial(r)))


def theorem(n):
    b_0 = 1
    b_1 = 1
    try:
        n = int(n)
        if n >= 0:
            pass
        else:
            return "error"

    except:
        return "error"
    if n == 0:
        return b_0
    elif n == 1:
        return b_1
    else:
        return b_calculator(n)

n = (input("Enter Your n Value: "))
answer = theorem(n)
if answer == "error":
    print("Error: Invalid 'n' Value")
else:
    print("Answer = " + str(answer))



