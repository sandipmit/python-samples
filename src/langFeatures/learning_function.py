def fib(n):
    """Print Fibonacci series up to n"""
    a, b = 0 ,1
    while(a < n):
        print (a, end=' ')
        a, b = b, a + b
    print()

def default_args(prompt, retries=4, reminder = 'Plase try again...'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'yes', 'Yes'):
            print ("That's great")
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            print("That's sad")
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('Invalid user response')
        print (reminder)

def lambda_sorting():
    pairs = [(1, 'one'), (2, 'two'), (3, 'three')]
    print('Pairs before sorting', pairs)
    pairs.sort(key= lambda pair : pair[0])
    print('Pairs after sorting', pairs)

def lambda_make_increment(n:int):
    print(lambda_make_increment.__annotations__)
    print('n : '  , n)
    return lambda x : x + n;

if __name__ == "__main__":
    fib(100)
    default_args('Are feeling OK(Yes/No) ? ')
    lambda_sorting()

    #Testing increment function using lambda
    f = lambda_make_increment(10);
    print(f(0))
    print(f(1))
