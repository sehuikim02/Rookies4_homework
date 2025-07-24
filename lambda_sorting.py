students = [('김철수', 85), ('이영희', 92), ('박민수', 78), ('최수진', 95)]

sort_name = sorted(students, key=lambda x: x[0])

sort_score = sorted(students, key=lambda x: x[1])

sorted_score_desc = sorted(students, key=lambda x: x[1], reverse=True)

print("학생 정보:", students)
print("이름순 정렬:", sort_name)
print("점수순 정렬:", sort_score)
print("점수 내림차순:", sorted_score_desc)