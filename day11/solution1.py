import copy
seats=[[*l.strip()] for l in open('input.txt', 'r').readlines()]

def adjacent_occupied(seats, i, j):
    adj=[row[max(0,j-1):min(len(seats),j+2)] for row in seats[max(0,i-1):min(len(seats),i+2)]]
    return sum(x.count('#') for x in adj) - (1 if seats[i][j]=='#' else 0)

def next_round(seats):
    seats_next=copy.deepcopy(seats)
    for i, row in enumerate(seats):
        for j, col in enumerate(row):
            if col=='L' and adjacent_occupied(seats,i,j)==0:
                seats_next[i][j]='#'
            elif  col=='#' and adjacent_occupied(seats,i,j)>=4:
                seats_next[i][j]='L'
    return seats==seats_next,seats_next

while True:
    unchanged,seats=next_round(seats)
    if unchanged:
        print(sum(x.count('#') for x in seats))
        break;