while True:
    try:
        A, B = map(int, input().split())
        print(A+B,end='')
    except EOFError:
        break