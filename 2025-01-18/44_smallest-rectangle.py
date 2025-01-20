def solution(sizes):
    max_height = 0
    max_width = 0

    for w, h in sizes:
        w = max(w, h)
        h = min(w, h)
        max_height = max(max_height, h)
        max_width = max(max_width, w)

    
