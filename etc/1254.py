string = input()

def is_palin(substr):
    length = len(substr)
    for i in range(length//2):
        if substr[i]!=substr[-i-1]:
            return False
    return True

substr_idx = 0
for i in range(len(string)):
    substr = string[i:]
    if is_palin(substr):
        substr_idx=i
        break

print(len(string)+substr_idx)