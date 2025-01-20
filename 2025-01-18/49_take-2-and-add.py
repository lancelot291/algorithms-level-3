def solution(numbers):
    answer_list = []
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] not in answer_list:
                answer_list.append(numbers[i] + numbers[j])

    return sorted(answer_list)

numbers = [2, 1, 3, 4, 1]
print(solution(numbers))

           