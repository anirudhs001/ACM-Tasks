def bubble_sort(list):
    #remember length of list. a list with 3 members has len = 3
    size = len(list)

    #increment i from 1 till size - 1
    #i is started from 1 coz so j reaches max value (size - 2) so j+1 remains in bounds
    for i in range(1, size):
        #increment j from 0 till size - i - 1 
        for j in range(0, size - i):
            #check if current value greater than next
            #if yes, swap
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp
    print(f"SORTED LIST:{list}")

list =[2,3,9,7,8,1,6,5,4]
print(f"ORIGINAL LIST:{list}")
bubble_sort(list)
