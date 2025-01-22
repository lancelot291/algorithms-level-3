'''
def weak_num(n):
    weak_num = 0
    for i in range(1, n+1):
        if n%i == 0: weak_num+=1
    return weak_num
'''
def weak_num(num):
    """Return the number of divisors of a given number."""
    count = 0
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            count += 1
            if i != num // i:
                count += 1
    return count

def solution(number, limit, power):
    total_steel = 0
    for i in range(1, number+1):
        a = weak_num(i)
        if a <= limit:
            total_steel += a
        else:
            total_steel += power

    return total_steel 

number = 10
limit = 3
power = 2
print(solution(number, limit, power)) # 10
