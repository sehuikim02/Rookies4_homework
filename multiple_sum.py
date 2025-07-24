n_list = [i for i in range(1, 100) if i % 3 == 0]
sum_num = sum(n_list)
count = len(n_list)

print(f'1부터 100까지의 3의 배수: {n_list}')
print(f'3의 배수의 합: {sum_num}')
print(f'3의 배수의 개수: {count}개')