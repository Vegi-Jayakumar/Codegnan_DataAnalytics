'''
create a dictionary using codegnan portal as example. keys:Exams,Mock Interviews, Project Demos.
'''

mock_CG = {
    "Daily Exams" : ('Monday','Tuesday','Wednesday','Thursday','Friday','Saturday'),    #Tuple
    "Mock Interviews with marks" : {'1st Mock Interview': 7, '2nd Mock Interview': 7},      #Dictionary
    "Subjects" : ['Python','Aptitude','Soft Skills','MySQL'],                               #List
    "Project Demos" : {'predictive analytics for food delivery systems','Library Management System','Inventory Management System'}, #Set
    "Course Completion percentage" : 62.2,                                                     #Float
    "Attendence streak" : 26,                                                                  #Int
    "Exam Streak": 23                                                                           #Int
}

print(mock_CG['Course Completion percentage'])
print(mock_CG['Mock Interviews with marks'])
print(mock_CG['Subjects'])
print(mock_CG['Project Demos'])
print(mock_CG['Daily Exams'])
print(mock_CG['Attendence streak'])
print(mock_CG['Exam Streak'])
