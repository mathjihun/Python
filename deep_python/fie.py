with open('경로', 'r') as f:       # with문은 file을 close할 필요가 없다.
    line = f.readline()
    # readlines()는 이스케이프 시퀀스 예를 들어 \n까지도 문자로 가져오고 줄 별로 모아서 하나의 리스트를 반환한다.
    # ex) [hi i am student\n, i love math\n]

    while line:
        print(line, end=' ##### ')
        line = f.readline()
      
with open('경로', 'w') as f:
  f.write('Niceman!\n')
  
with open('경로', 'a') as f:       # a는 기존 파일에 추가하는 것이다.
  f.write('Goodman!\n')

with open('경로', 'w') as f:       # writelines는 list를 파일에 쓰는 것이다.
  lst = ['Kim\n', 'Park\n', 'Cho\n']
  f.writelines(lst)
  
with open('경로', 'w') as f:       # 이렇게 하면 console로 나오는 것이 아니라 file로 기록이 된다.
  print('Test Contests1!', file=f)
  print('Test Contests2!', file=f)
  
