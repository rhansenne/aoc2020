seat_ids=set()
for seat in open('input.txt', 'r').readlines():
    row_low=0
    row_heigh=127
    for i in range(0,7):
        if seat[i]=='F':
            row_heigh=row_low+(row_heigh-row_low)//2
        else:
            row_low=row_low+(row_heigh-row_low)//2+1
    col_low=0
    col_heigh=7
    for i in range(7,10):
        if seat[i]=='L':
            col_heigh=col_low+(col_heigh-col_low)//2
        else:
            col_low=col_low+(col_heigh-col_low)//2+1
    seat_ids.add(row_low*8+col_low)     
print(max(seat_ids))