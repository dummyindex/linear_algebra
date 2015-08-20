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
                if vec[pivot] != 0:
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
        
def zero_vector(n):
    return Vec([0 for i in range(n)])
def det(mat):
    pass

