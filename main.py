import random
import os
import numpy
from numpy import *

matrix = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
cc = [2, 4]

def insert():
    ch = random.choice(cc)

# Transfer the matrix
def transfer2(direction, matrix):
    mat = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
    cnt = -1

    for i in matrix:
        if direction == 1:
            cnt += 1
            a = matrix.count("")
            b = [j for j in range(len(i)) if i[j] == ""]
            c = [j for j in i if j != ""]
            k = 0

            while k < len(c) - 1:
                if c[k] == c[k + 1]:
                    c[k + 1] = c[k] * 2
                    c[k] = ""
                    k = k + 1
                k = k + 1

            f = [kk for kk in c if kk != ""]
            d = len(mat) - len(f)
            e = ["" for i in range(d)]
            e.extend(f)
            mat[cnt] = e

        if direction == 2:
            cnt += 1
            a = matrix.count("")
            b = [j for j in range(len(i)) if i[j] == ""]
            c = [j for j in i if j != ""]
            c = c[::-1]
            k = 0

            while k < len(c) - 1:
                if c[k] == c[k + 1]:
                    c[k + 1] = c[k] * 2
                    c[k] = ""
                    k = k + 1
                k = k + 1

            c = [k for k in c if k != ""]
            c = c[::-1]
            d = len(mat) - len(c)
            e = ["" for i in range(d)]
            c.extend(e)
            mat[cnt] = c

    return mat

def transfer(direction, matrix):
    mat1 = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
    jj = 0

    for k in range(len(matrix)):
        for kk in range(len(matrix)):
            mat1[k][kk] = matrix[kk][k]

    matrix = mat1
    mat = [["", "", "", ""], ["", "", "", ""], ["", "", "", ""], ["", "", "", ""]]
    cnt = -1

    for i in matrix:
        if direction == 4:
            cnt += 1
            a = matrix.count("")
            b = [j for j in range(len(i)) if i[j] == ""]
            c = [j for j in i if j != ""]
            k = 0

            while k < len(c) - 1:
                if c[k] == c[k + 1]:
                    c[k + 1] = c[k] * 2
                    c[k] = ""
                    k = k + 1
                k = k + 1

            f = [kk for kk in c if kk != ""]
            d = len(mat) - len(f)
            e = ["" for i in range(d)]
            e.extend(f)
            mat[cnt] = e

        if direction == 3:
            cnt += 1
            a = matrix.count("")
            b = [j for j in range(len(i)) if i[j] == ""]
            c = [j for j in i if j != ""]
            c = c[::-1]
            k = 0

            while k < len(c) - 1:
                if c[k] == c[k + 1]:
                    c[k + 1] = c[k] * 2
                    c[k] = ""
                    k = k + 1
                k = k + 1

            c = [k for k in c if k != ""]
            c = c[::-1]
            d = len(mat) - len(c)
            e = ["" for i in range(d)]
            c.extend(e)
            mat[cnt] = c

    for k in range(len(matrix)):
        for kk in range(len(matrix)):
            mat1[k][kk] = mat[kk][k]

    return mat1

def enter(mat):
    a = random.choice([2, 4])

    def sel():
        b = random.choice([0, 1, 2, 3])
        c = random.choice([0, 1, 2, 3])
        return b, c

    b, c = sel()

    if mat[b][c] == "":
        mat[b][c] = a
        return mat
    else:
        return enter(mat)

def matdis(matrix):
    a = numpy.array(matrix)
    a.shape = (4, 4)
    print(a)

def defeat1(mat):
    return all(cell != "" for row in mat for cell in row)

defeat = 0
matrix = enter(matrix)
matdis(matrix)

while defeat != 1:
    os.system('cls')
    matdis(matrix)
    print("1 for right \n2 for left \n3 for up \n4 for down")
    chs = int(input())

    if chs in (1, 2):
        matrix = transfer2(chs, matrix)
    if chs in (3, 4):
        matrix = transfer(chs, matrix)

    matrix = enter(matrix)
    defeat = 1
    defeat = defeat1(matrix)
    matdis(matrix)

    if defeat == 1:
        print("GAME OVER")
        break
