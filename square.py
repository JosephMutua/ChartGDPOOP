 
def get_square(list):
    '''
    This is function that will accept a list of numbers as an input and 
    return a list of the numbers' squares.
    '''
    squared_values = []
    for i in list:
        squared_values.append(i*i)

    return squared_values

import time
start = time.time()
list = [1,2,3,4,12,23]

print (get_square(list))
end = time.time()
 
print (end - start)


import time
start = time.time()
list = [1,2,3,4,12,23,1,2,3,4,12,23,1,2,3,4,12,23,1,2,3,4,12,23,1,2,3,4,12,23,1,2,3,4,12,23,1,2,3,4,12,23,1,2,3,4,12,23,1,2,3,4,12,23,1,2,3,4,12,23,1,2,3,4,12,23,1,2,3,4,12,23]

print (get_square(list))
end = time.time()
 
print (end - start)




