logs = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero'  ]
digit_log = []
str_log = []

for x in logs:
    if x.split(' ')[1].isdigit():
        digit_log.append(x)
    else:
        str_log.append(x)

str_log.sort(key=lambda x: (x.split(' ')[1:], x.split(' ')[0]))

print(str_log + digit_log)