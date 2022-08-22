
#hold merge sort
#hold quicksort
#holdheapsort 
#from classes import DrawingInfo, DrawingManager
import pygame
pygame.init()

#take in a DrawingInfo object, a draw_manager object, and boolean
def bubble_sort(draw_info, manager, ascending = True):
    lst = draw_info.lst #updated list
    dm = manager #functions

    for i in range(len(lst)- 1):
        for j in range(len(lst) - 1 - i):
            bar1 = lst[j] #bars
            bar2 = lst[j + 1]

            if (bar1.sort_val > bar2.sort_val and ascending ) or (bar1.sort_val < bar2.sort_val and not ascending):
                lst[j], lst[j + 1] = lst[j + 1], lst[j] #swaps
                dm.draw_list(draw_info, {j: draw_info.GREEN, j+1: draw_info.RED}, True)
                yield True #allows for program to respond to other keys during sorting process
    
    return lst

def insertion_sort(draw_info, manager, ascending=True):
    lst = draw_info.lst #updated list
    dm = manager #functions

    for i in range(1, len(lst)):
        current = lst[i]

        while True:
            ascending_sort = i > 0 and lst[i - 1].sort_val > current.sort_val and ascending
            descending_sort = i > 0 and lst[i - 1].sort_val < current.sort_val and not ascending

            if not ascending_sort and not descending_sort:
                break

            lst[i] = lst[i - 1]
            i = i - 1
            lst[i] = current
            dm.draw_list(draw_info, {i - 1: draw_info.GREEN, i: draw_info.RED}, True)
            yield True

    return lst

def selection_sort(draw_info, manager, ascending=True):
    lst = draw_info.lst
    dm = manager

    num_vals = range(0, len(lst)-1)

    for i in num_vals:
        best_value = i
        for j in range(i+1, len(lst)):
            ascending_sort = lst[j].sort_val < lst[best_value].sort_val and ascending
            descending_sort = lst[j].sort_val > lst[best_value].sort_val and not ascending

            if ascending_sort: #"angled brackets not allowed in youtube description"
                best_value = j
            elif descending_sort:
                best_value = j

        if best_value != i:
            lst[best_value], lst[i] = lst[i], lst[best_value]
            dm.draw_list(draw_info, {best_value: draw_info.GREEN, i: draw_info.RED}, True)
            yield True

    return lst

def heapify(draw_info, list_size, index, manager, ascending):
    dm = manager
    lst = draw_info.lst
    left = 2*index+1
    right = 2*index+2
    max = index
    #if left chld is in scope and greater than parent
    if left < list_size and  lst[left].sort_val > lst[max].sort_val and ascending:
        max = left
    elif left < list_size and  lst[left].sort_val < lst[max].sort_val and not ascending:
        max = left

    #if right chld is in scope and greater than parent
    if right < list_size and  lst[right].sort_val > lst[max].sort_val and ascending:
        max = right
    elif right < list_size and  lst[right].sort_val < lst[max].sort_val and not ascending:
        max = right

    if(max!=index):
        lst[(index)], lst[(max)] = lst[(max)], lst[(index)] #defined in algorithm!!
        lst[(index)].x = draw_info.start_x + index * draw_info.bar_width 
        lst[(max)].x = draw_info.start_x + max * draw_info.bar_width  
        #dm.draw_list(draw_info, {index : draw_info.GREEN, max: draw_info.RED}, True)
        heapify(draw_info, list_size,max,dm,ascending)

    return lst #necessarry?


def heap_sort(draw_info, manager, ascending=True):
    dm = manager
    size = len(draw_info.lst)

    for i in range(size//2-1, -1, -1): #FIXME how to count down in python, whiel?
        draw_info.lst = heapify(draw_info,size, i, dm, ascending)

    for i in range(size-1,0,-1):
        draw_info.lst[i],  draw_info.lst[0] =  draw_info.lst[0],  draw_info.lst[i]
        dm.draw_list(draw_info, {i : draw_info.GREEN, 0: draw_info.RED}, True)
        draw_info.lst = heapify(draw_info,i, 0,dm, ascending)
        yield True
    
    return draw_info.lst