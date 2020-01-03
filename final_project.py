#coding:gbk
'''
�������ߣ���˳
'''


import codecs
import jieba.posseg as pseg
import jieba                #������صĿ�

names = {}
relationships = {}
lineNames = []
import jieba
excludes = {}
txt = open("���������Ľֵ�.txt", "r", encoding='utf-8').read()
words  = jieba.lcut(txt)
counts = {}
for word in words:
    if len(word) == 1:
        continue
    else:
        counts[word] = counts.get(word,0) + 1
for word in excludes:
    del(counts[word])
items = list(counts.items())
items.sort(key=lambda x:x[1], reverse=True)
for i in range(200000):
    word, count = items[i]
    print ("{0:<10}{1:>5}".format(word, count))
#���д�Ƶͳ�Ʋ���

jieba.load_userdict("names.txt")
with codecs.open("���������Ľֵ� .txt", 'r', 'utf-8') as f:
    for line in f.readlines():
        poss = pseg.cut(line)  # �ִʣ����ش���
        lineNames.append([])  # Ϊ��������һ�������б�
        for w in poss:
            if w.flag != 'nr' or len(w.word) < 2:
                continue
            lineNames[-1].append(w.word)
            if names.get(w.word) is None:
                names[w.word] = 0
                relationships[w.word] = {}
            names[w.word] += 1

            # ���������ִ���ͳ�ƽ��

for line in lineNames:
    for name1 in line:
        for name2 in line:
            if name1 == name2:
                continue
            if relationships[name1].get(name2) is None:
                relationships[name1][name2] = 1
            else:
                relationships[name1][name2] = relationships[name1][name2] + 1

#����ÿһ�ε������ϵ

with codecs.open("People_node.txt", "w", "utf8") as f:
    f.write("ID Label Weight\r\n")
    for name, times in names.items():
        if times > 10:
            f.write(name + " " + name + " " + str(times) + "\r\n")
# дcsv�ļ� ��������ͼʹ�ã�����Ȩ�ؽ��


with codecs.open("People_edge.txt", "w", "utf8") as f:
    f.write("Source Target Weight\r\n")
    for name, edges in relationships.items():
        for v, w in edges.items():
            if w > 10:
                f.write(name + " " + v + " " + str(w) + "\r\n")
                
#����߹�ϵ�Ĳ��� ���ڵ���gelphi
                




