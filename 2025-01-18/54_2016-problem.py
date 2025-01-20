def solution(a, b):
    num_of_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total_days = sum(num_of_days[:a-1])+b-1

    day = ["FRI", "SAT", "SUN", "MON", "TUE", "WED", "THU"]
    return day[(total_days)%7]

a = 5
b = 24
print(solution(a, b)) # TUE