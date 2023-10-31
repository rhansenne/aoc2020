x=y=0
wx=10
wy=1
for l in open('input.txt', 'r').readlines():
    match l[0]:
        case 'E':
            wx+=int(l[1:])
        case 'S':
            wy-=int(l[1:])
        case 'W':
            wx-=int(l[1:])
        case 'N':
            wy+=int(l[1:])
        case 'L':
            match int(l[1:]):
                case 90:
                    tx=wx
                    wx=-wy
                    wy=tx
                case 180:
                    wx=-wx
                    wy=-wy
                case 270:
                    ty=wy
                    wy=-wx
                    wx=ty
        case 'R':
            match int(l[1:]):
                case 90:
                    ty=wy
                    wy=-wx
                    wx=ty
                case 180:
                    wx=-wx
                    wy=-wy
                case 270:
                    tx=wx
                    wx=-wy
                    wy=tx
        case 'F':
            x+=int(l[1:])*wx
            y+=int(l[1:])*wy
print(abs(x)+abs(y))                                                        