import collections
from collections import Counter
def runoff(voters):
    
    return voters


#//* INSERT VOTERS WITH CANDIDATE
def input_voters_candidate():
    voter={}
    voters={}
    number_of_voters=int(input("Total of voters  : "))
    for _ in range(number_of_voters):                            #* numbers of voters
        voter=input("name of voter : ")
        candidate=input("name of its  candiadte : ")
        candidates=[c.strip() for c in candidate.split(' ') ]    #* split candidates
        voters[voter]=candidates   
    return voters                                                #* each voter has several candidates
    

#//* INSERT VOTERS WITH CANDIDATE
def Count_first_candidate(voters):
    
    first_place={key:value[0] for key,value in voters.items() if value}     #* get first value(candidate) in item of voters dictionary
    print("first place: ",first_place)
    places=[item[0] for item in voters.values() if item]                    #* get first item{key(voter):values(candidates)} of voterd dictionary voters   

    count_first_place=collections.Counter(places)                           #* count first candidate ,How many  
    print("count first place : ",count_first_place)  
    return count_first_place

#//* TO GET THE HIGHEST CANDIDATE
def highest_candidate(first_place):
    max_key=max(first_place, key=first_place.get)             #* key (get max key assoicated with its value)
    max_value=first_place[max_key]                            #* value max value(candidate)
    
    return f"The candidate with the highest votes is '{max_key}' with {max_value} votes."
    
#//* TO GET THE LOWEST CANDIDATE
def lowest_candidate(first_place):
    min_value=min(first_place.values())                                         #* value (lowest candidate)
    min_key=[key for key,value in first_place.items() if value ==min_value]     #* key

    return f"The candidate with the lowest votes is '{min_key}' with {min_value} votes."

#//* TO GET THE LOWEST CANDIDATE
def tie_candidate(first_place):
    first_number=list(first_place.keys())[0]
    first_value=first_place[first_number]                 #* get first value of voters
    tie_value =all(value == first_value for value in first_place.values())                                 #value to check if all candidate is tie
    return tie_value





#//* GET winner candidate
def winner_candidate(voters,count_candidate):
    total_voters=len(voters)
    max_candidate=highest_candidate(count_candidate) 
    min_candidate=lowest_candidate(count_candidate)
    min_key = min_candidate.split("'")[1]  

    if tie_candidate(count_candidate):
       return None
   
    if count_candidate[max_candidate] > total_voters/2:
        return f"The winner candidate is: {max_candidate}"
     
    removed_min_key = {key: [item for item in value if item != min_key] for key, value in voters.items()}
    
    return winner_candidate(removed_min_key, Count_first_candidate(removed_min_key))


      
 

input_voters=input_voters_candidate()
count_candidate=Count_first_candidate(input_voters)
""" 
max_candidate=highest_candidate(count_candidate)
min_candidate=lowest_candidate(count_candidate)
tie_candidate=tie_candidate(count_candidate)
 """
winner=winner_candidate(input_voters,count_candidate)
if winner is None:
    print("all candidate is tie")
else:
    print(winner)    


""" 
print(max_candidate)
print(min_candidate)
print(tie_candidate)
print(winner) """

#print(runoff())

'''

    Use //! for alerts or warnings.
    Use //? for questions or notes.
    Use //* for highlighting important comments.
    Use //= for TODOs or tasks.

'''