import os

folder = "data"

required_files = ['student_names.txt', 'math.txt', 'statistics.txt', 'physics.txt']
files = os.listdir(folder)


with open(os.path.join(folder, 'student_names.txt'), 'r') as f:
    student_names = [line.strip() for line in f]

def read_scores(filename):
    with open(os.path.join(folder, filename), 'r') as f:
        return [int(line.strip()) for line in f if line.strip()]


math_scores = read_scores('math.txt')
statistics_scores = read_scores('statistics.txt')
physics_scores = read_scores('physics.txt')

students = {}
for i, name in enumerate(student_names):
    students[name] = {
        "math": math_scores[i],
        "statistics": statistics_scores[i],
        "physics": physics_scores[i]
    }

print("Avarage score student:")
student_averages = {}
for name, scores in students.items():
    avg = sum(scores.values()) / len(scores)
    student_averages[name] = avg
    print(f"Student: {name} , Avg Score: {avg:.2f}")
print()

top_students = sorted(student_averages.items(), key=lambda x: x[1], reverse=True)[:3]
print("top-3 student:")
for name, avg in top_students:
    print(name)
print()

print(f"Kilkist Students: {len(students)}\n")

subjects = ['math', 'statistics', 'physics']
for subj in subjects:
    scores = [students[name][subj] for name in student_names]
    avg = sum(scores) / len(scores)
    print(f"Subject: {subj} , avg score: {avg:.2f} , min score: {min(scores)} , max score: {max(scores)}")
print()

for subj in subjects:
    scores = {name: students[name][subj] for name in student_names}
    top_student = max(scores.items(), key=lambda x: x[1])
    print(f"{subj}: Student: {top_student[0]} , Score: {top_student[1]}")
print()

low_students = [name for name, avg in student_averages.items() if avg < 50]
print(f"Students with less 50: {len(low_students)}")
for name in low_students:
    print(name)