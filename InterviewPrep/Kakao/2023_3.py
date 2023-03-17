from itertools import product

def solution(users, emoticons):
    U = len(users)
    E = len(emoticons)
    price=[[0]*E for _ in range(4)] #y = 할인율 , x = 이모지

    sale = [0.1, 0.2, 0.3, 0.4]

    plus_list = list()

    for perm in product(sale, repeat=E):
        imti_plus = 0
        imti_revenue = 0
        for dc, money in users:
            dc_thresh = dc*0.01
            money_thresh = money
            flag = False

            total_money = 0
            for idx, sale_rate in enumerate(perm):
                if sale_rate >= dc_thresh:
                    total_money+=emoticons[idx]*(1-sale_rate)
                if total_money>=money_thresh:
                    imti_plus+=1
                    flag = True
                    break
            
            if flag is False:
                imti_revenue+= total_money
        plus_list.append([imti_plus, int(imti_revenue)])

    plus_list.sort(key = lambda x:x[1], reverse=True)
    plus_list.sort(key= lambda x: x[0], reverse=True)
    return (plus_list[0])

users = [[40, 10000], [25, 10000]]	
emoticons = [7000, 9000]	

users = [[40, 2900], [23, 10000], [11, 5200], [5, 5900], [40, 3100], [27, 9200], [32, 6900]]	
emoticons = [1300, 1500, 1600, 4900]	
solution(users, emoticons)