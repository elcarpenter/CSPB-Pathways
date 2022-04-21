
# TO DO and QUESTIONS TO ANSWER 
# How to make sure they take all of the required classes 
# Find way to access different semesters 
# Find best way to organize course list 
    # How can we sort unwanted electives out/prioritize others 
    # What priority do we give required courses? 
# Create a two-semester schedule 
# When electives we want to take are not being offered, do we delay graduation or take something else? 
# How to take of pre-reqs for wanted electives 
    # EX: If someone wants 4622, but doesn't list 2820, how do we make sure it gets taken? 

def basicAlg(input, inputHours, inputElectives, inputSemester, dontWant):
    #courses, excluding 3122
    courses = [1300, 2824, 2270, 3022, 2820, 3403, 3202, 3104, 2400, 3308, 3155, 3287, 3753, 4622, 3302, 3702, 4122, 4502]
    reqCourses = [1300, 2824, 2270, 3104, 2400, 3308, 3155] 
    electives = [3022, 2820, 3403, 3202, 3287, 3753, 4622, 3302, 3702, 4122, 4502]
    everySem = [1300, 2824, 2270, 3104, 2400, 3308, 3155, 4122, 3702, 4502]
    possible = [] 

    #by semester
    summer2022 = [4122, 3702, 4502, 3287, 3202, 2820, 4622, 3022]
    fall2022 = [4122, 3702, 4502, 3753, 3022, 3403, 4622, 3302]
    spring2023 = [4122, 3702, 4502, 3287, 3202, 2820]
    summer2023 = [4122, 3702, 4502, 3753, 3022, 3403, 4622, 3302] 
    fall2023 = [4122, 3702, 4502, 3287, 3202, 2820] 
    spring2024 = [4122, 3702, 4502, 3753, 3022, 3403]

    # [summer2022, fall2022, spring2023, summer2023, fall2023, spring2024] 
    # Nested arrays to get elective offering for each semester  
    # semesters[0] = summer2022, semesters[1] = fall2022, etc. 
    semesters = [[4122, 3702, 4502, 3287, 3202, 2820, 4622, 3022], 
                [4122, 3702, 4502, 3753, 3022, 3403, 4622, 3302], 
                [4122, 3702, 4502, 3287, 3202, 2820], 
                [4122, 3702, 4502, 3753, 3022, 3403, 4622, 3302], 
                [4122, 3702, 4502, 3287, 3202, 2820], 
                [4122, 3702, 4502, 3753, 3022, 3403]]

    #representative of whether the classes have a 5, 10, 15, or 20 hour commitment 
    #unsure about 3302 (robotics) and 4622 (ML) for now 
    five = [4122, 3702, 3403, 4502]
    ten = [1300, 2820, 3308, 3287] 
    fifteen = [2270, 2824, 3155, 3022, 4622, 3302] 
    twenty = [2400, 3104, 3202, 3753] 

    threeCredits = [4122, 3702, 4502, 2820, 3308, 3287, 3022, 2824, 3202, 3302, 4622] 
    fourCredits = [2400, 3104, 3155, 3403, 3753, 1300, 2270] 

    # These smaller lists make it easier to determine when we can take advantage of the few co-reqs in the program, 
    # instead of going through every class
    haveCoReqs = [3702, 4122, 3022, 2824, 2400, 3308, 3104] 
    areCoReqs = [1300, 2824, 2270]

    totalCredits = 0 
    for course in input:
        if course in threeCredits:
            totalCredits = totalCredits + 3 
        if course in fourCredits:
            totalCredits = totalCredits + 4 

    if totalCredits >= 45:
        return "Congratulations! You've finished the program."


    #Here we need to make sure that we add the necessary electives to the input list
    #to ensure that the user will be eligible to take Robotics, ML, or AI if desired 

    #Machine Learning and Linear Algebra 
    if 4622 in inputElectives and 2820 not in inputElectives:
        if 2820 in dontWant:
            return "If you want to take Machine Leanrning, you have to take Linear Algebra"
        inputElectives.append(2820)
    #ML and Data Science 
    if 4622 in inputElectives and 3022 not in inputElectives:
        if 3022 in dontWant:
            return "If you want to take Machine Leanrning, you have to take Data Science"
        inputElectives.append(3022)
    #Robotics and Linear Algebra 
    if 3302 in inputElectives and 2820 not in inputElectives:
        if 2820 in dontWant:
            return "If you want to take Robtoics, you have to take Linear Algebra"
        inputElectives.append(2820)
    #AI and Data Science 
    if 3202 in inputElectives and 3022 not in inputElectives:
        if 3022 in dontWant:
            return "If you want to take Machine Leanrning, you have to take Data Science"
        inputElectives.append(3022)
    
    electiveCredits = 0 
    for course in inputElectives:
        electiveCredits = electiveCredits + 3
        if course in fourCredits:
            electiveCredits = electiveCredits + 1 
    
    for course in electives:
        if course not in inputElectives and course in input:
            electiveCredits = electiveCredits + 3
            if course in fourCredits:
                electiveCredits = electiveCredits + 1 
    
    if electiveCredits > 21:
        return "You've selected too many electives."
        
    
    take = [] 
    hours = 0

    for course in courses:
        if course not in input:
            if course in reqCourses:
                if preReqChecker(input, take, course):
                    possible.append(course) 
            if course in semesters[inputSemester] and course not in dontWant: 
                if preReqChecker(input, take, course):
                    possible.append(course) 
    
    
    for course in possible:
        if inputHours == 0: 
            return take, totalCredits 
        if course in inputElectives:
            if course in five and inputHours >= 5:
                hours = hours + 5 
                inputHours = inputHours - 5
                take.append(course)
                totalCredits = totalCredits + 3 
                if course in fourCredits:
                    totalCredits = totalCredits + 1
                if totalCredits >= 45:
                    return take, totalCredits 
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq) and coreq not in dontWant and coreq not in input:
                            possible.append(coreq) 
            elif course in ten and inputHours >= 10:
                hours = hours + 10
                inputHours = inputHours - 10
                take.append(course)
                totalCredits = totalCredits + 3 
                if course in fourCredits:
                    totalCredits = totalCredits + 1
                if totalCredits >= 45:
                    return take, totalCredits 
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq) and (coreq not in dontWant) and coreq not in input:
                            possible.append(coreq) 
            elif course in fifteen and inputHours >= 15:
                hours = hours + 15
                inputHours = inputHours - 15
                take.append(course)
                totalCredits = totalCredits + 3 
                if course in fourCredits:
                    totalCredits = totalCredits + 1
                if totalCredits >= 45:
                    return take, totalCredits 
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq) and coreq not in dontWant and coreq not in input:
                            possible.append(coreq) 
            elif course in twenty and inputHours >= 20:
                hours = hours + 20
                inputHours = inputHours - 20 
                take.append(course)
                totalCredits = totalCredits + 3 
                if course in fourCredits:
                    totalCredits = totalCredits + 1
                if totalCredits >= 45:
                    return take, totalCredits 
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq) and coreq not in dontWant and coreq not in input:
                            possible.append(coreq) 

    for course in possible:
        if inputHours == 0: 
            return take, totalCredits 
        if course in reqCourses:
            if course in five and inputHours >= 5:
                hours = hours + 5 
                inputHours = inputHours - 5
                take.append(course)
                totalCredits = totalCredits + 3 
                if course in fourCredits:
                    totalCredits = totalCredits + 1
                if totalCredits >= 45:
                    return take, totalCredits 
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq) and coreq not in dontWant and coreq not in input:
                            possible.append(coreq) 
            elif course in ten and inputHours >= 10:
                hours = hours + 10
                inputHours = inputHours - 10
                take.append(course)
                totalCredits = totalCredits + 3 
                if course in fourCredits:
                    totalCredits = totalCredits + 1
                if totalCredits >= 45:
                    return take, totalCredits 
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq) and (coreq not in dontWant) and coreq not in input:
                            possible.append(coreq) 
            elif course in fifteen and inputHours >= 15:
                hours = hours + 15
                inputHours = inputHours - 15
                take.append(course)
                totalCredits = totalCredits + 3 
                if course in fourCredits:
                    totalCredits = totalCredits + 1
                if totalCredits >= 45:
                    return take, totalCredits 
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq) and coreq not in dontWant and coreq not in input:
                            possible.append(coreq) 
            elif course in twenty and inputHours >= 20:
                hours = hours + 20
                inputHours = inputHours - 20 
                take.append(course)
                totalCredits = totalCredits + 3 
                if course in fourCredits:
                    totalCredits = totalCredits + 1
                if totalCredits >= 45:
                    return take, totalCredits 
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq) and coreq not in dontWant and coreq not in input:
                            possible.append(coreq) 

    for course in possible:
        if inputHours == 0: 
            return take, totalCredits 
        if electiveCredits >= 19:
            return take, totalCredits 
        if course not in inputElectives and course not in reqCourses:
            if course in five and inputHours >= 5:
                hours = hours + 5 
                inputHours = inputHours - 5
                take.append(course)
                totalCredits = totalCredits + 3 
                electiveCredits = electiveCredits + 3 
                if course in fourCredits:
                    totalCredits = totalCredits + 1
                    electiveCredits = electiveCredits + 1 
                if totalCredits >= 45:
                    return take, totalCredits 
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq) and coreq not in dontWant and coreq not in input:
                            possible.append(coreq) 
            elif course in ten and inputHours >= 10:
                hours = hours + 10
                inputHours = inputHours - 10
                take.append(course)
                totalCredits = totalCredits + 3 
                electiveCredits = electiveCredits + 3 
                if course in fourCredits:
                    totalCredits = totalCredits + 1
                    electiveCredits = electiveCredits + 1
                if totalCredits >= 45:
                    return take, totalCredits 
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq) and (coreq not in dontWant) and coreq not in input:
                            possible.append(coreq) 
            elif course in fifteen and inputHours >= 15:
                hours = hours + 15
                inputHours = inputHours - 15
                take.append(course)
                totalCredits = totalCredits + 3 
                electiveCredits = electiveCredits + 3 
                if course in fourCredits:
                    totalCredits = totalCredits + 1
                    electiveCredits = electiveCredits + 1
                if totalCredits >= 45:
                    return take, totalCredits 
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq) and coreq not in dontWant and coreq not in input:
                            possible.append(coreq) 
            elif course in twenty and inputHours >= 20:
                hours = hours + 20
                inputHours = inputHours - 20 
                take.append(course)
                totalCredits = totalCredits + 3 
                electiveCredits = electiveCredits + 3 
                if course in fourCredits:
                    totalCredits = totalCredits + 1
                    electiveCredits = electiveCredits + 1 
                if totalCredits >= 45:
                    return take, totalCredits 
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq) and coreq not in dontWant and coreq not in input:
                            possible.append(coreq) 
    return take, totalCredits 


def preReqChecker(input, take, course):
    if course == 1300:
        return True 
    elif course == 2824 or course == 3702 or course == 3022: 
        if 1300 in input or 1300 in take: 
            return True
    elif course == 2270:
        if 1300 in input:
            return True 
    elif course == 3308 or course == 2400:
        if 2270 in input or 2270 in take:
            return True
    elif course == 3104:
        if 2824 in input and (2270 in take or 2270 in input):
            return True
    elif course == 3155 or course == 3753:
        if 2824 in input and 2270 in input:
            return True
    elif course == 3403:
        if 2400 in input:
            return True 
    elif course == 4502 or course == 3287:
        if 2270 in input:
            return True
    elif course == 4122:
        if (1300 in input or 1300 in take) and (2824 in input or 2824 in take):
            return True
    elif course == 2820:
        if 2824 in input:
            return True
    elif course == 3302:
        if 2270 in input and 2824 in input and 2820 in input:
            return True
    elif course == 3202:
        if 2270 in input and 3022 in input and 2824 in input:
            return True
    elif course == 4622:
        if 3104 in input and 3022 in input and 2820 in input:
            return True 
    return False 
    
        #1300, 2824, 2270, 3104, 2400, 3308, 2820, 4502, 3302, 3702, 3022
        #3155, 3403
'''
input = [1300, 2824, 2270, 3104, 3702, 2400, 4122] 
inputHours = 25
inputElectives = [] 
dontWant = []
inputSemester = [0,1,2,3]
'''

#print(basicAlg(input, inputHours, inputElectives, inputSemester, dontWant)) 

def multipleSemesters(input, inputHours, inputElectives, inputSemester, dontWant): 
    for sem in inputSemester:
        classes, quit = basicAlg(input, inputHours, inputElectives, sem, dontWant)
        for cspb in classes:
            input.append(cspb)
        print(classes) 
        if quit >= 45:
            return "That's the end!" 

#print(multipleSemesters(input, inputHours, inputElectives, inputSemester, dontWant)) 