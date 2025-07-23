numbers = [15, 3, 27, 8, 19, 12, 31]
numbers_sorted = sorted(numbers, reverse=True)

max_value = numbers_sorted[0]
second_max = numbers_sorted[1]
min_value = numbers_sorted[-1]

print(f"숫자 목록: {numbers}")
print(f"최댓값: {max_value}")
print(f"최솟값: {min_value}")
print(f"두 번째로 큰 값: {second_max}")