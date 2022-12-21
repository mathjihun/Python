# 예를 들어 숫자 1억개를 만들어 계산하는 프로그램의 경우 메모리에 1억개를 보관할 공간이 필요하다.
# 제너레이터를 이용하면 단순히 제너레이터만 생성해두고 필요할 때 언제든 숫자를 만들어낼 수 있다.
import sys


def get_natural_number():
    n = 0

    while True:
        n += 1
        yield n

g = get_natural_number()   # generator 생성
for _ in range(0, 100):
    print(next(g))


# 대표적인 generator가 range가 있다.


c1 = [n for n in range(1000000)]
c2 = range(1000000)

print("c1의 길이: {}, c2의 길이: {}".format(len(c1), len(c2)))
print("c1의 메모리 점유: {}, c2의 메모리 점유: {}".format(sys.getsizeof(c1), sys.getsizeof(c2)))


# generator를 이용하여 permutation 만들기


def gen_permute(seq):
    if not seq:
        yield seq
    else:
        for k in range(len(seq)):     # Choose kth element
            for x in gen_permute(seq[:k] + seq[k+1:]):    # x is a permutation of k-1 elements excluding seq[k:k+1]
                yield seq[k:k+1] + x


S = '123'
L = [1, 2, 3, 4]
P = gen_permute(S)
P2 = gen_permute(L)

while True:
    try:
        print(next(P), end=' ')
    except StopIteration:
        break

print()

while True:
    try:
        print(next(P2), end=' ')
    except StopIteration:
        break

print()