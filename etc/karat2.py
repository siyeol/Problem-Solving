badge_records = [
   ["Martha",   "exit"],
   ["Paul",     "enter"],
   ["Martha",   "enter"],
   ["Steve",    "enter"],
   ["Martha",   "exit"],
   ["Jennifer", "enter"],
   ["Paul",     "enter"],
   ["Curtis",   "exit"],
   ["Curtis",   "enter"],
   ["Paul",     "exit"],
   ["Martha",   "enter"],
   ["Martha",   "exit"],
   ["Jennifer", "exit"],
   ["Paul",     "enter"],
   ["Paul",     "enter"],
   ["Martha",   "exit"],
   ["Paul",     "enter"],
   ["Paul",     "enter"],
   ["Paul",     "exit"],
   ["Paul",     "exit"] 
]

from collections import deque

def find(badge_records):
    no_exit = deque()
    no_enter = deque()

    office = deque()

    for name, trans in badge_records:
        if trans == 'exit':
            if len(office):
                no_enter.append(name)
            else:
                if name in office:
                    office.pop(office.index(name))
                else:
                    if name not in no_enter:
                        no_enter.append(name)
        elif trans == 'enter':
            if name in office:
                if name not in no_exit:
                    no_exit.append(name)
        
    for of in office:
        if of not in no_exit:
            no_exit.append(of)

    print(no_exit)
    print(no_enter)

find(badge_records)