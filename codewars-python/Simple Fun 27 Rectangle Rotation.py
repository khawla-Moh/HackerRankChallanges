import math


def rectangleRotation(a, b):
    result = 0
    for x in range(-(a+100), a+111):
        for y in range(-(b+100), b+111):
            x1=(x + y) / math.sqrt(2)
            y1 =(y-x) / math.sqrt(2)
            if x1 <a/2.0 and x1 >-a/2.0 and y1 <b/2.0 and y1 >-b/2.0:
                result += 1
              
    return result
           
    
    
print(rectangleRotation(6,4))    