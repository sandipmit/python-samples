def update_list_during_iteration():
    words = ['abcd', 'abcde', 'abcdef']
    for w in words[:]:
        print(w)
        if len(w) > 4:
            print ('big word')
            words.insert(0, w)
    print(words)

def test_range():
    for i in range(10):
        print(i)

def test_break():
    for i in range(2, 10):
        for j in range(2, i):
            if i % j == 0:
                print(i, 'equals', j, '*', (i//j));
                break
        else:
            print(i, 'is a prime number')

