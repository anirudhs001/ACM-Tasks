QUERY = 0

LIST = [1,2,3,4,5,6,7,8,9]

def binary_search(start, end):
    #remember the position
    mid = int((start + end) / 2)

    #when sub-list size is positive
    if end >= start :
        #found the element, hurray!
        if QUERY == LIST[mid]:
            print(f"found Query in the List at position : {mid + 1}(positions are ordinal) ")
        
        #if not found element,
        else:
            #divide the list
            if QUERY > LIST[mid]:
                #note the mid + 1 here since we know list[mid] is not equal to query
                #also mid + 1 can cause mid to be greater than end, that's when we know 
                #that query is not in list
                binary_search(mid + 1, end)
            else:
                #similarly mid - 1 and not just mid
                binary_search(start, mid - 1) 
    
    #when sub-list size becomes negative 
    else:
        print("Query not found!")
            

binary_search(0, len(LIST) - 1)
