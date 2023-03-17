from math import log2
def solution(numbers):
    
    def traversal(subtree, root):
        if root == '0':
            for sb in subtree:
                if sb != '0':
                    return False
                
        if len(subtree)==1:
            return True
        
        new_root = len(subtree)//2
        
        return traversal(subtree[:new_root], subtree[new_root]) and traversal(subtree[new_root+1:], subtree[new_root])
    
    
    answer = []
    for number in numbers:
        og_bin = bin(number).replace("0b", "")
        
        tree_height = int(log2(len(og_bin)))+1
        padding=2**tree_height -1 -len(og_bin)
        pad_bin = ('0'*padding+og_bin)
        
        if traversal(pad_bin, pad_bin[len(pad_bin)//2]):
            answer.append(1)
        else:
            answer.append(0)         
        
    return answer