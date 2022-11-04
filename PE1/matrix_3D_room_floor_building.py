rooms = [[[False for r in range(20)] for f in range(15)] for t in range(3)]

rooms[1][9][13] = True # 2 building 10 floor room 14
rooms[1][9][0] = True
rooms[1][9][3] = True

vacancy = 0
for room_number in range(20):
    if not rooms[1][9][room_number]:
        vacancy += 1

print(vacancy)
# print(rooms)