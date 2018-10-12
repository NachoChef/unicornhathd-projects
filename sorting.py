import unicornhathd as uh
import random, time

uh.rotation(270)
uh.brightness(0.5)
DISP_X, DISP_Y = uh.get_shape()

SUM_IND = -1
RGB_IND = -2
MOD_IND = -3

def build_array():
    disp = []
    for _ in range(DISP_X):
        row_sum = random.randint(1, DISP_Y)
        row = [1 if ind < row_sum else 0 for ind in range(DISP_Y)]
        row.append(False)
        row.append((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        row.append(row_sum)
        disp.append(row)
    return disp
#end build_array

def show_array(arr, efficient=True):
    for x in range(len(arr)):
        if arr[x][MOD_IND] is True or not efficient:    # if efficient mode activated, only update buffer if row is changed!
            arr[x][MOD_IND] = False
            for y in range(len(arr)):
                val = arr[x][y]
                uh.set_pixel(x, y, arr[x][y] * arr[x][RGB_IND][0], arr[x][y] * arr[x][RGB_IND][1], arr[x][y] * arr[x][RGB_IND][2])
    uh.show()
#end show_array

def bubble_sort(arr):
    for i in range(len(arr)):
        for j in range(len(arr) - 1 - i):
            if arr[j][SUM_IND] > arr[j+1][SUM_IND]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                arr[j+1][MOD_IND], arr[j][MOD_IND] = True, True
                show_array(arr)
    return arr
#end bubble_sort

def insertion_sort(arr):
    for i in range(1, len(arr)):
        current = arr[i]
        pos = i
        while pos > 0 and arr[pos-1][SUM_IND] > current[SUM_IND]:
            arr[pos] = arr[pos-1]
            arr[pos][MOD_IND], arr[pos][MOD_IND] = True, True
            pos = pos - 1
            show_array(arr)
            #time.sleep(0.1)
          
        arr[pos] = current
        arr[pos][MOD_IND] = True
        show_array(arr)
    show_array(arr, False)
    return arr
#end insertion_sort

def quicksort(arr):
    # array is [16 * (0 or 1), (r, g, b), sum]
    
    # partitions
    less, equal, greater = [], [], []
    #show_array(arr)
    
    # this checks that there is more than 1 col in the list
    if len(arr) > 1 and type(arr[0]) is list:
        # pivot is a 20digit col with size at SUM_IND
        pivot = arr[len(arr) // 2]
        for col in arr:
            if col[SUM_IND] < pivot[SUM_IND]:
                less.append(col)
            if col[SUM_IND] == pivot[SUM_IND]:
                equal.append(col)
            if col[SUM_IND] > pivot[SUM_IND]:
                greater.append(col)
            show_array(less+equal+greater, False)
        return quicksort(less) + equal + quicksort(greater) 
    else: 
        return arr
#end quicksort

def main():
    my_array = build_array()
    show_array(my_array, False)
    time.sleep(1.0)
    arr = insertion_sort(my_array)
    show_array(arr, False)
    #time.sleep(1.0)
    #show_array(my_array)
    #time.sleep(1.0)
    #arr = quicksort(my_array)
    #show_array(arr)
    time.sleep(1)
    uh.off()
#end main

if __name__ == '__main__':
    main()
    
