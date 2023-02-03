from collections import deque

def solution(number, k):
    answer = ''
    
    dq = list()
    
    for digit in number:
        while dq and k>0 and dq[-1]<digit :
            dq.pop()
            k-=1
        dq.append(digit)
        
    if k>0:
        dq = dq[:-k]
        
    return "".join(dq)