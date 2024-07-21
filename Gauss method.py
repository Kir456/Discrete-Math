from fractions import Fraction


print('Write sizes of matrix: number of lines and number of columns(in spite of last column with values)')
a, b = map(int, input().split())
print('Write matrix')
matrix = []
for i in range(a):
    s = input()
    x = [Fraction(float(y)) for y in s.split()]
    matrix.append(x)


def gauss_method(matrix, a, b):
    for i in range(a):
        delit = matrix[i][i]
        if delit == 0:
            h = i+1
            while h < a:
                if matrix[h][i] != 0:
                    delit = matrix[h][i]
                    line = matrix[h]
                    matrix[h] = matrix[i]
                    matrix[i] = line
                    break
                else:
                    h += 1
            if delit == 0:
                k = i+1
                while k < b:
                    if matrix[i][k] != 0:
                        delit = matrix[i][k]
                        break
                    else:
                        k += 1
                if delit == 0:
                    return 'INF'
        for j in range(b+1):
            matrix[i][j] = Fraction(matrix[i][j], delit)
        for g in range(a):
            if g != i:
                if matrix[g].count(0) == b and matrix[g][-1] != 0:
                    return 'NO'
                ind = matrix[g][i]
                for n in range(b+1):
                    matrix[g][n] = Fraction(matrix[g][n])-Fraction(matrix[i][n]*ind)
    for ee in range(a):
        if matrix[ee].count(0) == b and matrix[ee][-1] != 0:
            return 'NO'
    for e in range(a):
        if (b-matrix[e].count(0)) >= 2 or (b-matrix[e].count(0)-matrix[e].count(1) >= 1):
            return 'INF'
    return 'YES'


if gauss_method(matrix, a, b) == 'NO':
    print('No solution')
elif gauss_method(matrix, a, b) == 'YES':
    print('One solution')
    res = ''
    for t in range(a):
        if t != a-1:
            res = res+str(float(matrix[t][-1]))+' '
        else:
            res = res+str(float(matrix[t][-1]))
    print(res)
elif gauss_method(matrix, a, b) == 'INF':
    print('Infinite number of solutions')