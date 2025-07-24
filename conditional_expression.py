nums = [-3, 5, 12, -1, 8, 23, -7]
score = 85
age = 17

result = "합격" if score >= 80 else "불합격"

status = "성인" if age >= 20 else "미성년자"

max_num = max(nums) if nums else None

positive_num = [num for num in nums if num > 0] if nums else []

print(f"점수: {score}, 결과: {result}")
print(f"나이: {age}, 상태: {status}")
print(f"숫자들의 최대값: {max_num}")
print(f"양수들: {positive_num}")
