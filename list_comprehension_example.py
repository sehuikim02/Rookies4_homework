origin_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_num = [num for num in origin_list if num % 2 == 0]
square_even = [num ** 2 for num in even_num]

print(f'원본 리스트: {origin_list}')
print(f'짝수들: {even_num}')
print(f'짝수의 제곱: {square_even}')
