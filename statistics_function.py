import math

def calculate_stats(nums):
    n = len(nums)
    mean = sum(nums) / n
    max_val = max(nums)
    min_val = min(nums)
    
    variance = sum((x - mean) ** 2 for x in number) / (n - 1)
    std_val = math.sqrt(variance)
    return mean, max_val, min_val, std_val

number = [10, 20, 30, 40, 50]

mean, max_val, min_val, std_val = calculate_stats(number)

print("숫자들:", number)
print(f"평균: {mean:.1f}")
print(f"최댓값: {max_val}")
print(f"최솟값: {min_val}")
print(f"표준편차: {std_val:.2f}")
