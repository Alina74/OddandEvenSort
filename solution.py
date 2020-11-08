input_arr = [3, 4, 1, 2, 16, 27, 13]


def quicksort(array):
    if len(array) < 2:
        return array
    else:
        pivot = array[0]
        less = [i for i in array[1:] if i <= pivot]
        greater = [i for i in array[1:] if i > pivot]
    return quicksort(less) + [pivot] + quicksort(greater)


def solve(source):
    odd_arr = [x for x in source if x % 2 == 1]
    even_arr = [x for x in source if x % 2 == 0]

    odd_arr = quicksort(odd_arr)
    even_arr = quicksort(even_arr)

    odd_arr.reverse()

    res = even_arr + odd_arr

    return res


result = solve(input_arr)
print(result)
