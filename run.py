from subprocess import call
from source import *
S1 = "Master! Here's what I can do for you."
S2 = "\nPlease give me an index(a numeric value).\n"
S3 = "It seems your input is not a number"
S4 = "Sorry, the service you ordered is not available."
S5 = "Please give the dimensions of the matrix, separate by space\n"
S6 = "format of the dimension is wrong\n"
S7 = "Please give me numeric values\n"
S8 = "Now we are going to solve the equation.......\n"
S9 = "Give A please.\n"
S10 = "Give b please.\n"
S11 = "Give the length of the vector please"
S12 = "Please give me a numeric value\n"

MENU = {
    1:"solve matrix equation Ax = b",
    2:"solve homogenious equation Ax = 0(shortcut for 1)",
    3:"compute the inverse of a matrix",
    -1:"exit"
}



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
def matrix_input():
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
    print(S8)

def vec_input():
    length = None
    while(1):
        try:
            length = int(input(S11))
            break
        except:
            print(S12)
    print(S13)
    temp = []
    for i in range(length):
        x = None
        while(1):
            try:
                x = input(S14)
            else:
                print(S12)
        temp.append(x)

        


def solve_matrix_equation():
    call(["clear"])
    print(S9)
    A = matrix_input()
    print(S10)
    b = vector_input()

def service_handler(idx):
    if idx==1:
        solve_matrix_equation()


def run():
    while(1):
        idx = menu()
        if idx==-1:
            return
        service_handler(idx)
        call(["clear"])
        

if "__main__"==__name__:
    run()
