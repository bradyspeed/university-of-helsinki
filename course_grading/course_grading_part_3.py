# tee ratkaisu tänne
""" student_info = "students1.csv"
exercise_data = "exercises1.csv"
exam_points = "exam_points1.csv" """

student_info = input('Student information: ')
exercise_data = input('Exercises completed: ')
exam_points = input('Exam points: ')



student_dict = {}
with open(student_info) as new_file:
    for line in new_file:
        parts = line.split(';')
        if parts[0] == 'id':
            continue
        name = f'{parts[1].strip()} {parts[2].strip()}'
        student_dict[parts[0]] = name
    #print(student_dict)




exercises_dict = {}
with open(exercise_data) as new_file:
    for line in new_file:
        #line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        id = parts[0]
        exercises_dict[id] = []
        for grade in parts[1:]:
            exercises_dict[id].append(int(grade))
    #print(exercises_dict)



exam_dict = {}
with open(exam_points) as new_file:
    for line in new_file:
        #line = line.replace("\n", "")
        parts = line.split(";")
        if parts[0] == 'id':
            continue
        id = parts[0]
        exam_dict[id] = []
        for points in parts[1:]:
            exam_dict[id].append(int(points))
    #print(exam_dict)




grade_dict = {(0, 15): 0, (15, 18): 1, (18, 21): 2, (21, 24): 3, (24, 28): 4, (28, 1000): 5}



header_1 = 'name'
header_2 = 'exec_nbr'
header_3 = 'exec_pts.'
header_4 = 'exm_pts.'
header_5 = 'tot_pts.'
header_6 = 'grade'
print(f'{header_1:30}{header_2:10}{header_3:10}{header_4:10}{header_5:10}{header_6:10}')



for id, name in student_dict.items():
    if id in exercises_dict and exam_dict:
        total = (sum(exercises_dict[id]) // 4) + sum(exam_dict[id])
        qty = len(exercises_dict[id])
        #print(total)
        for i in grade_dict:
            if total in range(i[0], i[1]):
                final_grade = grade_dict[i]
                print(f'{name:30}{sum(exercises_dict[id]):<10}{sum(exercises_dict[id]) // 4:<10}{sum(exam_dict[id]):<10}{total:<10}{final_grade:<10}')

""" for id, name in student_dict.items():
    if id in exercises_dict:
        total = sum(exercises_dict[id])
        for i in grade_dict:
            if total in range(i[0], i[1]):
                print(f'{name} {total}') """