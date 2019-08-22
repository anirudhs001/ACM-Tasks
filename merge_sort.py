#1st list contains the unsorted list
LIST = [4,7,9,3,8,6,5,2,1]
# need 2nd list to store the sorted array while merging
SORTED_LIST = []
#make 2nd list copy of first(to make it the same size)
for i in LIST:
    SORTED_LIST.append(i)


def merge_sort(start, end):
    #################
    #DIVIDE THE LIST:
    #################
    
    #remember the middle value
    mid = int((start + end ) / 2)
   
    #divide list in sub-lists until all sub-lists become single membered
    if end > start :
        #divide the list 
        merge_sort(start, mid)
        merge_sort(mid + 1, end)
        

    ########################
    #JOIN THE SUB-LISTS NOW:
    ########################
    

    i = start
    j = mid + 1
    # k stores the position until which the merged list is filled
    for k in range(start, end + 1):
        if j <= end and i <= mid:
            if LIST[i] < LIST[j]:
                SORTED_LIST[k] = LIST[i]
                i = i + 1
            else:
                SORTED_LIST[k] = LIST[j]
                j = j + 1
        #when all elements of first list have been added to sorted list already
        elif i > mid:
            SORTED_LIST[k] = LIST[j]
            j = j + 1
        #when all elements of second list have been added....
        elif j > end:
            SORTED_LIST[k] = LIST[i]
            i = i + 1
        

    #make list same as sorted array 
    for k in range(start, end + 1):
        LIST[k] = SORTED_LIST[k]

print(f"Unsorted List:{LIST}")
merge_sort(0, len(LIST) - 1)
print(f"Sorted List:{SORTED_LIST}")