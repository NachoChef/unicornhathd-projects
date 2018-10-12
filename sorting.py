import unicornhathd as uh
import random, time

uh.rotation(270)
uh.brightness(0.5)

# 17 X 16 = [-1] is sum

def build_array():
    disp = []
    for _ in range(16):
        row_sum = random.randint(1,16)
        row = [1 if ind < row_sum else 0 for ind in range(16)]
        row.append(row_sum)
        row.append(random.randint(1, 255))
        row.append(random.randint(1, 255))
        row.append(random.randint(1, 255))
        disp.append(row)
    return disp
#end build_array

def show_array(arr):
    for x in range(len(arr)):
        for y in range(len(arr)):
            val = arr[x][y]
            uh.set_pixel(x, y, arr[x][y] * arr[x][-1], arr[x][y] * arr[x][-2], arr[x][y] * arr[x][-3])
    uh.show()
#end show_array

def bubble_sort(arr):
    for i in range(16):
        for j in range(15-i):
            if arr[j][-4] > arr[j+1][-4]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                show_array(arr)
    return arr
#end bubble_sort

def insertion_sort(arr):
    for i in range(1, 16):
        current = arr[i]
        pos = i
        while pos > 0 and arr[pos-1][-4] > current[-4]:
            arr[pos] = arr[pos-1]
            pos = pos - 1
            show_array(arr)
            time.sleep(0.1)
          
        arr[pos] = current
        show_array(arr)
    return arr
#end insertion_sort

def quicksort(arr):
    # array is [16 * (0 or 1), sum, r, g, b]
    
    # partitions
    less, equal, greater = [], [], []
    #show_array(arr)
    
    # this checks that there is more than 1 col in the list
    if len(arr) > 1 and type(arr[0]) is list:
        # pivot is a 20digit col with size at -4
        pivot = arr[len(arr) // 2]
        for col in arr:
            if col[-4] < pivot[-4]:
                less.append(col)
            if col[-4] == pivot[-4]:
                equal.append(col)
            if col[-4] > pivot[-4]:
                greater.append(col)
            show_array(less+equal+greater)
        return quicksort(less) + equal + quicksort(greater) 
    else: 
        return arr
#end quicksort

def main():
    my_array = build_array()
    show_array(my_array)
    time.sleep(1.0)
    arr = bubble_sort(my_array)
    show_array(arr)
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
    
