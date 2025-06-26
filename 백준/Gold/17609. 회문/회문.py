def palindrome(s, left, right, chance):
    while left < right:
        if s[left] != s[right]:
            # 기회가 없을 경우(2)
            if chance == 0:
                return 2

            skip_left = palindrome(s, left + 1, right, chance - 1)
            skip_right = palindrome(s, left, right - 1, chance - 1)

            return min(skip_left, skip_right)
        left += 1
        right -= 1
    # 기회가 남아 있으면 회문(0), 아니면 유사회문(1)
    if chance == 1:
        return 0
    else:
        return 1

T = int(input())
for _ in range(T):
    s = input().rstrip()
    print(palindrome(s, 0, len(s) - 1, 1))
