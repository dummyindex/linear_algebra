from basic_utils import *
def add(u,v):
    '''
    input:2 vectors
    output: result of adding 2 vectors
    '''
    assert len(u) == len(v)
    return Vec([u[i]+v[i] for i in range (len(v))])
def neg(v):
    res = v.copy()
    for key in range(len(v)):
        res[key] = -v[key]
    return res 
def getitem(v,k):
    assert len(v) > k
    return v.vec[k]

def setitem(v,k,val):
    assert len(v) > k 
    v.vec[k] = float(val) if type(val)==int else val

def scalar_mul(v,k):
    
    res = Vec([0 for i in range(0,len(v))])
    for i in range(len(v)):
        res[i] = v[i]*k
    return res
def dot_product(v,u):
    assert  len(v) == len(v)
    res = 0 
    for i in range(len(v)):
        res += v[i]*u[i]
    return res

def vec_cmp(v1,v2):
    assert len(v1)==len(v2)
    diff = v1-v2
    return is_zero(diff*diff)

class Vec:
    __add__ = add
    __getitem__ = getitem
    __setitem__ = setitem
    __rmul__ = scalar_mul
    __neg__ = neg
    __eq__ = vec_cmp
    def __init__(self,vec):
        '''
        constructor
        input: a vector list with int or float
        
        '''
        self.vec = []
        for item in vec:
            assert type(item)==int or type(item)==float or type(item)==complex
            self.vec.append(float(item) if type(item)==int else item)

    def length(self):
        return (self*self)**(1/2)
    
    
    def __sub__(self,other):
        return self+(-other)
    def __str__(self,sep = '    '):
        s1 = ""
        s2 = ""
        s3 = ""
        for i in range(len(self)):
            s1 += "---------"
            s2 += str(i)+": "+str(round(self[i],2) if type(self[i])!=complex else self[i]) + sep 
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

    def __len__(self):
        return len(self.vec)
