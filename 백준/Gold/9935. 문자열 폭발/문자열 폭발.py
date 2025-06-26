text = input() # 원래 문자열
boom = input() # 폭발 문자열
result = []

boom_length = len(boom)

for char in text:
    result.append(char)

    if len(result) >= boom_length:
        if ''.join(result[-boom_length:]) == boom:
            del result[-boom_length:]

if result:
    print(''.join(result))
else:
    print('FRULA')