def main():

    grid = [[' ',' ',' '],
            [' ',' ',' '],
            [' ',' ',' '],
            ['-','-','-']]
    
    wrong_dic={0:[2,1,'o'],1:[1,1,'o'],2:[0,1,'o'],3:[1,0,'/'],4:[1,2,'\\']}
    wronglist=[]
    for i in range(1):
        (rows, cols,symbols)=wrong_dic[i]
        change_grid(rows, cols,symbols,grid)
    
    printPretty(grid)

def printPretty(g):
    rows = len(g)
    cols = len(g[0])
    for r in range(rows):
        for c in range (cols):
            print(g[r][c],end="")
        print()

def change_grid(x,y,z,grid):
    grid[x][y]=z

main()
