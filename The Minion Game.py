def minion_game(string):
       
   vowel=['A','E','I','O','U']
   Kevin_sorce=0
   Stuar_sorce=0
   
   for subsring in(range(len(string))):
      if string[subsring] in vowel:
         Kevin_sorce +=len(string) -subsring
      else:
         Stuar_sorce +=len(string) -subsring
   
    
   if Kevin_sorce > Stuar_sorce:
         print(f"kevin {Kevin_sorce}")              
   elif Stuar_sorce > Kevin_sorce:
       print(f"stuart {Stuar_sorce}")
   else:
       print("Draw")    



   """  print(string)
    first_letter=string[0]
    print(first_letter)
    vwoel=['A','U','O','E','I']
    Kevin=[]
    Stuar=[]
    Kevin_sorce=0
    Stuar_sorce=0
    for substring in string:
        p1=input()
         """

        
       
     # your code goes here




""" 
if __name__ == '__main__':
    s = input()
    minion_game(s) """
s = input()
minion_game(s.upper())