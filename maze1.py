import sys
class Node():
    def __init__(self,state,parent, action):
        self.state = state
        self.parent = parent
        self.action = action

class StackFrontier():
    def __init__(self):
        self.frontier = []
    
    def add(self, node):
        self.frontier.append(node)
    
    def empty(self):
        return len(self.frontier) == 0
    
    def contains_state(self,state):
        return any(node.state == state for node in self.frontier)
    
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            removed = self.frontier[-1]
            self.frontier = self.frontier[:-1]
            return removed
    
class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("Empty frontier")
        else:
            removed = self.frontier[0]
            self.frontier = self.frontier[1:]
            return removed  #this will be used a current node for searching

class Maze():
    
    def __init__(self, filename):
        #we need to read the file and find the height and width of the maze
        with open(filename) as f:
            contents = f.read()
        #checking for invalid entry
        if contents.count("A") !=1:
            raise Exception("invalide maze as it has multiple starting points")
        if contents.count("B") !=1:
            raise Exception("Invalid maze contains multiple end points")
        contents = contents.splitlines()
        #Find the height and width of the maze
        self.height = len(contents)
        self.width = max(len(x) for x in contents)

        #defining wall 
        self.wall = []
        for i in range(self.height):
            row =[]
            for j in range(self.width):
                try:
                    if contents[i][j] == 'A':
                        self.start = (i,j)
                        row.append(False)
                    elif contents[i][j] == 'B':
                        self.goal = (i,j)
                        row.append(False)
                    elif contents[i][j] ==" ":
                        row.append(False)
                    else:
                        row.append(True)               
                except IndexError:
                    row.append(False)
            
            self.wall.append(row)
        
        self.solution = None

    def fprint(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i,row in enumerate(self.wall):
            for j,col in enumerate(row):
                
                if col:
                    print("█", end = "")
                elif (i,j) == self.start:
                    print("A", end = "")
                elif (i,j) == self.goal:
                    print("B", end = "")
                elif solution is not None and (i,j) in solution:
                    print("*", end="")
                else :
                    print(" ",end ="")
            print()
        print()

    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1))
        ]

        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.wall[r][c]:
                result.append((action, (r, c)))
        return result

    #final ingredinet to solve the maze
    def solve(self):
        #Keep the track of number of states explored
        self.num_explored = 0
        #initialize the frontier to the starting point i.e A
        start = Node(state = self.start, parent = None, action = None)
        frontier = StackFrontier()
        frontier.add(start)
        #initialize an empty exlpored set
        self.explored = set()
        while True:
            if frontier.empty():
                raise Exception("No solution found")
            
            node = frontier.remove()
            self.num_explored +=1

            #check if we have reached the goal 
            if node.state == self.goal:
                action = []
                cells = []
                while node.parent is not None:
                    action.append(node.action)
                    cells.append(node.state)
                    node = node.parent
                action.reverse()
                cells.reverse()
                self.solution = (action, cells)
                return
            self.explored.add(node.state)
            #Add neighbour to the frontier
            for action,state in self.neighbors(node.state):
                if not frontier.contains_state(state) and state not in self.explored:
                    child = Node(state=state,action = action, parent = node)
                    frontier.add(child)
    
if len(sys.argv) != 2:
    sys.exit("Usage: python maze.py maze.txt")

m = Maze(sys.argv[1])
print("Maze:")
m.fprint()
print("Solving...")
m.solve()
print("States Explored:", m.num_explored)
print("Solution:")
m.fprint()


                    






                


