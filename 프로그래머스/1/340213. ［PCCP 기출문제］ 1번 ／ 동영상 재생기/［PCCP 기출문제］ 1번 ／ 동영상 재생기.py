def solution(video_len, pos, op_start, op_end, commands):
    def to_minute(string):
        return int(string.split(":")[0]) * 60 + int(string.split(":")[1])

    pos = to_minute(pos)

    for c in commands:
        if to_minute(op_start) <= pos <= to_minute(op_end):
            pos = to_minute(op_end)

        if c == "next":
            pos = min(pos + 10, to_minute(video_len))

        elif c == "prev":
            pos = max(0, pos - 10)

        if to_minute(op_start) <= pos <= to_minute(op_end):
            pos = to_minute(op_end)

    answer = ""
    answer += str(pos // 60).zfill(2)
    answer += ":"
    answer += str(pos % 60).zfill(2)

    return answer