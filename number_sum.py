sum_number = 0
while True:
    n = int(input('숫자를 입력하세요. (0을 입력하면 종료): '))
    if n == 0:
        break
    else:
        sum_number += n

print(f'입력된 숫자들의 합: {sum_number}')
    
