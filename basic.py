"""
Python 기초

여러줄 주석
"""

# 한 줄 주석

# 모듈을 import 하는 방법
import random
from pprint import pprint
from random import randint

def print_func(param1):
    pprint(param1)
    param2 = 1 + 2
    param2 += param1

if __name__=="__main__":
    val1 = 10
    val2 = 'apple'
    val3 = None

    rnd = randint(0,9)

    print_func([val1,val2,val3,rnd]) # Array type
    print_func((val1 + rnd,val2,val3)) # Tuple type
    print_func({val1,val2,val3,rnd}) # Set type

