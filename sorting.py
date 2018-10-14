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

# whether or not to activate slow mode
slow_mode = True
slow_value = 0.1


def pause():
    """Sleeps `slow_value` seconds if `slow_mode` is True"""
    time.sleep(slow_value) if slow_mode else None


def build_array():
    """Generates random columns with appropriate data."""
    disp = uh.get_pixels()
    for i in range(len(disp)):
        r, g, b = random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)
        row_sum = random.randint(1, DISP_Y)
        disp[i] = [(r, g, b) if ind < row_sum else ([0] * 3) for ind in range(DISP_Y)]
        disp[i].append(row_sum)
    return disp
# end build_array


def update_screen(arr):
    """Calls library methods to update screen buffer for all pixels and display changes.

    :param arr: new buffer array
    :return: None
    """
    uh.set_pixels(arr[:][:-1])
    uh.show()
# end show_array


def row_swap(x_1, row_1, x_2, row_2):
    """Will change buffer rows s.t. buf[x_1] = row_2 and vice versa, then display.

    :param x_1: First index
    :param row_1: First row
    :param x_2: Second index
    :param row_2: Second row
    :return: None
    """
    uh.set_row(x_1, row_2[:-1])
    uh.set_row(x_2, row_1[:-1])
    uh.show()
# end row_swap


def update_row(pos, row):
    """Will update row for a given position and display it.

    :param pos: index of row to update
    :param row: new row to write to buffer
    :return: None
    """
    uh.set_row(pos, row[:-1])
    uh.show()


def blank_display():
    """Sets all pixels to gray and displays."""
    uh.set_all(100, 100, 100)
    uh.show()
# end display


def bubble_sort(arr):
    """Given array with sum at SUM_IND, perform bubble sort on entries and return output.

    :param arr: Input array, value to sort on at SUM_IND
    :return: Sorted array
    """
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - 1 - i):
            if arr[j][SUM_IND] > arr[j+1][SUM_IND]:
                swapped = True
                row_swap(j, arr[j], j+1, arr[j+1])
                arr[j], arr[j+1] = arr[j+1], arr[j]
                # "bubble the hole"
                k = j
                while k > 0:
                    if arr[k][SUM_IND] < arr[k-1][SUM_IND]:
                        row_swap(k, arr[k], k-1, arr[k-1])
                        arr[k][SUM_IND], arr[k-1][SUM_IND] = arr[k-1][SUM_IND], arr[k][SUM_IND]
                        k = k - 1
                        swapped = True

                pause()
        if not swapped:  # no changes == sorted
            break
    return arr
# end bubble_sort


def insertion_sort(arr):
    for pos in range(1, len(arr)):
        current = arr[pos]
        while pos > 0 and arr[pos-1][SUM_IND] > current[SUM_IND]:
            row_swap(pos, current, pos-1, arr[pos-1])
            arr[pos] = arr[pos-1]
            pos = pos - 1
            pause()
          
        arr[pos] = current
        update_screen(arr)
    update_screen(arr)
    return arr
# end insertion_sort


def quicksort(arr):
    """Quicksort algorithm for Python. I think the recursiveness is breaking the display portion.

    :param arr: The array to be sorted.
    :return: None
    """
    # partitions
    less, equal, greater = [], [], []
    
    # this checks that there is more than 1 col in the list...
    # because it's a list of lists, len will always be > 1 UNLESS we move into the inner list, which would be a tuple,
    # so we make sure to not do that
    if len(arr) > 1 and type(arr[0]) is list:
        pivot = arr[len(arr) // 2]
        for col in arr:
            if col[SUM_IND] < pivot[SUM_IND]:
                less.append(col)
            if col[SUM_IND] is pivot[SUM_IND]:
                equal.append(col)
            if col[SUM_IND] > pivot[SUM_IND]:
                greater.append(col)
            update_screen(less + equal + greater)
            pause()
        return quicksort(less) + equal + quicksort(greater) 
    else: 
        return arr
# end quicksort


def main():
    global slow_mode
    slow_mode = True
    uh.rotation(180)
    update_screen(greeting)
    time.sleep(1.0)
    unsorted_array = build_array()
    uh.rotation(270)
    update_screen(unsorted_array)
    time.sleep(1.0)
    arr = bubble_sort(list(unsorted_array))
    time.sleep(1.0)
    update_screen(unsorted_array)
    time.sleep(1.0)
    arr = insertion_sort(list(unsorted_array))
    time.sleep(1.0)
    update_screen(unsorted_array)
    time.sleep(1.0)
    arr = quicksort(list(unsorted_array))
    update_screen(arr)
    time.sleep(1)
    uh.off()
# end main


if __name__ == '__main__':
    main()

