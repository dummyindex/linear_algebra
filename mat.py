
from vec import Vec
def getitem(mat , r):
    return mat.mat[r]

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
            
class Mat:
    __getitem__ = getitem
    def __init__(self, listlist):
        assert len(listlist)>0 and len(listlist[0])>0
        self.rowLen = len(listlist)
        self.colLen = len(listlist[0])
        for i in range(len(listlist)):
            for j in range(len(listlist[0])):
                assert type(listlist[i][j])== int or type(listlist[i][j])==float or type(listlist[i][j]) == complex
        self.mat = [[listlist[i][j] for j in range(len(listlist[i]))]
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
    
