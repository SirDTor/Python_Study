import random
subjects = ['Python1', 'Python2', 'Python3', 'Python4', 'Python5']
youngest_student = []
oldest_student = []

def generate_students(num_students):
    first_names = ['Иван', 'Петр', 'Сидор',
                   'Алексей', 'Мария', 'Елена', 'Анна', 'Ксения']
    last_names = ['Иванов', 'Петров', 'Сидоров', 'Алексеев',
                  'Маркова', 'Еленова', 'Аннова', 'Ксенева']
    middle_names = ['Иванович', 'Петрович', 'Сидорович',
                    'Алексеевич', 'Марковна', 'Еленовна', 'Анновна', 'Ксеневна']
    global subjects
    groups = [101, 102, 103]
    students = []
    for i in range(num_students):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        middle_name = random.choice(middle_names)
        year_of_birth = random.randint(1995, 2005)
        course = random.randint(1, 4)
        group_number = random.choice(groups)
        grades = [random.randint(2, 5) for i in range(len(subjects))]
        student = {'last_name': last_name, 'first_name': first_name, 'middle_name': middle_name,
                   'year_of_birth': year_of_birth, 'course': course, 'group_number': group_number, 'grades': grades}
        students.append(student)
    return students


def sort_students(students):
    sorted_students = sorted(
        students, key=lambda x: (x['course'], x['last_name']))
    return sorted_students


def avarage_grades(students):
    global subjects
    average_grades = {}
    for subject in subjects:
        total_grade = 0
        for student in students:
            total_grade += student['grades'][subjects.index(subject)]
        average_grade = total_grade / len(students)
        average_grades[subjects[subjects.index(subject)]] = round(
            average_grade, 2)
    return average_grades


def find_age_students(students):
    global youngest_student 
    global oldest_student
    youngest_student = max(students, key=lambda x: x['year_of_birth'])
    oldest_student = min(students, key=lambda x: x['year_of_birth'])


def find_best_student_by_group(students):
    groups = set([student['group_number'] for student in students])
    best_students = {}
    for group in groups:
        group_students = [student for student in students if student['group_number'] == group]
        best_student = max(group_students, key=lambda x: sum(x['grades']))
        best_students[group] = f"{best_student['last_name']} {best_student['first_name']} {best_student['middle_name']}"
    return best_students


students = generate_students(10)
sorted_students = sort_students(students)
for student in sorted_students:
    print(student)
average_grades = avarage_grades(students)
for subject, grade in average_grades.items():
    print(f"Средний балл по предмету {subject}: {grade}")
find_age_students(students)
print(f"Самый старший студент: {oldest_student['last_name']} {oldest_student['first_name']} {oldest_student['middle_name']}")
print(f"Самый младший студент: {youngest_student['last_name']} {youngest_student['first_name']} {youngest_student['middle_name']}")
best_students_by_group = find_best_student_by_group(students)
for group, best_student in best_students_by_group.items():
    print(f"Лучший студент в группе {group}: {best_student}")