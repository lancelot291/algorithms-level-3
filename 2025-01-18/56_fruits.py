def solution(k, m, score):

    # reset
    sum = 0
    len_score = len(score)

    # the number of apples that will remain after dividing by m
    rest = len_score % m

    # get rid of the remaining apples
    score = sorted(score, reverse=True)[:len_score-rest]

    # sum the apples according to the condition
    for i in range(0, len_score-m+1, m):
        min_score_of_box = score[i+m-1]
        sum+=min_score_of_box*m

    # that's the answer
    return sum    
    
    
# example
score =  [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]
print(solution(4, 3, score)) 