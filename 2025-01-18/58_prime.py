
def is_prime(n):
    """Check if a number is prime."""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def solution(nums):
    count = 0
    length = len(nums)
    for i in range(0, length):
        for j in range(i+1, length):
           for k in range(j+1, length):
               if(prime(nums[i]+nums[j]+nums[k])):
                   count+=1

    return count

nums = [1, 2, 7, 6, 4]
print(solution(nums)) # 4