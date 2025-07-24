def recursive(n):     # 재귀 함수
    if n <= 1:
        return 1
    else:
        return n * recursive(n - 1)
    
def iterative(n):     # 반복
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"5! (재귀) = {recursive(5)}")
print(f"5! (반복) = {iterative(5)}")

print(f"7! (재귀) = {recursive(7)}")
print(f"7! (반복) = {iterative(7)}")
