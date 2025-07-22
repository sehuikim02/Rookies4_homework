num = int(input('원의 반지름을 입력하세요: '))

area = (num ** 2) * 3.1415
peri = 2 * num  * 3.1415

print(f"\n반지름이 {num}인 원의 넓이: {area:.2f}")
print(f"\n반지름이 {num}인 원의 둘레: {peri:.2f}")