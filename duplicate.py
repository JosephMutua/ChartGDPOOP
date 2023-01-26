def find_duplicate(list):
    '''
    This function will go through a list of numbers and return a list of number that have duplicates
    '''
    duplicates =  []
    for i in range (len(list)):
        for j in range(i+1, len(list)):
            if list[j] == list[i]:
                duplicates.append(list[i])

    return duplicates 

list = [1,2,2,3,4,12,3,23,2,3]

print(find_duplicate(list))
