class Node():
    def __init__(self,state,parent,action,hurestic):
        self.state = state
        self.parent = parent
        self.action = action 
        self.hurestic = hurestic

# Now we will create Greedy Best for search class
class Greedy_b_s():

    def __init__(self):
        self.frontier = []
    
    def add(self,node):
        self.frontier.append(node)

    def empty(self):
        return len(self.frontier) == 0
    
    def contains_state(self,state):
        return any(node.state == state for node in self.frontier)
    
    def remove(self):
        removed = self.frontier[0]
        self.frontier = self.frontier[1:]
    
    def sortByhurestic(self):

        for i in range(len(self.frontier)-1):
            if a[i].hurestic > a[i+1].hurestic:
                temp = a[i]
                a[i] = a[i+1]
                a[i+1] = temp
    

a = [40,30,10,8]
for i in range(len(a)-1):
    for j in range(len(a)-1):
        if a[i]>a[j]:
            temp = a[i]
            a[i] = a[j]
            a[j] = temp
print(a)
            
        
