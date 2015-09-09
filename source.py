from mat import Mat
from vec import Vec
from random import *
from basic_utils import *
from math import *
def generate_mat(n, m ,upper_limit = 10):
    return Mat(generate_listlist(n, m ,upper_limit))
def generate_complex_mat(n,m, upper_limit = 10):
    return Mat(generate_complex_listlist(n, m ,upper_limit))
def generate_vec(n, upper_limit = 10):
    return Vec([randint(0,upper_limit) for i in range(n)])
def generate_veclist(listLen, dim , upper_limit = 10):
    return [generate_vec(dim,upper_limit) for i in range(listLen)]
    

def zero_vector(n):
    return Vec([0 for i in range(n)])
def gaussian_elimination(listlist):
    if type(listlist)==Mat:
        listlist = [[listlist[i][j] for j in range(listlist.colLen)] for i in range(listlist.rowLen)]
    assert len(listlist)>0
    vecNum = len(listlist)
    veclist = [Vec(listlist[i]) for i in range(vecNum)]
    length = len(veclist[0])
    added_rowIndex = set()
    row_order = []
    res = []
    for pivot in range(length):
        row = []
        rowIndex = None
        for i in range(vecNum):
            vec = veclist[i]
            if(not is_zero(vec[pivot]) and not i in added_rowIndex):
                row = vec
                rowIndex = i
                break
        if rowIndex == None:
            continue
        else:
            added_rowIndex.add(rowIndex)
            row_order.append(rowIndex)
            for i in range(vecNum):
                if i == rowIndex:
                    continue
                vec = veclist[i]
                if not is_zero(vec[pivot]):
                    veclist[i] = row - row[pivot]/vec[pivot]*vec
                
    for idx in row_order:
        res.append(veclist[idx])
    for i in range(len(veclist)):
        if not i in added_rowIndex:
            res.append(veclist[i])
    return res
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
    veclist =  row_reduced_form(gaussian_elimination(mat.mat))
    temp = []
    for vec in veclist:
        temp.append(vec.vec)
    return Mat(temp)
def solve_homogenious(listlist):
    '''
    input: a 2-D list represents a linear equation system
    output:a solution for the system
    '''    
    veclist = gaussian_elimination(listlist)
    print(veclist)
    x = zero_vector(len(veclist[0]))
    vecLen = len(veclist[0])
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

def solve(A,b):
    #deep copy
    assert type(A)==Mat and type(b)==Vec and A.rowLen == len(b)
    A = A.mat
    
    matlist = [[ float(A[i][j]) if type(A[i][j])==float else complex(A[i][j]) for j in range(len(A[i]))]for i in range(len(A))]
    veclist = [float(b[i]) if type(b[i])==float else complex(b[i]) for i in range(len(b))]
    for i in range(len(veclist)):
        matlist[i]+=[veclist[i]]
    reduced_mat = row_reduce(Mat(matlist))
    #has bugs, need fixed
    ans = zero_vector(reduced_mat.colLen-1)
    ans[-1] = -1
    col_pos = reduced_mat.colLen-2
    row_pos = reduced_mat.rowLen-1
    while(row_pos>=0):
        pass
def getitem(mat , r):
    return mat.mat[r]

def identity_mat(n):
    bar = [[1 if i==j else 0 for i in range(n)]for j in range(n)]
    return Mat(bar)

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
    det = mat.det()
    if( is_zero(det)):
        return None
    else:
        I = identity_mat(mat.rowLen)
        new_mat = merge_by_col(mat,I)
        reduced_mat = row_reduce(new_mat)
        inv_mat = reduced_mat.right_half_mat()
        return inv_mat


def check_eigenvalue(mat,v):
    assert mat.colLen==mat.rowLen
    foo = mat.copy()
    for i in range(mat.rowLen):
        foo[i][i] -= v
    det = foo.det()
    if det==0:
        return True
    else:
        return False

def orthogonalize(something):
    if type(something)==list:
        return orthogonalize_veclist(something)


def orthogonalize_veclist(veclist):
    '''
    Gram Schmidt Process!
    input : a veclist
    output: a orthogonalized veclist without change the value of veclist
    '''
    if len(veclist)==0:
        return []
    lengths = [veclist[0].length()**2]
    res = [veclist[0]]
    for i in range(1,len(veclist)):
        x = veclist[i].copy()
        for j in range(len(res)):
            x = x - (x*res[j]/lengths[j])*res[j]
        res.append(x)
        lengths.append(x.length()**2)
    return res

A = generate_mat(2,2)
b = Vec([1,2,3])
