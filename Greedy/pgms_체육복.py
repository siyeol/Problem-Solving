def solution(n, lost, reserve):
    answer = 0
    
    
    _lost = set(lost) - set(reserve)
    _reserve = set(reserve) - set(lost)
    
    lost_len = len(_lost)

    for loser in _lost:
        left = loser-1
        right = loser+1
        
        if left in _reserve:
            _reserve.remove(left)
            lost_len -= 1
        elif right in _reserve:
            _reserve.remove(right)
            lost_len -= 1
            
    answer = n - lost_len
        
    return answer