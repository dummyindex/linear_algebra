
from source import *
from random import *
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

