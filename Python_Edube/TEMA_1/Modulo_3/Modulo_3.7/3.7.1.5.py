rooms = [[[False for i in  range(20)] for j in range(15)] for k in range(3)]

rooms[1][14][2] = True
rooms[0][4][1] = False

vacancy = 0

for room_number in range(20):
    if not rooms[1][14][room_number]:
        vacancy += 1

print(vacancy)