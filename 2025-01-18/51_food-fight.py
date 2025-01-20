def solution(food):
    answer_list = []
    temp_list = []
    for i in range(1, len(food)):
        answer_list.append(str(i)*(food[i]//2))

    temp_list = answer_list[::-1]
    answer_list.append("0")

    answer_list.extend(temp_list)

    return "".join(answer_list)

food = [1, 3, 4, 6]
print(solution(food)) # 12210