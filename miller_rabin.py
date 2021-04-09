"""
miller-rabin prime test

Test if n is prime with error probability less than 2^(−𝑠).

"""

import random
from exponentiation import exp

Prime = 0
Composite = 1


def miller_rabin(n, s):
    if n == 2:
        return Prime
    elif n % 2 == 0:
        return Composite

    for _ in range(s):
        a = random.randint(1, n-1)
        if test(a, n) == True:
            return Composite

    return Prime


def int_to_bin(num):
    return list(bin(num))[2:]


# 12161540 김상우
def test(a, n):
    # 1. 정수 k,q를 찾는다.
    while True:
        k = 1
        q_remain = (n-1) % (exp(2, k, n))
        if q_remain == 0:
            q = (n-1) // (exp(2, k, n))
            break
        k += 1

    # 2. 1 < a < n-1 임의 정수 a 선택
    # -> 인수로 이미 a를 받았다.

    # 3. 첫 번쨰 조건
    if exp(a, q, n) % n == 1:
        return False

    # 4. 두 번째 조건
    for j in range(0,k):
        x = exp(2, j, n)
        if exp(a, x * q, n) % n == n-1:
            return False

    return True


if __name__ == "__main__":

    primes = [
        39402006196394479212279040100143613805079739270465446667948293404245721771496870329047266088258938001861606973112319,
        6864797660130609714981900799081393217269435300143305409394463459185543183397656052122559640661454554977296311391480858037121987999716643812574028291115057151,
        443372888629441, 561
    ]

    for p in primes:
        result = miller_rabin(p, 20)
        if result == Prime:
            print("Prime")
        elif result == Composite:
            print("Composite")
        else:
            print("Undefined")
