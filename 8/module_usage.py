import datetime
import random

now = datetime.datetime.now()
formatted_date = now.strftime("%Y년 %m월 %d일 %A")

fruits = ['사과', '바나나', '오렌지', '딸기', '포도']

random.shuffle(fruits)

print("현재 날짜와 시간:", now.strftime("%Y-%m-%d %H:%M:%S"))

print("포맷된 날짜:", formatted_date)

print("임의의 숫자:", random.randint(1, 10))
print("임의의 실수:", round(random.uniform(1.0, 10.0), 2))
print("임의의 리스트 요소:", random.choice(fruits))

print("섞인 리스트:", fruits)
