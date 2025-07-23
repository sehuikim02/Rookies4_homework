nums = [10, 20, 30, 40, 50]
total = 0

for i in nums:
    total += i

avg = float(total / 5)

print(f'숫자들: {nums}')
print(f'합계: {total} \n평균: {avg}')