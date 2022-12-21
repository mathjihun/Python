import collections

a = collections.defaultdict(int)
a['A']=5
a['B']=4
a['C'] += 1   # 이렇듯 defaultdict는 디폴트 값을 0으로 해서 없는 값에 대한 연산도 error를 발생하지 않도록 해준다.

print(a)

b = [1, 2, 3, 4, 5, 5, 5, 6, 6]
c = collections.Counter(b)    # 각 리스트의 원소들을 key로 하고 key들의 중복되는 개수를 value로 하는 딕셔너리를 리턴
print(c)
print(c.most_common(2))     # 가장 많이 쓰이는 2개의 요소를 추출한다.

# dictionary는 python 3.7 이후부터는 입력 순서를 보존하지만 그 전에는 보존하지 않았다.
# 이를 대비하려면 collections.OrderedDict(dictionary)를 해주어야 한다.