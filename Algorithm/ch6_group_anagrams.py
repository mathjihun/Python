inputs = ["eat", "tea", "tan", "ate", "nat", "bat"]
word_dict = {}

for word in inputs:
    if ''.join(sorted(word)) in word_dict.keys():
        word_dict[''.join(sorted(word))].append(word)
    else:
        word_dict[''.join(sorted(word))] = [word]

print([v for v in word_dict.values()])
