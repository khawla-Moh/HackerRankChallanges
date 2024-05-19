import re
def order(sentence):
  # code here
  word=sentence.split()
  words=[]
  for i in range(1,10):
    for char in word:
      if str(i) in char:
        words.append(char)
  return ' '.join(words)     


print(order('thi3s is1 black'))