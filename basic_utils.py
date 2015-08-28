from random import randint

EPSILON = 0.01
def is_zero(n):
    if abs(n)<EPSILON:
        return True
def generate_listlist(n, m ,upper_limit = 10):
    return [[randint(0, upper_limit) for j in range(m)]for i in range(n)]
