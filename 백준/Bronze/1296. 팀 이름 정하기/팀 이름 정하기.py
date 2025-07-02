import sys

yeondu = input().strip()
t = int(input())

teams = [0] * t
for i in range(t):
    teams[i] = sys.stdin.readline().strip()

# 점수 계산 함수
def calculate_score(team):
    word = yeondu + team
    L = word.count('L')
    O = word.count('O')
    V = word.count('V')
    E = word.count('E')
    return ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100

# 각 팀의 점수
team_scores = []
for team in teams:
    score = calculate_score(team)
    team_scores.append((score, team))

# 버블 정렬
n = len(team_scores)
for i in range(n):
    for j in range(0, n - i - 1):
        score1, name1 = team_scores[j]
        score2, name2 = team_scores[j + 1]
        # 점수 내림차순
        if score1 < score2:
            team_scores[j], team_scores[j + 1] = team_scores[j + 1], team_scores[j]
        # 점수가 같으면 이름 오름차순
        elif score1 == score2:
            if name1 > name2:
                team_scores[j], team_scores[j + 1] = team_scores[j + 1], team_scores[j]

print(team_scores[0][1])
