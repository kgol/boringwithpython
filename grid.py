from listtostr import listtostr
grid = [['.', '.', '.', '.', '.', '.'],['.', 'O', 'O', '.', '.', '.'],['O', 'O', 'O', 'O', '.', '.'],['O', 'O', 'O', 'O', 'O', '.'],['.', 'O', 'O', 'O', 'O', 'O'],['O', 'O', 'O', 'O', 'O', '.'],['O', 'O', 'O', 'O', '.', '.'],['.', 'O', 'O', '.', '.', '.'],['.', '.', '.', '.', '.', '.']]
x=[]
for k in range(len(grid[0])):
    for i in range(len(grid)):
        x=[grid[i][k]]
        m=listtostr(x)
        print(m)
        #print(grid[i][k])
        ##niedziala tak jak trzeba :(((






