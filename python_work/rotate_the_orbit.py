array = [
    [1,  2,  3,  4,  5,  6,  7],
    [8,  9, 10,  1,  2,  3,  4],
    [10, 11, 12, 13, 14, 15, 16],
    [0,  9,  8,  7,  6,  5,  4],
    [2,  4,  6,  8, 10,  9,  8],
    [4,  8,  0,  9,  5,  7,  3],
    [7,  6,  8,  2,  1,  0,  6]
]
def print_the_array(array):
    i = 0
    while i < 7:
        j = 0
        while j < 7:
            print(f"{array[i][j]:2}", end=" ")
            j = j + 1
        print()
        i = i + 1
def rotation_positive(array,n):
    i, j = n, n
    T = array[n][n]
    while j != 6-n:
        array[i][j+1], T = T, array[i][j+1]
        j = j + 1
    while i != 6-n:
        array[i+1][j], T = T, array[i+1][j]
        i = i + 1
    while j != n:
        array[i][j-1], T = T, array[i][j-1]
        j = j - 1
    while i != n:
        array[i-1][j], T = T, array[i-1][j]
        i = i - 1
    return array
def rotation_negative(array, n):
    i, j = n, n
    T = array[n][n]
    while i != 6-n:
        array[i+1][j], T = T, array[i+1][j]
        i = i + 1
    while j != 6-n:
        array[i][j+1], T = T, array[i][j+1]
        j = j + 1
    while i != n:
        array[i-1][j], T = T, array[i-1][j]
        i = i - 1
    while j != n:
        array[i][j-1], T = T, array[i][j-1]
        j = j - 1
    return array
def rotations(array,n,r):
    if r >= 0:
        while r != 0:
            rotation_positive(array,n)
            r = r - 1
    else:
        while r != 0:
            rotation_negative(array,n)
            r = r + 1
    return array
n = int(input("Please input an orbit number (0 <= n <= 2): "))
r = int(input("Please input a rotation number: "))
print("\nOriginal array:")
print_the_array(array)
print("\nRotated array:")
print_the_array(rotations(array, n, r))

