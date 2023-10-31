import copy
seats=[[*l.strip()] for l in open('input.txt', 'r').readlines()]

def adjacent_occupied(seats, i, j):
    occ=0
    for x,y in [(-1,-1),(-1,0),(0,-1),(1,0),(0,1),(1,1),(1,-1),(-1,1)]:
        adj_i=i
        adj_j=j
        while True:
            adj_i+=x
            adj_j+=y
            if 0 <= adj_i < len(seats) and 0 <= adj_j < len(seats[0]) and seats[adj_i][adj_j] != 'L':
                if seats[adj_i][adj_j] == '#':
                    occ+=1
                    break
            else:
                break
    return occ

def next_round(seats):
    seats_next=copy.deepcopy(seats)
    for i, row in enumerate(seats):
        for j, col in enumerate(row):
            if col=='L' and adjacent_occupied(seats,i,j)==0:
                seats_next[i][j]='#'
            elif  col=='#' and adjacent_occupied(seats,i,j)>=5:
                seats_next[i][j]='L'
    return seats==seats_next,seats_next

while True:
    unchanged,seats=next_round(seats)
    if unchanged:
        print(sum(x.count('#') for x in seats))
        break;