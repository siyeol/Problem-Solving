def solution(today, terms, privacies):
    answer = []
    
    now_y, now_m, now_d = map(int, today.split(sep='.'))
    now_total = now_y * 12 * 28 + now_m * 28+ now_d
    
    for idx, privacy in enumerate(privacies):
        day, law = privacy.split()
        #parse day
        dest_y, dest_m, dest_d = map(int, day.split(sep='.'))
        dest_total = dest_y * 12 * 28 + dest_m * 28+dest_d 
        
        for term in terms:
            if term[0] == law:
                period = int(term[2:])
                
                if dest_total + period*28 <= now_total:
                    answer.append(idx+1)

    return answer