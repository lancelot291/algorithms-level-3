def solution(k, score):
    answer_list = []
    for i in range(len(score)):
        if i<k:
            answer_list.append(min(score[:i+1]))
            # the first k days
        else:
            if score[i] > sorted(score[:i], reverse=True)[k-1]:
                answer_list.append(sorted(score[:i+1], reverse=True)[k-1])
                # if the hall of fame needs a new score
            else: 
                answer_list.append(sorted(score[:i], reverse=True)[k-1])
                # if the hall of fame doesn't need a new score
    return answer_list

k = 3
score = [10, 100, 20, 150, 1, 100, 200]
print(solution(k, score)) 
