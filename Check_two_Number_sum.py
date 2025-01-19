def check_two_sum(array,target):
    store_map = {}
    
    for i in array:
        if i in store_map:
            return True
        store_map[target-i]=i
    return False
    
    
print(check_two_sum([10,5,3,8],20))
