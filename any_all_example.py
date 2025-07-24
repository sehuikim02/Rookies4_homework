num1 = [2, 4, 6, 8, 10]
num2 = [1, 3, 5, 7, 12]

print("숫자 리스트:", num1)
print("모든 수가 짝수인가?", all(num % 2 == 0 for num in num1))
print("하나라도 10보다 큰 수가 있는가?", any(num > 10 for num in num1))
print()
print("숫자 리스트2:", num2)
print("모든 수가 짝수인가?", all(num % 2 == 0 for num in num2))
print("하나라도 10보다 큰 수가 있는가?", any(num > 10 for num in num2))
