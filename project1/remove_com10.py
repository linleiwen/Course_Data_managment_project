# author: Leiwen Lin G48129884
## count_workds reference: http://blog.csdn.net/cxsydjn/article/details/70991846
## stopwords reference: Udemy Machine learning A-Z
def count_words(s, n):
    """Return the n most frequently occuring words in s."""
    w = {}
    sp = s.split()
    # TODO: Count the number of occurences of each word in s
    for i in sp:
        if i not in w:
            w[i] = 1
        else:
            w[i] += 1

    # TODO: Sort the occurences in descending order (alphabetically in case of ties)
    top = sorted(w.items(), key=lambda item:(-item[1], item[0]))
    top_n = top[:n]
    # TODO: Return the top n most frequent words.
    return top_n

import re
import fileinput
num = 10## we wanna remove 10 top common word

whole =''
file = open("holmes.txt", "r")
##file = fileinput.input()
for line in file:
    whole = whole + line
remove = count_words(whole, num) ##remove: list(tuple(words, counts))
file = open("holmes.txt", "r")  
newlist = [] ## get only the words list(words)
for each in remove:
    newlist.append(each[0])


for l in file:
    l = re.findall(r"[\w']+|[.,!?;]", l) #split function, but it also split punctuation individually
    l = [word for word in l if not word in set(newlist)] #remove words in newlist
    l = ' '.join(l)
    print(l)