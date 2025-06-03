from sol import solution

TEST_CASES = []

def test(case, expected):
    target_times, logs, threshold = case
    result = solution(target_times, logs, threshold)
    status = "✅ PASS" if result == expected else f"❌ FAIL (expected {expected})"
    print(f"solution{case} = {result} → {status}")

if __name__ == '__main__':
    print("=== 테스트 케이스 실행 ===\n")
    for case, expected in TEST_CASES:
        test(case, expected)