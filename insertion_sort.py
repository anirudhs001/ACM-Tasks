def insertion_sort(list):
    #remember the list length. list with 3 members has len = 3
    size = len(list)

    #increment marker from 1 till size - 1
    for marker in range(1, size ):
        
        #remember the list value at current marker position
        temp = list[marker]
        
        #now iterate through list between 0 and marker; look for correct position of marker
        i = marker - 1
        while i < marker and i >= 0:
            
            #current val > marker val
            if list[i] > temp:
                
                #shift current val forward
                list[i + 1] = list[i]
               
                #write marker val in place of current val(this position may be over written later, 
                # but this approach takes of the case when all values are greater than marker value) 
                list[i] = temp
                
            else:
                list[i + 1] = temp
                break

            i = i - 1
    print(f"SORTED List:{list}")

list = [1,3,2,5,4,8,7,6,9]
print(f"UNSORTED List:{list}")
insertion_sort(list)
