# use the Counter module
from collections import Counter
# use the regex module
import re

def top_3_words(text):
    # count the input, pass through a regex and lowercase it
    c = Counter(re.findall(r"[a-z']+", re.sub(r" '+ ", " ", text.lower())))
    # return the `most common` 3 items
    return [w for w,_ in c.most_common(3)]




def top_3_words(text):
    # loop through each character in the string
    for c in text:
        # if it's not alphanumeric or an apostrophe
        if not (c.isalpha() or c=="'"):
            # replace with a space
            text = text.replace(c,' ')
    # create some `list` variables
    words,counts,out = [],[],[]

    # loop through the words in the text
    for word in list(filter(None,text.lower().split())):
        # if in all, then continue
        if all([not c.isalpha() for c in word]):
            continue
        # if the word is in the words list
        if word in words:
            # increment the count
            counts[words.index(word)] += 1
        else:
            # otherwise create a new entry
            words.append(word); counts.append(0)

    # loop while bigger than 0 and less than 3
    while len(words)>0 and len(out)<3:
        # append the counts
        out.append(words.pop(counts.index(max(counts))).lower())
        counts.remove(max(counts))
    # return the counts
    return out

def top_3_words(text):
    wrds = {}
    for p in r'!"#$%&()*+,./:;<=>?@[\]^_`{|}~-':
        text = text.replace(p, ' ')
    for w in text.lower().split():
        if w.replace("'", '') != '':
            wrds[w] = wrds.get(w, 0) + 1
    return [y[0] for y in sorted(wrds.items(), key=lambda x: x[1], reverse=True)[:3]]




""" import re


def top_3_words(text):
    new_dic={}
    text= ''.join([word.lower() for word in text if word.isalpha() or word ==' ' or word == "'"])
    for word in text:
        if word.replace("'",'').isalpha():
            if word  in text:
                new_dic[word] +=1
            else:
                new_dic[word] =1      
    return [i for i,j in sorted(new_dic.items(),key=lambda new_dic:new_dic[1],reverse=True)][:3]  





 """













n="In a village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance in the lance-rack, an old buckler, a lean hack, and a greyhound forcoursing. An olla of rather more beef than mutton, a salad on mostnights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extraon Sundays, made away with three-quarters of his income."
print(top_3_words(n))
""" t={}
    m=[]
    counter=0
    text=text.split()
    for i in text:
        if i in t:
           t[i] +=1 
        else:
            t[i]=1
        max1=max(t,key=t.get)
        m.append(max1)
        t.pop(max1)
        max2=max(t,key=t.get)
        m.append(max2)
        t.pop(max2)
        max3=max(t,key=t.get)
            
    print(f'{t}, {counter}',max1,max2,max3)            
    """     


""" 
    counts={}
    rep=[]
    text1=sorted(text.split(' '))
    for i in text1:
        if i in counts:
            counts[i] +=1
        else:
            counts[i]=1
    repeated_words = [word for word, count in counts.items() if count > 1]
    
    
    return 
repeated_words

"""