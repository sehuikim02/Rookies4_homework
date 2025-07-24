text = "Python is awesome programming language"

split_text = text.split()
joined_text = '-'.join(split_text)
upper_text = text.upper()

print(f'원본 문자열: {text}')
print(f'분리된 문자열: {split_text}')
print(f'하이픈으로 연결: {joined_text}')
print(f'대문자로 변환 후 공백으로 연결: {upper_text}')