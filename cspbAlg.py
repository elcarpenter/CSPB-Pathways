'''
# Currentyly unused, but want to save 
# [0] == CREDITS, [1] == TIME, [2] == COREQS, [3] == PREREQS
CSPB1300 = [4, 10, [], []] 
CSPB2270 = [4, 15, [], [CSPB1300]] 
CSPB2400 = [4, 20, [CSPB2270], []] 
CSPB2824 = [3, 15, [CSPB1300], []] 
CSPB2820 = [3, 10, [], [CSPB2824]] 
CSPB3022 = [3, 20, [CSPB1300], []]
CSPB3104 = [4, 20, [CSPB2270], [CSPB2824]]
CSPB3112 = [1, 5, [], []]
CSPB3155 = [4, 15, [], [CSPB2270]] 
CSPB3202 = [3, 15, [], [CSPB2824, CSPB2270, CSPB3022]]
CSPB3287 = [3, 10, [], [CSPB2270]] 
CSPB3302 = [3, 15, [], [CSPB2820, CSPB2270, CSPB2824]]
CSPB3308 = [3, 10, [CSPB2270], []]
CSPB3403 = [4, 5, [], [CSPB2400]]
CSPB3702 = [3, 5, [CSPB1300], []] 
CSPB3753 = [4, 20, [], [CSPB2270]] 
CSPB4122 = [3, 5, [CSPB1300, CSPB2824], []]
CSPB4502 = [3, 5, [], [CSPB2270]]  
CSPB4622 = [3, 15, [], [CSPB2824, CSPB2820, CSPB3104]] 



AllCourses = [CSPB1300, CSPB2824, CSPB2270, CSPB3308, CSPB3155, CSPB2400, CSPB3104, 
                CSPB3022, CSPB3202, CSPB2820, CSPB4622, CSPB3302, CSPB4502, CSPB4122, 
                CSPB3702, CSPB3753, CSPB3287, CSPB3403, CSPB3112] 
ReqCourses = [CSPB1300, CSPB2824, CSPB2270, CSPB3308, CSPB3155, CSPB2400, CSPB3104]
Electives = [CSPB3022, CSPB3202, CSPB2820, CSPB4622, CSPB3302, CSPB4502, CSPB4122, CSPB3702, 
                CSPB3753, CSPB3287, CSPB3403, CSPB3112]

#Credit hours 
oneCredit = [CSPB3112] 
threeCredits = [CSPB2824, CSPB3308, CSPB3022, CSPB3202, CSPB2820, CSPB4622, CSPB3302, CSPB4502, CSPB4122, CSPB3702, CSPB3287]
fourCredits = [CSPB1300, CSPB2270, CSPB3104, CSPB2400, CSPB3155, CSPB3753, CSPB3403] 
''' 

# This is just an alg to produce a single semesters schedule 
# This just gives us something to play with when we are working with our GUI this week. 

# TO DO 
# Update Total Credits in main for loop 
# Find way to access different semesters 
# Find best way to organize course list 
    # How can we sort unwanted electives out/prioritize others 
    # What priority do we give required courses? 
# Create a two-semester schedule 

def basicAlg(input, inputHours, inputElectives, inputSemester):
    #courses, excluding 3122
    courses = [1300, 2824, 2270, 3022, 2820, 3403, 3202, 3287, 3753, 4622, 3302, 3104, 2400, 3308, 3155, 3702, 4122, 4502]
    reqCourses = [1300, 2824, 2270, 3104, 2400, 3308, 3155] 
    possible = [] 

    #by semester
    summer2022 = [4122, 3702, 4502, 3287, 3202, 2820, 4622]
    fall2022 = [4122, 3702, 4502, 3753, 3022, 3403, 4622, 3302]
    spring2023 = [4122, 3702, 4502, 3287, 3202, 2820]
    summer2023 = [4122, 3702, 4502, 3753, 3022, 3403, 4622, 3302] 
    fall2023 = [4122, 3702, 4502, 3287, 3202, 2820] 
    spring2024 = [4122, 3702, 4502, 3753, 3022, 3403]
    
    # [summer2022, fall2022, spring2023, summer2023, fall2023, spring2024] 
    # Nested arrays to get elective offering for each semester 
    semesters = [[4122, 3702, 4502, 3287, 3202, 2820, 4622], 
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


    take = [] 
    hours = 0


    for course in courses:
        if course not in input:
            if course in reqCourses:
                if preReqChecker(input, take, course):
                    possible.append(course) 
            if course in semesters[inputSemester]: 
                if preReqChecker(input, take, course):
                    possible.append(course) 
    
    for course in possible:
        if inputHours == 0: 
            return take 
        if course in inputElectives:
            if course in five and inputHours >= 5:
                hours = hours + 5 
                inputHours = inputHours - 5
                take.append(course)
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq):
                            possible.append(coreq) 
            elif course in ten and inputHours >= 10:
                hours = hours + 10
                inputHours = inputHours - 10
                take.append(course)
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq):
                            possible.append(coreq) 
            elif course in fifteen and inputHours >= 15:
                hours = hours + 15
                inputHours = inputHours - 15
                take.append(course)
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq):
                            possible.append(coreq) 
            elif course in twenty and inputHours >= 20:
                hours = hours + 20
                inputHours = inputHours - 20 
                take.append(course)
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq):
                            possible.append(coreq) 
        elif course in reqCourses:
            if course in five and inputHours >= 5:
                hours = hours + 5 
                inputHours = inputHours - 5
                take.append(course)
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq):
                            possible.append(coreq) 
            elif course in ten and inputHours >= 10:
                hours = hours + 10
                inputHours = inputHours - 10
                take.append(course)
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq):
                            possible.append(coreq) 
            elif course in fifteen and inputHours >= 15:
                hours = hours + 15
                inputHours = inputHours - 15
                take.append(course)
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq):
                            possible.append(coreq) 
            elif course in twenty and inputHours >= 20:
                hours = hours + 20
                inputHours = inputHours - 20 
                take.append(course)
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq):
                            possible.append(coreq) 
        else:
            if course in five and inputHours >= 5:
                hours = hours + 5 
                inputHours = inputHours - 5
                take.append(course)
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq):
                            possible.append(coreq) 
            elif course in ten and inputHours >= 10:
                hours = hours + 10
                inputHours = inputHours - 10
                take.append(course)
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq):
                            possible.append(coreq) 
            elif course in fifteen and inputHours >= 15:
                hours = hours + 15
                inputHours = inputHours - 15
                take.append(course)
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq):
                            possible.append(coreq) 
            elif course in twenty and inputHours >= 20:
                hours = hours + 20
                inputHours = inputHours - 20 
                take.append(course)
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq):
                            possible.append(coreq)
    return take 


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
