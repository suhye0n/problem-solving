while True:
    sentence = input()
    if sentence == '.':
        break

    stack = []
    is_balanced = True

    for char in sentence:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                is_balanced = False
                break
        elif char == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                is_balanced = False
                break

    if is_balanced and not stack:
        print("yes")
    else:
        print("no")