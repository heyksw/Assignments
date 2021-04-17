# 12161540 김상우
# bin_ext_euclid 완성하기 과제
"""
polynomial representation

For example, f(z) = z^5 + z^2 + 1 <=> f = 0b100101

"""

# z의 몇승 꼴로 문자열 출력하는 함수
def get_poly_str(f):
    polys = []
    for i, v in enumerate(reversed(bin(f)[2:])):
        if v == '1':
            polys.insert(0, (i, v))
    return " + ".join(["z^{}".format(i) for i, v in polys])

"""
Multiplication for binary polynomials

the case of GF(2^8) and the number of bits of n is 9-bits. (e.g. AES)

"""


def carry(a):   # 캐리 탐지 함수
    if a & 0x100:
        return True
    else:
        return False

# Multiplication for binary polynomials A*B mod(n)
def bin_mul(a, b, n):   # A,B,C 단계 나눈 것
    # buf = 0  # pre-computation for mod operation
    # for i in reversed(range(9)):  # from 8 down to 0
    #     mask = 1 << i
    #     if n & mask is not 0:
    #         buf = n & ((mask << 1) - 1)
    #         break
    buf = n & 0xff  # pre-computation for mod operation (simple)


    # part A : shift pre-computation table. (중간 단계 표 작성)
    f = [0] * 8  # pre-computation table for `a`
    f[0] = a
    for i in range(1, 8):
        f[i] = f[i-1] << 1
        if carry(f[i]):
            f[i] &= 0xff
            f[i] ^= buf

    # part B : 1이 있는 자리 수 파악
    res = 0
    for i in range(8):
        mask = 1 << i   # masking
        if b & mask != 0:
            res ^= f[i]     # part C : 최종 XOR 계산

    return res


m = 32  # 32bit
"""
degree of binary polynomials
"""

# 차수 구하기
def deg(bp):
    for i in reversed(range(m)):  # from m-1 down to 0
        if (bp & (1 << i)) != 0:
            return i
    return 0


"""
Extended Euclidean Algorithm for binary polynomials(Iterative version)

return (d, g, h) such that a * g + b * h = d = gcd(a, b)
loop invariant :
a * g_1 + b * h_1 = u
a * g_2 + b * h_2 = v
"""

# 12161540 김상우
from exponentiation import exp
# d, g, h = bin_ext_euclid(128, 0b100011011) 이런식으로 들어올 거임.
def bin_ext_euclid(a, b):
    # todo

    # 1
    u, v = a, b

    #2
    g1, g2 = 1, 0
    h1, h2 = 0, 1

    #3
    while u != 0:
        # 3.1
        j = deg(u)-deg(v)
        # 3.2
        if j < 0 :
            u, v = v, u
            g1, g2 = g2, g1
            h1, h2 = h2, h1
            j = -j
        # 3.3
        u ^= v << j
        # 3.4
        g1 ^= g2 << j
        h1 ^= h2 << j
    # 4
    d = v
    g = g2
    h = h2

    # 5
    return d, g, h


"""
Inversion for binary polynomials using extended euclidean algorithm

returns a^-1 mod n. (n should be irreducible.)
"""


def bin_inv(a, n):
    d, g, h = bin_ext_euclid(a, n)
    return g


if __name__ == "__main__":
    '''
    print("deg(10) = {}".format(deg(10)))
    # f(z) = z^8 + z^4 + z^3 + z + 1. f(z) is irreducible.
    print(get_poly_str(0b100011011))
    # the example on 4th slide
    print(get_poly_str(bin_mul(0b01010111, 0b10000011, 0b100011011)))
    # Inversion test
    d, g, h = bin_ext_euclid(128, 0b100011011)
    print(d, "|", get_poly_str(g), "|", get_poly_str(h))
    print(get_poly_str(bin_inv(128, 0b100011011)))
    print(get_poly_str(bin_mul(128, 131, 0b100011011)))
    

    u = 0
    v = 1
    u ^= v
    x = 0b1
    print(u)
    print('log1')
    print(x<<1)
    '''

    d, g, h = bin_ext_euclid(128, 0b100011011)
    print("input:", 128, ":", d, "|", get_poly_str(g), "|", get_poly_str(h))

    d, g, h = bin_ext_euclid(126, 0b100011011)
    print("input:", 126, ":", d, "|", get_poly_str(g), "|", get_poly_str(h))


    d, g, h = bin_ext_euclid(7, 0b100011011)
    print("input:", 7, ":", d, "|", get_poly_str(g), "|", get_poly_str(h))
    # print(bin_mul(0b01010111, 0b10000011, 0b100011011))
    # print(deg(0b00111010))
    print('terminate')