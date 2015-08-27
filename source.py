from mat import Mat
from vec import Vec
from random import *
EPSILON = 0.000001
def generate_listlist(n, m ,upper_limit = 10):
    return [[randint(0, upper_limit) for j in range(m)]for i in range(n)]

def generate_mat(n, m ,upper_limit = 10):
    return Mat(generate_listlist(n, m ,upper_limit))

def is_zero(n):
    if abs(n)<EPSILON:
        return True

def gaussian_elimination(listlist):
    if type(listlist)==Mat:
        listlist = [[listlist[i][j] for j in range(listlist.colLen)] for i in range(listlist.rowLen)]
    assert len(listlist)>0
    vecNum = len(listlist)
    veclist = [Vec(listlist[i]) for i in range(vecNum)]
    length = veclist[0].length()
    added_rowIndex = set()
    for pivot in range(length):
        row = []
        rowIndex = None
        for i in range(vecNum):
            vec = veclist[i]
            if(vec[pivot]!=0 and not i in added_rowIndex):
                row = vec
                rowIndex = i
                break
        if rowIndex == None:
            continue
        else:
            added_rowIndex.add(rowIndex)
            for i in range(vecNum):
                if i == rowIndex:
                    continue
                vec = veclist[i]
                if not is_zero(vec[pivot]):
                    veclist[i] = row - row[pivot]/vec[pivot]*vec
    return veclist
def row_reduced_form(veclist):
    for idx in range(len(veclist)):
        vec = veclist[idx]
        pivot_val = None
        for idx2 in range(len(vec)):
            if(not is_zero(vec[idx2])):
                pivot_val = vec[idx2]
                break
        if(pivot_val!=None):
            veclist[idx] = (1.0/pivot_val)*vec
    return veclist

def row_reduce(mat):
    return row_reduced_form(gaussian_elimination(mat.mat))


def solve_homogenious(listlist):
    '''
    input: a 2-D list represents a linear equation system
    output:a solution for the system
    '''    
    veclist = gaussian_elimination(listlist)
    print(veclist)
    x = zero_vector(veclist[0].length())
    vecLen = veclist[0].length()
    vecNum = len(veclist)
    col_pos = vecLen-1
    row_pos = vecNum-1
    while row_pos>=0:
    #not very efficient, can be improved by storing the first non zero index 
    #in the instance
        firstIndex = -1
        for i in range(vecLen):
            if(not is_zero(veclist[row_pos][i])):
                firstIndex = i
                break
        if firstIndex==-1:
            row_pos-=1
            continue
        for i in range(firstIndex+1, col_pos+1):
            x[i] = randint(1,100)
        x[firstIndex] = -x*veclist[row_pos]/veclist[row_pos][firstIndex]
        col_pos = firstIndex-1
        row_pos-= 1
    #set free variables
    for i in range(col_pos+1):
        x[i] = randint(1,100)

    return x


def getitem(mat , r):
    return mat.mat[r]

def identity_mat(n):
    bar = [[1 if i==j else 0 for i in range(n)]for j in range(n)]
    return Mat(bar)

def mat_mat_mul(mat1 , mat2):
    assert mat1.colLen == mat2.rowLen
    rowLen = mat1.rowLen
    colLen = mat2.colLen
    res = []
    for r in range(rowLen):
        res.append([])
        for c in range(colLen):
            acc = 0
            for k in range(mat1.colLen):
                acc+= mat1[r][k] * mat2[k][c]
            res[r].append(acc)
    return Mat(res)

def mat_vec_mul(mat ,vec):
    assert mat.colLen == vec.length()
    res = []
    for r in range(mat.rowLen):
        acc = 0
        for c in range(vec.length()):
            acc += mat[r][c] * vec[c]
        res.append(acc)
    return Vec(res)

def mat_scalar_mul(mat, k):
    res = Mat([[mat[i][j] for j in range(mat.colLen)] for i in range(mat.rowLen)])
    for i in range(mat.rowLen):
        for j in range(mat.colLen):
            res[i][j] *= k
    return res

def merge_by_col(mat1,mat2):
    assert mat1.rowLen == mat2.rowLen
    c1 = mat1.colLen
    c2 = mat2.colLen
    foo = []
    for i in range(mat1.rowLen):
        foo.append([])
        for j in range(c1):
            foo[i].append(mat1[i][j])
        for j in range(c2):
            foo[i].append(mat2[i][j])
    return Mat(foo)
            


def inv_mat(mat):
    assert mat.rowLen == mat.colLen
    n = mat.rowLen
    matI = merge_by_col(mat,identity_mat(n))
    reduced_matrix = row_reduce(matI)
    isInvertible = True
    
    if not isInvertible:
        print("This matrix is not invertible")
        return None
    print(matI)
    print("reduced matrix:")
    print(reduced_matrix)
    
