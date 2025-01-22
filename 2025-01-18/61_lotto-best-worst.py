def solution(lottos, win_nums):
    zero = lottos.count(0)  
    intersection = list(set(lottos).intersection(set(win_nums)))
    max_score = len(intersection) + zero 
    min_score = len(intersection) 

    max_rank = 7-max_score if max_score > 1 else 6
    min_rank = 7-min_score if min_score > 1 else 6

    return [max_rank, min_rank]

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums)) # [3, 5]

