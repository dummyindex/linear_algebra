from subprocess import call
from source import *
from sentences import *
import  platform
MENU = {
    1:"solve matrix equation Ax = b",
    2:"solve homogenious equation Ax = 0(shortcut for 1)",
    3:"compute the inverse of a matrix",
    4:"row reduce a matrix",
    5:"Change of basis (Coordinate System change",
    -1:"exit"
}

def clear_console():
    if platform.system()=='Linux':
        call(["clear"])
    elif platform.system()=='Windows':
        call(["cls"])



def print_menu():
    for key in MENU:
        print(str(key)+":"+MENU[key])
def menu():
    print(S1)
    print_menu();
    while(1):
        try:
            idx = int(input(S2))
            if idx in MENU:
                break
            else:
                print(S4)
        except:
            print(S3)

    return idx

def string2numlist(s):
    temp = ""
    res = []
    for i in range(len(s)):
        if(s[i]==' '):
            temp = ""
        else:
            temp += s[i]
            if (i<len(s)-1 and s[i+1] == ' ') or (i==len(s)-1 and temp!=""):
                try:
                    x = int(temp)
                    res.append(x)
                except:
                    print(S14)
                    return None
    return res
            

def mat_input():
    row = None
    col = None
    while(1):
        flag = False
        s = input(S5)
        for idx in range(len(s)):
            if s[idx]==' ':
                flag = True
                break
        if flag:
            try:
                row = int(s[:idx])
                col = int(s[idx+1:])
                break
            except:
                print(S7)
        else:
            print(S6)
        
    print(S15)
    res = []
    for i in range(row):
        numlist = None
        while(1):
            s = input("row"+str(i)+" :\n")
            numlist = string2numlist(s)
            if numlist==None:
                print(S14)
            else:
                break
        res.append(numlist)
    print(S16)
    res = Mat(res)
    print(res)
    return res


def vec_input():
    numlist = None
    while numlist == None:
        s = input(S13)
        numlist = string2numlist(s)
    clear_console()
    print(S17)
    res = Vec(numlist)
    print(res)
    return res

def wait_for_viewing_answer():
    s = input("give any keyboard input to clear the console and back to the menu")
def solve_matrix_equation():
    clear_console()
    print(S9)
    A = mat_input()
    print(S10)
    b = vec_input()
    while len(b)!=A.rowLen:
        print(S19)
        b = vec_input()
    print(S8)
    print(S20)
    print(A)
    print(S21)
    print(b)
    ans = solve(A,b)
    if ans !=None:
        print(S22)
        print(ans)
    else:
        pass
    wait_for_viewing_answer()
    return 
    
def inv_mat_handler():
    mat = None
    while(1):
        print(S23)
        mat = mat_input()
        if mat.colLen!=mat.rowLen:
            clear_console()
            print(S24)
        else:
            break
    clear_console()
    print(S16)
    print(mat)
    inv = inv_mat(mat)
    if(inv==None):
        print(S25)
    else:
        print(S26)
        print(inv)
    wait_for_viewing_answer()

SERVICES = {
    #1:solve_matrix_equation,
    3:inv_mat_handler
}

def service_handler(idx):
    if idx in SERVICES.keys():
        SERVICES[idx]()
    else:
        print(S4)
        wait_for_viewing_answer()
    return


def run():
    clear_console()
    while(1):
        idx = menu()
        if idx==-1:
            return
        service_handler(idx)
        clear_console()
        

if "__main__"==__name__:
    run()
