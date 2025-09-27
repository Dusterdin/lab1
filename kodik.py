import os


folder = "data"


required_files = ['student_names.txt', 'math.txt', 'statistics.txt', 'physics.txt']

def read_scores(filename):
    with open(os.path.join(folder, filename), 'r') as f:
        return [int(line.strip()) for line in f if line.strip()]

with open(os.path.join(folder, 'student_names.txt'), 'r') as f:
    student_names = [line.strip() for line in f if line.strip()]


math_scores = read_scores('math.txt')
statistics_scores = read_scores('statistics.txt')
physics_scores = read_scores('physics.txt')


n = min(len(student_names), len(math_scores), len(statistics_scores), len(physics_scores))


students = {}
for i in range(n):
    name = student_names[i]
    students[name] = {
        "math": math_scores[i],
        "statistics": statistics_scores[i],
        "physics": physics_scores[i]
    }


print("Середня оцінка кожного студента:")
student_averages = {}
for name, scores in students.items():
    avg = sum(scores.values()) / len(scores)
    student_averages[name] = avg
    print(f"Студент: {name} , середня оцінка: {avg:.2f}")
print()


top_students = sorted(student_averages.items(), key=lambda x: x[1], reverse=True)[:3]
print("Топ-3 студенти:")
for name, avg in top_students:
    print(f"{name} (середня: {avg:.2f})")
print()


print(f"Загальна кількість студентів: {len(students)}\n")

subjects = ['math', 'statistics', 'physics']
for subj in subjects:
    scores = [students[name][subj] for name in students]
    avg = sum(scores) / len(scores)
    print(f"Предмет: {subj} | середня: {avg:.2f} , min: {min(scores)} , max: {max(scores)}")
print()


for subj in subjects:
    scores = {name: students[name][subj] for name in students}
    top_student = max(scores.items(), key=lambda x: x[1])
    print(f"{subj}: студент: {top_student[0]} , оцінка: {top_student[1]}")
print()

low_students = [name for name, avg in student_averages.items() if avg < 50]
print(f"Кількість студентів з оцінкою нижче 50: {len(low_students)}")
for name in low_students:
    print(name)
