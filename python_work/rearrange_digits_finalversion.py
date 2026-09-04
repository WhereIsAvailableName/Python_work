def swap(f, i, j):
    f[i], f[j] = f[j], f[i]

# Higher number
def find_stop_higher(f):
    stop = 8
    #whether the numbers are ascending from right to left
    while stop >= 0 and f[stop] >= f[stop + 1]:
        stop = stop - 1
    return stop

def find_swap_index_higher(f, stop):
    swap_idx = 9
    while swap_idx > stop and f[swap_idx] <= f[stop]:
        swap_idx = swap_idx - 1
    swap(f, stop, swap_idx)

def reverse_higher(f, stop):
    find_swap_index_higher(f, stop)
    left = stop + 1
    right = 9
    while left < right:
        if f[left] > f[right]:
            swap(f, left, right)
        left = left + 1
        right = right - 1
    return f

# Smaller number
def find_stop_smaller(f):
    stop = 8
    while stop >= 0 and f[stop] <= f[stop + 1]:
        stop = stop - 1
    return stop

def find_swap_index_smaller(f, stop):
    swap_idx = 9
    #whether the numbers are descending from right to left
    while swap_idx > stop and f[swap_idx] >= f[stop]:
        swap_idx = swap_idx - 1
    swap(f, stop, swap_idx)

def reverse_smaller(f, stop):
    find_swap_index_smaller(f, stop)
    left = stop + 1
    right = 9
    while left < right:
        if f[left] < f[right]:
            swap(f, left, right)
        left = left + 1
        right = right - 1
    return f

def turn_num_into_list(num):
    f = []
    while num != 0:
        f.insert(0, num % 10)
        num = num // 10
    return f

def turn_list_into_num(f):
    result = 0
    i = 0
    while i != 10:
        result = result * 10 + f[i]
        i = i + 1
    return result

def next_higher_number(num):
    f = turn_num_into_list(num)
    stop = find_stop_higher(f)
    if stop == -1:
        return None
    reverse_higher(f, stop)
    return turn_list_into_num(f)

def next_smaller_number(num):
    f = turn_num_into_list(num)
    stop = find_stop_smaller(f)
    if stop == -1:
        return None
    reverse_smaller(f, stop)
    return turn_list_into_num(f)

num = int(input("Please input a 10-digit number: "))
print("Next higher number:", next_higher_number(num))
print("Next smaller number:", next_smaller_number(num))
