N = int(input())
base = input() # 기준이 되는 첫 단어
count = 0 # 비슷한 단어 개수

for _ in range(N - 1):
    word = input()
    base_list = list(base)
    diff = 0 # 다른 문자 개수

    for char in word:
        if char in base_list:
            base_list.remove(char)
        else:
            diff += 1

    if diff < 2 and len(base_list) < 2:
        count += 1

print(count)
