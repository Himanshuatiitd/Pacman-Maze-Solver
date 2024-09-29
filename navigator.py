from maze import *
from exception import *
from stack import *
class PacMan:
    def __init__(self, grid : Maze) -> None:
        ## DO NOT MODIFY THIS FUNCTION
        self.navigator_maze = grid.grid_representation
    def isvalid(self,x,y):
        if x<0 or y<0 or x>=len(self.navigator_maze) or y>=len(self.navigator_maze[0]) :
            return False
        if self.navigator_maze[x][y]==1:
            return False
        return True
            
    def find_path(self, start : tuple, end : tuple) -> list:
        # IMPLEMENT FUNCTION HERE'
        m=len(self.navigator_maze)
        n=len(self.navigator_maze[0])
        if self.isvalid(start[0],start[1])==False or self.isvalid(end[0],end[1])==False or self.navigator_maze[start[0]][start[1]]==1 or self.navigator_maze[end[0]][end[1]]==1 or n==0 or m==0:
            raise PathNotFoundException
        lis=Stack()
        lis.push(start)
        notpossible=[]
        visited=[]
        m=len(self.navigator_maze)
        n=len(self.navigator_maze[0])
        for row in range(m):
            grid_row = []
            for column in range(n):
                grid_row.append(False)
            notpossible.append(grid_row)
            visited.append(grid_row)
        visited[start[0]][start[1]]=True
        if(start==end):
            # print(lis.li)
            return lis.li
        else:
            while True:
                if(lis.isempty()):
                    break
                elif(lis.top()==end):
                    # print(lis.li)
                    return lis.li
                elif self.isvalid(lis.top()[0]-1,lis.top()[1]) and notpossible[lis.top()[0]-1][lis.top()[1]]==False and visited[lis.top()[0]-1][lis.top()[1]]==False:
                    visited[lis.top()[0]-1][lis.top()[1]]=True
                    lis.push((lis.top()[0]-1,lis.top()[1]))
                elif self.isvalid(lis.top()[0],lis.top()[1]-1) and notpossible[lis.top()[0]][lis.top()[1]-1]==False and visited[lis.top()[0]][lis.top()[1]-1]==False:
                    visited[lis.top()[0]][lis.top()[1]-1]=True
                    lis.push((lis.top()[0],lis.top()[1]-1))
                elif self.isvalid(lis.top()[0]+1,lis.top()[1]) and notpossible[lis.top()[0]+1][lis.top()[1]]==False and visited[lis.top()[0]+1][lis.top()[1]]==False:
                    visited[lis.top()[0]+1][lis.top()[1]]=True
                    lis.push((lis.top()[0]+1,lis.top()[1]))
                elif self.isvalid(lis.top()[0],lis.top()[1]+1) and notpossible[lis.top()[0]][lis.top()[1]+1]==False and visited[lis.top()[0]][lis.top()[1]+1]==False:
                    visited[lis.top()[0]][lis.top()[1]+1]=True
                    lis.push((lis.top()[0],lis.top()[1]+1))
                else:
                    visited[lis.top()[0]][lis.top()[1]]=False
                    notpossible[lis.top()[0]][lis.top()[1]]=True
                    lis.pop()
        raise PathNotFoundException