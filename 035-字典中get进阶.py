# 问：统计英文句子“Life is short, we learn Python.”中各字符出现的次数
sentence = 'Life is short, we learn Python.'
sentence = sentence.lower()
print(sentence)
counts = {}
for i in sentence:
    if i in counts:  # 之前写成了 if i in sentence: 导致字典中找不到 l 则输出：KeyError: 'l
        counts[i] = counts[i] + 1
    else:
        counts[i] = 1
print(counts)
# {'l': 2, 'i': 2, 'f': 1, 'e': 3, ' ': 5, 's': 2, 'h': 2, 'o': 2, 'r': 2, 't': 2, ',': 1, 'w': 1, 'a': 1, 'n': 2, 'p': 1, 'y': 1, '.': 1}

# 用 get() 简化运算操作
sentence1 = 'World is so big, I would like to travel.'
sentence1 = sentence1.lower()
counts1 = {}
for n in sentence1:
    counts1[n] = counts1.get(n, 0) + 1   # n是键，而get()返回的是值
print(counts1)
