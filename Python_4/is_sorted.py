"""
check recursively if list is sorted
"""

def is_sorted(list):
    sorted = True
    items = len(list)
    medium = len(list) // 2
    left_list = list[:medium]
    right_list = list[medium:]

    if items > 4: #end script when left and right lists have 1 or 2 items
        if left_list[0] <= left_list[-1] <= right_list[0] <= right_list[-1]: #check
            sorted = is_sorted(left_list) and is_sorted(right_list) #true if both are sorted
        else:
            sorted = False # if not - return False
            return sorted
    else: #end of script - final check
        if left_list[0] <= left_list[-1] <= right_list[0] <= right_list[-1]:
            sorted = True
        else:
            sorted = False
            return sorted

    return sorted

list_sorted = [i for i in range(10)]
list_unsorted = list_sorted[:]

list_unsorted[3], list_unsorted[7] = list_unsorted[7], list_unsorted[3]

print('Is this list\n{} sorted? - {}\n'.format(list_sorted, is_sorted(list_sorted)))

print('But is this list\n{}\nsorted?\n{}'.format(list_unsorted, is_sorted(list_unsorted)))
