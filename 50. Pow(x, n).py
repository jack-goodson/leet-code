def myPow(x: float, n: int) -> float:
    # x^n
    num: float = x
    iterations: int = abs(n)
    if n == 0:
        return 1
    if n == 1:
        return x
    if abs(x) <= 0.00001:
        return 0
    for i in range(iterations-1):
        num *= x
    if n < 0:
        return 1/num
    else:
        return num
print(myPow(-2, 2))

