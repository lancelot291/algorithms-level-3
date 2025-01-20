def solution(array, commands):
    answer_array = []
    for command in commands:
        i, j, k = command
        new_array = sorted(array[i-1:j])
        answer_array.append(new_array[k-1])

    return answer_array

array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]   
print(solution(array, commands))     