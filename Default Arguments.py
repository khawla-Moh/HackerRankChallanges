
class even_stream(object):
    def __init__(self) :
        self.cuurent=0
    def get_next(self):
        to_return = self.cuurent
        self.cuurent += 2
        return to_return
class odd_stream(object):
    def __init__(self) :
        self.cuurent=1
    def get_next(self):
        to_return = self.cuurent
        self.cuurent += 2
        return to_return
def print_from_stream(n, stream=None):
    if stream is None:
        stream = even_stream()
    for _ in range(n):
        print(stream.get_next())
            
for _ in range(int(input())):
    stream_name,n=input().split()
    n=int(n)
    if stream_name=='even':

        print_stream(n)
        
    else:
        print_stream(n,odd_stream())
        
          