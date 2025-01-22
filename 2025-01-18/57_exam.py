def solution(answers):
    student_pattern_1 = [1, 2, 3, 4, 5]
    student_pattern_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_pattern_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    student_scores = [0, 0, 0]

    for i in range(len(answers)):
        if answers[i] == student_pattern_1[i % len(student_pattern_1)]:
            student_scores[0] += 1
        if answers[i] == student_pattern_2[i % len(student_pattern_2)]:
            student_scores[1] += 1
        if answers[i] == student_pattern_3[i % len(student_pattern_3)]:
            student_scores[2] += 1

    max_score = max(student_scores)

    return [i + 1 for i in range(3) if student_scores[i] == max_score]

answers = [1, 3, 2, 4, 2]
print(solution(answers)) # [1, 2, 3]



