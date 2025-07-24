nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

square = list(map(lambda x: x ** 2, nums))

filter_nums = list(filter(lambda x: x > 5, nums))

filter_square = list(map(lambda x: x ** 2, filter_nums))


print("원본 숫자:", nums)
print("모든 수의 제곱:", square)
print("5보다 큰 수들:", filter_nums)
print("5보다 큰 수들의 제곱:", filter_square)