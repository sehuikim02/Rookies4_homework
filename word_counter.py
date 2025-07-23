sentence = input("문장을 입력하세요: ")

trim_sentence = ' '.join(sentence.split())
num = len(trim_sentence.split())

print(f'공백 제거: {trim_sentence}')
print(f'단어 개수: {num}')
