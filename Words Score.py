def isVowel(letter):
    return letter in [ 'a', 'e', 'i', 'o', 'u' ,'y']



def sorce_word(sentence):
    sorce=0
    for word in sentence:
        vowel_num=0
        for letter in word:
            if isVowel(letter):
                vowel_num +=1            
        if vowel_num%2==0:
            sorce +=2
                    
        else:
             sorce+=1
                    
                    
    return sorce               
                        
n=int(input())
list_word=input().split()

print(sorce_word(list_word))


#another way to solve this challange:
def score_words(words:list) -> int:
    
    # create internal list of vowels
    VOWELS = ['a', 'e', 'i', 'o', 'u', 'y']
    
    # initialize score
    score = len(words)
    
    for w in words:
        # filter the vowels in the word
        vowels_in_w = list(filter(lambda x: x in VOWELS, w)) 
        
        # add +1 score for words with even nr. of vowels
        if len(vowels_in_w) % 2 == 0:
            score += 1 
    
    return score

    
# read inputs
n = int(input())
words= input().split()

# compute and print score
score = score_words(words)
print(score)