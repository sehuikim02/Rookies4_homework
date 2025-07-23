sentence = input("문장을 입력하세요: ")
find_word = input("찾을 문자를 입력하세요: ")
count = 0

for i in sentence:
    if(i == find_word):
        count += 1

print(f"문자 '{find_word}'이 {count}번 나타납니다.")
