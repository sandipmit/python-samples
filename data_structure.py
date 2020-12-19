def list_comprehension_transpose_matrix():
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print('Orginal matrix ', matrix)
    #m = matrix[:]
    transposed = [[row[i] for row in matrix] for i in range(3)]
    print(transposed)

def del_stmt():
    a = [0, 1, 2, 3, 4, 5, 6, 7]
    del a[0]
    print(a)

    del a[2:4]
    print(a)

    #Removes all elements from the list but keeps the list reference variable a
    del a[:]
    print(a)

    #Removes entire list including reference variable a. If anyone tries to use it later, they will get an exception
    del a

def set_operations():
    a = set('abcdefg')
    b = set('efghijk')
    print (sorted(a - b))
    print(sorted(a | b))
    print(sorted(a & b))
    print(sorted(a ^ b))

def set_comprehension():
    a = {x for x in 'abcdefg' if x not in 'abc'}
    print(a)

def dictionary_test():
    dict = {1:'one', 2:'two', 3:'three'}
    print('first entry - ', dict[1])
    dict[4] = 'Four'
    print('New dictionary after adding 4 - ', dict)
    print('All keys - ', list(dict.keys()))
    del dict[1]
    print('Dictionary after deleting first entry - ', dict)

def sequence_comparision():
    print('(1,2,3) < (1,2,4) - ', (1,2,3) < (1,2,4))
    print('[1,2,3] < [1,2,4] - ', [1,2,3] < [1,2,4])
    print("'ABC' < 'C' < 'PASCAL' < 'PYTHON' - ", 'ABC' < 'C' < 'PASCAL' < 'PYTHON')
    print('(1,2,3,4) < (1,2,3) - ' , (1,2,3,4) < (1,2,3))
    print('(1,2,3) < (1,2,3,4) - ', (1, 2, 3) < (1, 2, 3, 4))
    print('(1,2,3) == (1.0,2.0,3.0) - ', (1,2,3) == (1.0,2.0,3.0))
    print("(1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4)) - " , (1, 2, ('aa', 'ab')) < (1, 2, ('abc', 'a'), 4))

