from math import atan2,degrees
#enter a lenght of ab,bc
AB=float(input())
BC=float(input())
#use atan2 to find angle from ab/bc  use degree to make result wirh degree
MBC=round(degrees(atan2(AB,BC))) 
print(str(MBC),chr(176),sep="")# use chr to find symbol ° sep to remove any space