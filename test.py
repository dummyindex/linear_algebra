
from source import *
from random import *
'''
u = Vec([1,2,3])
v = Vec([2,3,4])
A = generate_mat(2,4)
B = generate_mat(4,2)
A = [
    [-1,2,-1,-1,-1,-1],
    [2,-3, 2, 1, 2, 2],
    [0, 4,-1, 0, 1,-2]
    ]
Pc2b = row_reduce(Mat(A)).right_half_mat()

'''

def test_inv(case = 10, n = 5):
    I = identity_mat(n)
    for i in range(case):
        A = generate_mat(n,n)
        inv = inv_mat(A)
        if(inv==None):
            print("A is not invertible")
            continue
        print( (A*inv)==I)
        #print(A*inv)
def test_orthogonalize(vecLen = 4, dim = 4):
    veclist = generate_veclist(vecLen,dim)
    veclist = orthogonalize(veclist)
    for i in range(vecLen):
        for j in range(vecLen):
            if i!=j:
                print("iszero? "+str(is_zero(veclist[i]*veclist[j])))
    print(veclist)
    return veclist

