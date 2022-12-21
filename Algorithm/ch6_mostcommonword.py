paragraph = "Bob hit a ball, the hit BALL flew far after it was hit"
banned = ["hit"]

para_dict = {}
paragraph = ''.join(list(map(lambda x: ' ' if not x.isalpha() else x, paragraph))).split()

for word in paragraph:
    if word not in banned and word.lower() not in banned:
        if word.lower() in para_dict.keys():
            para_dict[word.lower()] += 1
        else:
            para_dict[word.lower()] = 1

idx = list(para_dict.values()).index(max(para_dict.values()))

print(list(para_dict.keys())[idx])

