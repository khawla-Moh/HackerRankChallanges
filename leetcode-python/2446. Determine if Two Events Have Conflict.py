""" 
class Solution(object):
    def haveConflict(self, event1, event2):
       

       return not (event1[0] > event2[1] or event1[1] < event2[0])


o=Solution()
event1 = ["01:15","02:00"]
event2 = ["02:00","03:00"]        
d=o.haveConflict(event1,event2)
print(d)


 """
class Solution(object):
    def haveConflict(self, event1, event2):
        if event1[0] >= event2[0] and event1[0] < event2[1]:
            return True
        if event1[1] > event2[0] and event1[1] <= event2[1]:
            return True
        if event2[0] >= event1[0] and event2[0] < event1[1]:
            return True
        if event2[1] > event1[0] and event2[1] <= event1[1]:
            return True
        #if the start or end time of one event is equal to the start or end time of the other event
        if event1[0] == event2[0] or event1[0] == event2[1] or event1[1] == event2[0] or event1[1] == event2[1]:
            return True
        return False


o=Solution()
event1 = ["01:15","02:00"]
event2 = ["02:00","03:00"]        
d=o.haveConflict(event1,event2)
print(d)

