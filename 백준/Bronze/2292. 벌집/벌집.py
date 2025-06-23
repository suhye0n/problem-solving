N = int(input())

room = 1 # 현재 단계에서 마지막 방 번호
step = 1 # 현재 위치한 단계

while room < N:
    room += 6 * step
    step += 1

print(step)
