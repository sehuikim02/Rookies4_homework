money = int(input('상품 가격을 입력하세요: '))
discount_num = int(input('할인율을 입력하세요(%): '))

discount = int(money * (discount_num / 100)) 
result = int(money - discount)

print(f"원래 가격: {money}원")
print(f"할인율: {discount_num}%")
print(f"할인 금액: {discount}원")
print(f"최종 가격: {result}원")
