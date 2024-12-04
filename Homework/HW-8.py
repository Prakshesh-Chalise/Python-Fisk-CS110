# def grade_calculator(input_grades):


#     homework_test = input_grades["homework"]
#     length = len(homework_test)


#     lowest_element = homework_test[0]
#     for x in range(1,length):
            
#             element = homework_test[x]
            
#             if element < lowest_element:
#                    lowest_element = element

#     homework_test.remove(lowest_element)



#     length_2 = len(homework_test)
#     lowest_element_2 = homework_test[0]
#     for y in range(1,length_2):
            
#       element_2 = homework_test[y]
            
#       if element_2 < lowest_element_2:
#         lowest_element_2 = element_2
    
#     homework_test.remove(lowest_element_2)

#     average = 0
#     count  = 0

#     for marks in homework_test:
#            average += marks
#            count += 1     

#     homework_final = (average/count)






#     quiz_test = input_grades["quizzes"]
#     length_3 = len(quiz_test)
#     lowest_element_3 = quiz_test[0]
#     for x in range(1,length_3):
            
#             element_3 = quiz_test[x]
            
#             if element_3 < lowest_element_3:
#                    lowest_element_3 = element_3

#     quiz_test.remove(lowest_element_3)


#     lowest_element_4 = quiz_test[0]
#     length_4 = len(quiz_test)
#     for y in range(1,length_4):
            
#       element_4 = quiz_test[y]
            
#       if element_4 < lowest_element_4:
#         lowest_element_4 = element_4
        
    
#     quiz_test.remove(lowest_element_4)

#     average_2 = 0
#     count_2 = 0

#     for marks in quiz_test:
#            average_2 += marks
#            count_2 += 1     
           
#     quiz_final = (average_2/count_2)


#     project_test = input_grades["project 1"]
#     project_test_2 = input_grades["project 2"]

#     average_3 = 0
#     count_3 = 0

#     for projects in project_test:
#            average_3 += projects
#            count_3 += 1

#     project_final = (average_3/count_3)

#     average_4 = 0
#     count_4 = 0

#     for projects in project_test_2:
#            average_4 += projects
#            count_4 += 1

#     project_final_2 = (average_4/count_4)
    
             
             


#     exam_1 = 0.13 * input_grades["exam 1"]
#     exam_2 = 0.18 * input_grades["exam 2"]
#     final_exam = 0.23 * input_grades["final exam"]
#     homework = 0.07 * homework_final
#     project_1 = 0.12 * project_final
#     project_2 = 0.17 * project_final_2
#     quiz = 0.05 * quiz_final
#     attendances = 0.05 * input_grades["attendance"]

#     score = exam_1 + exam_2 + final_exam + homework + project_1 + project_2 + quiz + attendances
#     if score >= 90:
#             grade = "A"
#     elif 85 <= score < 90:
#             grade = "A-"
#     elif  80 <= score < 85:
#             grade = "B+"
#     elif 75 <= score < 80:
#             grade = "B"
#     elif 70 <= score < 75:
#             grade = "B-"
#     elif 65 <= score < 70:
#             grade = "C+"
#     elif 60 <= score < 65:
#             grade = "C"
#     elif 55 <= score < 60:
#             grade = "C-"
#     elif 50 <= score < 55:
#             grade = "D"
#     else:
#             grade = "F"

#     exam_1_2 = 0.07 * input_grades["exam 1"]
#     exam_2_2 = 0.12 * input_grades["exam 2"]
#     final_exam_2 = 0.17 * input_grades["final exam"]
#     homework_2 = 0.13 * homework_final
#     project_1_2 = 0.18 * project_final
#     project_2_2 = 0.23 * project_final_2
#     quiz_2 = 0.05 * quiz_final
#     attendances_2 = 0.05 * input_grades["attendance"]

#     score_2 = exam_1_2 + exam_2_2 + final_exam_2 + homework_2+ project_1_2 + project_2_2 + quiz_2 + attendances_2
#     if score_2 >= 90:
#             grade_2 = "A"
#     elif 85 <= score_2 < 90:
#             grade_2 = "A-"
#     elif  80 <= score_2 < 85:
#             grade_2 = "B+"
#     elif 75 <= score_2 < 80:
#             grade_2 = "B"
#     elif 70 <= score_2 < 75:
#             grade_2 = "B-"
#     elif 65 <= score_2 < 70:
#             grade_2 = "C+"
#     elif 60 <= score_2 < 65:
#             grade_2 = "C"
#     elif 55 <= score_2 < 60:
#             grade_2 = "C-"
#     elif 50 <= score_2 < 55:
#             grade_2 = "D"
#     else:
#             grade_2 = "F"



#     if score >= score_2:
#             return grade
#     else:
#             return grade_2
    



# input_grades = {
#         'exam 1': 78,
#         'exam 2': 85,
#         'final exam': 70,
#         'homework': [100, 78, 97, 93, 80, 0, 85, 100],
#         'project 1': [70, 96, 100, 100],
#         'project 2': [96, 100, 85],
#         'quizzes': [60, 70, 40, 0, 80, 0, 100, 80, 100, 90],
#         'attendance': 85 
# }

# print(grade_calculator(input_grades))

# DOING THE PROBLEM BY USING THE FUNCTIONS METHOD:

def remove_two_lowest(scores):
    if len(scores) > 2:
        scores.remove(min(scores))
        scores.remove(min(scores))
    return scores

def calculate_average(scores):
    return sum(scores) / len(scores) if scores else 0

def grade_calculator(input_grades):
    homework_scores = remove_two_lowest(input_grades["homework"])
    homework_final = calculate_average(homework_scores)

    quiz_scores = remove_two_lowest(input_grades["quizzes"])
    quiz_final = calculate_average(quiz_scores)

    project_final = calculate_average(input_grades["project 1"])
    project_final_2 = calculate_average(input_grades["project 2"])

    def calculate_score(weights):
        return (
            weights["exam 1"] * input_grades["exam 1"] +
            weights["exam 2"] * input_grades["exam 2"] +
            weights["final exam"] * input_grades["final exam"] +
            weights["homework"] * homework_final +
            weights["project 1"] * project_final +
            weights["project 2"] * project_final_2 +
            weights["quiz"] * quiz_final +
            weights["attendance"] * input_grades["attendance"]
        )

    weights_1 = {
        "exam 1": 0.13, "exam 2": 0.18, "final exam": 0.23,
        "homework": 0.07, "project 1": 0.12, "project 2": 0.17,
        "quiz": 0.05, "attendance": 0.05
    }

    weights_2 = {
        "exam 1": 0.07, "exam 2": 0.12, "final exam": 0.17,
        "homework": 0.13, "project 1": 0.18, "project 2": 0.23,
        "quiz": 0.05, "attendance": 0.05
    }

    score_1 = calculate_score(weights_1)
    score_2 = calculate_score(weights_2)

    def determine_grade(score):
        if score >= 90:
            return "A"
        elif 85 <= score < 90:
            return "A-"
        elif 80 <= score < 85:
            return "B+"
        elif 75 <= score < 80:
            return "B"
        elif 70 <= score < 75:
            return "B-"
        elif 65 <= score < 70:
            return "C+"
        elif 60 <= score < 65:
            return "C"
        elif 55 <= score < 60:
            return "C-"
        elif 50 <= score < 55:
            return "D"
        else:
            return "F"

    grade_1 = determine_grade(score_1)
    grade_2 = determine_grade(score_2)

    return grade_1 if score_1 >= score_2 else grade_2

input_grades = {
    'exam 1': 78,
    'exam 2': 85,
    'final exam': 70,
    'homework': [100, 78, 97, 93, 80, 0, 85, 100],
    'project 1': [70, 96, 100, 100],
    'project 2': [96, 100, 85],
    'quizzes': [60, 70, 40, 0, 80, 0, 100, 80, 100, 90],
    'attendance': 85
}

print(grade_calculator(input_grades))


