facing=0 # 0=east, 1=south, 2=west, 3=north
x=y=0
for l in open('input.txt', 'r').readlines():
    match l[0]:
        case 'E':
            x+=int(l[1:])
        case 'S':
            y-=int(l[1:])
        case 'W':
            x-=int(l[1:])
        case 'N':
            y+=int(l[1:])
        case 'L':
            match int(l[1:]):
                case 90:
                    facing=(facing+3)%4
                case 180:
                    facing=(facing+2)%4
                case 270:
                    facing=(facing+1)%4
        case 'R':
            match int(l[1:]):
                case 90:
                    facing=(facing+1)%4
                case 180:
                    facing=(facing+2)%4
                case 270:
                    facing=(facing+3)%4
        case 'F':
            match facing:
                case 0:
                    x+=int(l[1:])
                case 1:
                    y-=int(l[1:])
                case 2:
                    x-=int(l[1:])
                case 3:
                    y+=int(l[1:])
print(abs(x)+abs(y))                                                        