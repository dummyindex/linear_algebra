from vec import Vec
from basic_utils import *
def getitem(mat , r):
    return mat.mat[r]
def mat_cmp(m1,m2):
    if m2==None:
        return False
    if not (m1.colLen==m2.colLen and m1.rowLen==m2.rowLen):
        return False

    for i in range(m1.rowLen):
        for j in range(m2.colLen):
            if not is_zero(m1[i][j]-m2[i][j]):
                print(m1[i][j]-m2[i][j])
                return False
    return True

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
    assert mat.colLen == len(vec)
    res = []
    for r in range(mat.rowLen):
        acc = 0
        for c in range(len(vec)):
            acc += mat[r][c] * vec[c]
        res.append(acc)
    return Vec(res)

def mat_scalar_mul(mat, k):
    res = Mat([[mat[i][j] for j in range(mat.colLen)] for i in range(mat.rowLen)])
    for i in range(mat.rowLen):
        for j in range(mat.colLen):
            res[i][j] *= k
    return res
            
class Mat:
    __getitem__ = getitem
    __cmp__ = mat_cmp
    __eq__ = mat_cmp
    def __init__(self, listlist):
        assert len(listlist)>0 and len(listlist[0])>0
        self.rowLen = len(listlist)
        self.colLen = len(listlist[0])
        for i in range(len(listlist)):
            for j in range(len(listlist[0])):
                assert type(listlist[i][j])== int or type(listlist[i][j])==float or type(listlist[i][j]) == complex
        self.mat = [[float(listlist[i][j]) if type(listlist[i][j])!=complex else complex(listlist[i][j]) for j in range(len(listlist[i]))]
                        for i in range(len(listlist))]
        
    def __str__(self):
        res = ""
        row = 0
        for i in self.mat:
            res+="row"+str(row)
            res += str(Vec(i))+"\n"
            row+=1
        return res

    __rmul__ = mat_scalar_mul
    def __mul__(self,other):
        if type(other) == Mat:
            return mat_mat_mul(self,other)
        elif type(other) == Vec:
            return mat_vec_mul(self, other)
        else:
            return NotImplemented


    def __repr__(self):
        res = "<Matrix>\n"+self.__str__()
        return res
    
    def isRow(self, x):
        return 0<=x and x<self.rowLen
    def isCol(self, x):
        return 0<=x and x<self.colLen
    def sub_mat(self, r1, r2, c1, c2):
        assert self.isRow(r1) and self.isRow(r2) and self.isCol(c1) and self.isCol(c2)
        res = []
        for r in range(r1,r2+1):
            res.append([])
            for c in range(c1,c2+1):
                res[r].append(self.mat[r][c])
        return Mat(res)
    
    def right_half_mat(self):
        return self.sub_mat(0,self.rowLen-1, int(self.colLen/2), self.colLen-1)
    

    def copy(self):
        temp = [[self[i][j] for j in range(self.colLen)] for i in range(self.rowLen)]
        return Mat(temp)
    def remove_row(self,r):
        self.mat.pop(r)
        self.rowLen-=1
    
    def remove_col(self,c):
        for colvec in self.mat:
            colvec.pop(c)
        self.colLen-=1
    def det(self):
        '''
        output:the determinant of the square matrix
        super inefficient! with naive implementation of definition
        of determinants by cofactors.
        time complexity: O( (n!)^3), this silly implementation can
        be optimized to O(n!)
        '''
        assert self.colLen==self.rowLen
        
        if self.colLen==1 and self.rowLen==1:
            return self[0][0]
        
        if self.colLen>=2:
            res = 0
            for r in range(0,self.rowLen):
                if(self[r][0]==0):
                    continue
                foo_mat = self.copy()
                foo_mat.remove_col(0)
                foo_mat.remove_row(r)
                #print("foomat:\n"+str(foo_mat))
                res+=(-1)**r*self[r][0]*foo_mat.det()
            return res
        else:
            res = 0 
            for c in range(0,self.colLen):
                if(self[r][0]==0):
                    continue
                foo_mat = self.copy()
                foo_mat.remove_col(c)
                foo_mat.remove_row(0)
                res+=(-1)**c*self[0][c]*foo_mat.det()
            return res

