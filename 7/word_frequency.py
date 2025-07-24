from collections import Counter
import re

filename = "sample.txt"

with open(filename, "r", encoding="utf-8") as f:
    text = f.read()

words = re.findall(r'\b[가-힣]+\b', text)

counter = Counter(words)

print("단어 빈도 분석 결과:")
for word, freq in counter.most_common():
    print(f"{word}: {freq}번")
