fruits = ['사과', '바나나', '오렌지', '포도', '딸기']

print(f'과일 목록: {fruits}')
find_fruit = input("찾을 과일을 입력하세요: ")

for fruit in fruits:
    if fruit == find_fruit:
        print(f'{find_fruit}가 목록에 있습니다!')
    else:
        continue