import numpy as np
#초기 설정
percept_grid = [['' for col in range(6)] for row in range(6)]
wumpus_grid = [['' for col in range(6)] for row in range(6)]
user_grid = [['' for col in range(6)] for row in range(6)]

wumpus_grid[2][2] = 'Gold'
percept_grid[2][2] = percept_grid[2][2] + 'glitter'
wumpus_grid[2][3] = 'Pitch'
percept_grid[2][3] = percept_grid[2][3] + ' breeze'
wumpus_grid[3][3] = 'Wumpus'
percept_grid[3][3] = percept_grid[3][3] + ' stench'

for i in range(6):
    for j in range(6):
        if i == 0 or i == 5:
            wumpus_grid[i][j] = 'Wall'
        else:
            if j == 0 or j == 5:
                wumpus_grid[i][j] = 'Wall'

for i in range(1,4):
    for j in range(1,4):
        if wumpus_grid[i][j] == 'Gold' and wumpus_grid[i+1][j] != 'W':
            percept_grid[i+1][j] = percept_grid[i+1][j] + ' glitter'
        if wumpus_grid[i][j] == 'Gold' and wumpus_grid[i][j-1] != 'W':
            percept_grid[i][j-1] = percept_grid[i][j-1] + ' glitter'
        if wumpus_grid[i][j] == 'Gold' and wumpus_grid[i][j+1] != 'W':
            percept_grid[i][j+1] = percept_grid[i][j+1] + ' glitter'
        if wumpus_grid[i][j] == 'Gold' and wumpus_grid[i-1][j] != 'W':
            percept_grid[i-1][j] = percept_grid[i-1][j] + ' glitter'

        if wumpus_grid[i][j] == 'Pitch' and wumpus_grid[i+1][j] != 'W':
            percept_grid[i+1][j] = percept_grid[i+1][j] + ' breeze'
        if wumpus_grid[i][j] == 'Pitch' and wumpus_grid[i][j-1] != 'W':
            percept_grid[i][j-1] = percept_grid[i][j-1] + ' breeze'
        if wumpus_grid[i][j] == 'Pitch' and wumpus_grid[i][j+1] != 'W':
            percept_grid[i][j+1] = percept_grid[i][j+1] + ' breeze'
        if wumpus_grid[i][j] == 'Pitch' and wumpus_grid[i-1][j] != 'W':
            percept_grid[i-1][j] = percept_grid[i-1][j] + ' breeze'

        if wumpus_grid[i][j] == 'Wumpus' and wumpus_grid[i+1][j] != 'W':
            percept_grid[i+1][j] = percept_grid[i+1][j] + ' stench'
        if wumpus_grid[i][j] == 'Wumpus' and wumpus_grid[i][j-1] != 'W':
            percept_grid[i][j-1] = percept_grid[i][j-1] + ' stench'
        if wumpus_grid[i][j] == 'Wumpus' and wumpus_grid[i][j+1] != 'W':
            percept_grid[i][j+1] = percept_grid[i][j+1] + ' stench'
        if wumpus_grid[i][j] == 'Wumpus' and wumpus_grid[i-1][j] != 'W':
            percept_grid[i-1][j] = percept_grid[i-1][j] + ' stench'

for i in range(6):
        print("   ",wumpus_grid[i],"   ")

print()
for i in range(6):
        print(percept_grid[i])

pos_Code = percept_grid[2][2].find('stench')
print(pos_Code)







#존재여부는 새로운 grid2에 저장하면 어떨까???
