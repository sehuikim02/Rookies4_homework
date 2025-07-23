students = {
    "김철수": 85,
    "이영희": 92,
    "박민수": 78,
    "최수진": 95
}

print("학생 성적:")

for name, score in students.items():
    print(f"{name}: {score}점")

avg = sum(students.values()) / len(students)

print(f"평균 점수: {avg:.1f}점")
