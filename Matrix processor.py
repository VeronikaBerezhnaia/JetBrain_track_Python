def enter_matrix (rows=0, which='first'):
    print(f'Enter {which} matrix')
#     m = [[int(k) for k in input().split() if ("." in k) else float(k)] for i in range(a)] # doesn't work
    m = [[float(k) for k in input().split()] for i in range(rows)]
    return m
   
def matmult():
    raw = input('Enter size of second matrix:')
    a, b = int(raw[0]), int(raw[2])
    m1 = enter_matrix(a)
    raw = input('Enter size of second matrix:')
    c, d = int(raw[0]), int(raw[2])
    m2 = enter_matrix(c, 'second')
    if  b != c:
        print('The operation cannot be performed.')
    else:
        result = [[sum([m1[i][k] * m2[k][j] for k in range(b)]) for j in range(d)]for i in range(a)]
        print('The result is:')
        print("\n".join(" ".join(str(value) for value in row) for row in result))

def matadd():
    raw = input('Enter size of first matrix:')
    a, b = int(raw[0]), int(raw[2])
    m1 = enter_matrix(a)
    raw = input('Enter size of second matrix:')
    c, d = int(raw[0]), int(raw[2])
    m2 = enter_matrix(c, 'second')
    if a != c or b != d:
        print('The operation cannot be performed.')
    else:
        print('The result is:')
        for i in range(a):
            for j in range(b):
                print (m1[i][j] + m2[i][j], end = ' ')
            print()

def matscal():
    raw = input('Enter size of matrix:')
    a, b = int(raw[0]), int(raw[2])
    m1 = enter_matrix(a)
    print('Enter constant:')
    c = input()
    c = float(c) if '.' in c else int(c)
    print('The result is:')
    for i in range(a):
        for j in range(b):
            print (int(m1[i][j]) * c, end = ' ')
        print()

def transpose():
    choice = input ('1. Main diagonal\n2. Side diagonal\n3.Vertical line\n4. Horizontal line\nYour choice:')
    raw = input('Enter size of matrix:')
    a, b = int(raw[0]), int(raw[2])
    m1 = enter_matrix(a)    
    if choice == '1':
        result = [[m1[j][i] for j in range(b)] for i in range (a)]
    if choice == '2':
        result = [[m1[j][i] for j in range(b-1, -1, -1)] for i in range (a-1, -1, -1)]
    if choice == '3':
        result = [[m1[i][j] for j in range(b-1, -1, -1)] for i in range (a)]
    if choice == '4':
        result = [[m1[i][j] for j in range(b)] for i in range (a-1, -1, -1)]
    print("\n".join(" ".join(str(value) for value in row) for row in result))

    choice = ''
while choice != '0':
    print('1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n0. Exit')
    choice = input('Your choice:')
    if choice == '1':
        matadd()
    if choice == '2':
        matscal()
    if choice == '3':
        matmult()
    if choice == '4':
        transpose()
