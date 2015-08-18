EPSILON = 0.0000001
def generate_listlist(n,m):
    return [[randint(0,100) for j in range(m)]for i in range(n)]
def is_zero(n):
    if abs(n)<EPSILON:
        return True
def zero_vector(n):
    return Vec([0 for i in range(n)])
def add(u,v):
    '''
    input:2 vectors
    output: result of adding 2 vectors
    '''
    assert u.length() == v.length()
    return Vec([u[i]+v[i] for i in range (v.length())])
def neg(v):
    res = v.copy()
    for key in range(v.length()):
        res[key] = -v[key]
    return res 
def getitem(v,k):
    assert v.length() > k
    return v.vec[k]

def setitem(v,k,val):
    assert v.length() > k 
    v.vec[k] = float(val)

def scalar_mul(v,k):
    
    res = Vec([0 for i in range(0,v.length())])
    for i in range(v.length()):
        res[i] = v[i]*k
    return res
def dot_product(v,u):
    assert  v.length() == u.length()
    res = 0 
    for i in range(v.length()):
        res += v[i]*u[i]
    return res
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
                    #print("newVec:")
                    #print(veclist[i])
    return veclist

def solve_homogenious(listlist):
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
        
            






class Vec:
    __add__ = add
    __getitem__ = getitem
    __setitem__ = setitem
    __rmul__ = scalar_mul
    __neg__ = neg
    def __init__(self,vec):
        '''
        constructor
        input: a vector list with int or float
        
        '''
        self.vec = []
        for item in vec:
            assert type(item)==int or type(item)==float
            self.vec.append(float(item))

    def length(self):
        return len(self.vec)
    
    def __sub__(self,other):
        return self+(-other)
    def __str__(self,sep = '           '):
        s1 = ""
        s2 = ""
        s3 = ""
        for i in range(self.length()):
            s1 += "---------"
            s2 += str(i)+": "+str(round(self[i],2)) + '   ' 
        return s1+"\n"+s2+"\n"+s1+"\n"
    def __repr__(self):
        return "<vector>\n"+self.__str__()
            
    def __mul__(self,other):
        if type(other) == Vec:
            return dot_product(self,other)
        else:
            return NotImplemented

    def copy(self):
        rawlist = [i for i in self.vec]
        return Vec(rawlist)

from random import *
u = Vec([1,2,3])
v = Vec([2,3,4])
lllist = [[1,2,3],[2,3,4]]
A = [[randint(0,100) for j in range(5)] for i in range(5)]
