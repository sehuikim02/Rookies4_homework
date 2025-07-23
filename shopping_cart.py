cart = {
    '사과': [2, 1000],
    '바나나': [3, 800],
    '오렌지': [1, 1500]
}
total_price = 0

print("쇼핑 카트: ")

for fruit, (cnt, price) in cart.items():
    fruit_total = cnt * price
    print(f'{fruit}: {cnt}개 (개당 {price}원) = {fruit_total}원')
    total_price += fruit_total

print(f'총 가격: {total_price}원')