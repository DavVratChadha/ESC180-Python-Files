import collections

res_d = {}

l =[['the', 'reality', 'that', 'i', 'had', 'known', 'no', 'longer', 'existed'], ['it', 'sufficed', 'that', 'mme'], ['swann', 'did', 'not', 'appear', 'in', 'the', 'same', 'attire', 'and', 'at', 'the', 'same', 'moment', 'for', 'the', 'whole', 'avenue', 'to', 'be', 'altered']]

for sentence in l:
    for word in sentence:
        res_d = dict.fromkeys(sentence,dict(collections.Counter(list(filter(lambda a: a != word, sentence)))))

print(res_d)