from fractions import Fraction


print('Write sizes of matrix: number of lines and number of columns(in spite of last column with values)')
a, b = map(int, input().split())
a_sp = a
print('Write matrix')
pre_matrix = []
for i in range(a):
    s = input()
    x = [Fraction(float(y)) for y in s.split()]
    pre_matrix.append(x)
f = []
for ii in range(a):
    f.append(pre_matrix[ii][b])
bb = ([0] for _ in range(b))
cnt = 0
e = []
for aa in bb:
    cnt += 1
    aa.remove(0)
    for jj in range(a):
        aa.append(pre_matrix[jj][cnt-1])
    e.append(aa)


def make_matrix(e, f, a, b):
    matrix = []
    f_list = []
    number = 0
    for e_cnt in range(b):
        for en_cnt in range(a):
            number += f[en_cnt]*e[e_cnt][en_cnt]
        f_list.append(number)
        number = 0
    e_list = []
    for e_num in range(b):
        pre_e_list = []
        number = 0
        for e_cnt in range(b):
            for en_cnt in range(a):
                number += e[e_num][en_cnt]*e[e_cnt][en_cnt]
            pre_e_list.append(number)
            number = 0
        e_list.append(pre_e_list)
    for add_num in range(b):
        add_matrix = []
        for the_num in range(b):
            add_matrix.append(e_list[add_num][the_num])
        add_matrix.append(f_list[add_num])
        matrix.append(add_matrix)
    return matrix, b


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
        for j in range(b+1):
            matrix[i][j] = Fraction(matrix[i][j], delit)
        for g in range(a):
            if g != i:
                ind = matrix[g][i]
                for n in range(b+1):
                    matrix[g][n] = Fraction(matrix[g][n])-Fraction(matrix[i][n]*ind)
    return 'YES'


matrix, b = make_matrix(e, f, a, b)
a = b
if gauss_method(matrix, a, b) == 'YES':
    print('Your answer')
    res = ''
    res_list = []
    for t in range(a):
        if t != a-1:
            res = res+str(float(matrix[t][-1]))+' '
            res_list.append(float(matrix[t][-1]))
        else:
            res = res+str(float(matrix[t][-1]))
            res_list.append(float(matrix[t][-1]))
    print(res)
    print('Sum of squared deviations')
    summa = 0
    for i in range(a_sp):
        num_sq = 0
        for j in range(b):
            num_sq += res_list[j]*pre_matrix[i][j]
        summa += (pre_matrix[i][b]-num_sq)**2
    print(summa)