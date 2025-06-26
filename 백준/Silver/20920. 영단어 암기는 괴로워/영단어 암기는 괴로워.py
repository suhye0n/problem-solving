import sys

N, M = map(int, sys.stdin.readline().split())
words = {}

for _ in range(N):
    word = sys.stdin.readline().rstrip()

    if len(word) < M:
        continue

    words[word] = words.get(word, 0) + 1

def sort_rule(item):
    word = item[0]
    count = item[1]
    return -count, -len(word), word

sorted_words = sorted(words.items(), key=sort_rule)

for word, _ in sorted_words:
    print(word)
