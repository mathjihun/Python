with open('../', 'r') as f:      # 이러면 file을 close할 필요가 없다.
  line = f.readline()
  
  while line:
    print(line, end=' ##### ')
    line = f.readline()
