#Inverse RMQ: www.hackerrank.com/challenges/inverse-rmq

#number of distinct values in the array
n = int(input())

#m: determine the power of n 
m = 0
tmp = 1
while tmp != n:
    tmp *= 2
    m += 1

#read & sort the array
lst = list(map(int,input().split()))
lst = sorted(lst)

#count the number of occurences of array elements and construct tuples [elem, count of elem]
count = 1
tmp = lst[0]
clst = []
for i in range(1, 2 * n - 1):
    if lst[i] == tmp:
        count +=1
    else:
        clst.append([tmp, count])
        tmp = lst[i]
        count = 1
clst.append([tmp, count])
slst = [[] for _ in range(m + 1)]
arr = ['n' for _ in range(2 * n - 1)]
tmp = 0

#try to construct an output array and in case of error print 'NO'
try:
    
	#construct list of elements for each layer of tree starting from the top
    for i in range(n):
        tmp = clst[i]
        slst[m + 1 - tmp[1]].append(tmp[0])
    
    #record first element into array
    tmp = slst[0][0]
    shift = 1
    for k in range(m + 1):
        arr[shift - 1] = tmp
        shift += shift
    
     #record other element into array
    for i in range(1, m + 1):
        
        #shift count position to the most left node of the ith layer
        count = (1 << i) - 1
        
        #while there are elements in the ith layer list
        while slst[i]:
            j = 0
            tmp = slst[i]
            
            #find a first element that can be placed in current node
            while (tmp[j] < arr[count]):
                j += 1
            
            #increase count of node by 2 as each even node is already recorded as minimum of the upper layer
            count += 2
            
            #record current elemnt into the current node as well as all left nodes of depper layers
            shift = count
            for k in range(m - i + 1):
                arr[shift - 1] = tmp[j]
                shift += shift
            
            #remove current element from ith layer
            slst[i].pop(j)
    
    #if you're here then the output array is constrcuted
    print('YES')
    print(*arr)
except:
    print('NO')