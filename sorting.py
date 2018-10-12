import unicornhathd as uh
import random, time
from utils import greeting

# rotate so that HDMI port is pointing up
uh.rotation(270)

# half brightness because camera :)
uh.brightness(0.5)

# RGB dimensions in case...something
DISP_X, DISP_Y = uh.get_shape()

# the sum of the column stored here:
SUM_IND = -1

# the random color tuple for the column stored here:
RGB_IND = -2

# the status of the column stored here:
MOD_IND = -3

# whether or not to activate slow mode
slow_mode = True

def pause():
    time.sleep(0.1) if slow_mode else None

def build_array():
    r''' Generates random columns with appropriate data '''
    disp = []
    for _ in range(DISP_X):
        row_sum = random.randint(1, DISP_Y)
        row = [1 if ind < row_sum else 0 for ind in range(DISP_Y)]
        row.append(False)
        row.append((random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)))
        row.append(row_sum)
        disp.append(row)
    return disp
# end build_array

def show_array(arr, efficient=True):
    r'''  Will loop through and display array. If `efficient` then only modified rows will be written to the buffer. '''
    for x in range(len(arr)):
        if arr[x][MOD_IND] is True or not efficient: 
            arr[x][MOD_IND] = False
            for y in range(len(arr)):
                state = arr[x][y]
                rgb = arr[x][RGB_IND]
                # if position value is 1 then we want to add color info, otherwise clear color info so we don't draw anything
                uh.set_pixel(x, y, state * rgb[0], state * rgb[1], state * rgb[2])
    uh.show()
# end show_array
    
def display(arr):
    for x in range(len(arr)):
        for y in range(len(arr)):
            pixel = arr[x][y]
            uh.set_pixel(x, y, pixel * 100, pixel * 100, pixel * 100)
    uh.show()
# end display

def bubble_sort(arr):
    for i in range(len(arr)):
        swaps = 0
        for j in range(len(arr) - 1 - i):
            if arr[j][SUM_IND] > arr[j+1][SUM_IND]:
                swaps = swaps + 1
                arr[j], arr[j+1] = arr[j+1], arr[j]
                arr[j+1][MOD_IND], arr[j][MOD_IND] = True, True
                
                # "bubble the hole"
                k = j
                while k > 0:
                    if arr[k][SUM_IND] < arr[k-1][SUM_IND]:
                        arr[k][SUM_IND], arr[k-1][SUM_IND] = arr[k-1][SUM_IND], arr[k][SUM_IND]
                        arr[k][MOD_IND], arr[k-1][MOD_IND] = True, True
                        k = k - 1
                        
                show_array(arr)
                pause()
        if swaps is 0:
            break
    return arr
# end bubble_sort

def insertion_sort(arr):
    for pos in range(1, len(arr)):
        current = arr[pos]
        current[MOD_IND] = True
        while pos > 0 and arr[pos-1][SUM_IND] > current[SUM_IND]:
            arr[pos] = arr[pos-1]
            arr[pos][MOD_IND], arr[pos-1][MOD_IND] = True, True
            pos = pos - 1
            show_array(arr)
            pause()
          
        arr[pos] = current
        show_array(arr)
    show_array(arr, False)
    return arr
# end insertion_sort

def quicksort(arr):
    # array is [16 * (0 or 1), (r, g, b), sum]
    
    # partitions
    less, equal, greater = [], [], []
    #show_array(arr)
    
    # this checks that there is more than 1 col in the list
    if len(arr) > 1 and type(arr[0]) is list:
        # pivot is a 19 item list with size at SUM_IND
        pivot = arr[len(arr) // 2]
        for col in arr:
            if col[SUM_IND] < pivot[SUM_IND]:
                less.append(col)
            if col[SUM_IND] is pivot[SUM_IND]:
                equal.append(col)
            if col[SUM_IND] > pivot[SUM_IND]:
                greater.append(col)
            show_array(less + equal + greater, False)
        return quicksort(less) + equal + quicksort(greater) 
    else: 
        return arr
# end quicksort

def main():
    uh.rotation(180)
    display(greeting)
    time.sleep(1.0)
    unsorted_array = build_array()
    uh.rotation(270)
    show_array(unsorted_array, False)
    time.sleep(1.0)
    arr = bubble_sort(list(unsorted_array))
    #show_array(arr, False)
    time.sleep(1.0)
    show_array(unsorted_array, False)
    time.sleep(1.0)
    arr = insertion_sort(list(unsorted_array))
    #show_array(arr, False)
    time.sleep(1.0)
    show_array(unsorted_array, False)
    time.sleep(1.0)
    arr = quicksort(list(unsorted_array))
    show_array(arr, False)
    time.sleep(1)
    uh.off()
# end main

if __name__ == '__main__':
    main()
    
