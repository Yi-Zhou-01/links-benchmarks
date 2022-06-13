from itertools import repeat
from math import sqrt
from multiprocessing import Pool
from sys import argv


def eval_A(i, j):
    ij = i + j
    return ij * (ij + 1) // 2 + i + 1


def A_sum(u, i):
    return sum(u_j / eval_A(i, j) for j, u_j in enumerate(u))


def At_sum(u, i):
    return sum(u_j / eval_A(j, i) for j, u_j in enumerate(u))


def multiply_AtAv(u):
    r = range(len(u))

    tmp = pool.starmap(
        A_sum,
        zip(repeat(u), r)
    )
    return pool.starmap(
        At_sum,
        zip(repeat(tmp), r)
    )


def main():
    n = 50
    u = [1] * n

    for _ in range(10):
        v = multiply_AtAv(u)
        u = multiply_AtAv(v)

    # print("______v_______")
    # print(v)
    # print("_______u_________")
    # print(u)

    vBv = vv = 0

    for ue, ve in zip(u, v):
        vBv += ue * ve
        vv  += ve * ve

    result = sqrt(vBv/vv)
    print("{0:.9f}".format(result))


if __name__ == '__main__':
    with Pool(processes=4) as pool:
        main()
    
# n = 1000: 1.274224148
# n = 100 : 1.274219991
# n = 50  : 1.274193837