
# QUESTIONS TO ANSWER 
# When electives we want to take are not being offered, do we delay graduation or take something else? 


def basicAlg(input, inputHours, inputElectives, inputSemester, dontWant):
    #courses, excluding 3122
    courses = [1300, 2824, 2270, 3022, 2820, 3403, 3202, 3104, 2400, 3308, 3155, 3287, 3753, 4622, 3302, 3702, 4122, 4502]
    reqCourses = [1300, 2824, 2270, 3104, 2400, 3308, 3155] 
    electives = [3022, 2820, 3403, 3202, 3287, 3753, 4622, 3302, 3702, 4122, 4502]
    everySem = [1300, 2824, 2270, 3104, 2400, 3308, 3155, 4122, 3702, 4502]
    possible = [] 

    # [summer2022, fall2022, spring2023, summer2023, fall2023, spring2024] 
    # Nested arrays to get elective offering for each semester  
    # semesters[0] = summer2022, semesters[1] = fall2022, etc. 
    semesters = [[4122, 3702, 4502, 3287, 3202, 2820, 4622, 3022], 
                [4122, 3702, 4502, 3753, 3022, 3403, 4622, 3302], 
                [4122, 3702, 4502, 3287, 3202, 2820], 
                [4122, 3702, 4502, 3753, 3022, 3403, 4622, 3302], 
                [4122, 3702, 4502, 3287, 3202, 2820], 
                [4122, 3702, 4502, 3753, 3022, 3403, 4622, 3302]]

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
        return 0


    #Here we need to make sure that we add the necessary electives to the input list
    #to ensure that the user will be eligible to take Robotics, ML, or AI if desired 

    #Machine Learning and Linear Algebra 
    if 4622 in inputElectives and 2820 not in inputElectives:
        if 2820 in dontWant:
            dontWant.remove(2820)
        inputElectives.append(2820)
    #ML and Data Science 
    if 4622 in inputElectives and 3022 not in inputElectives:
        if 3022 in dontWant:
            dontWant.remove(3022)
        inputElectives.append(3022)
    #Robotics and Linear Algebra 
    if 3302 in inputElectives and 2820 not in inputElectives:
        if 2820 in dontWant:
            dontWant.remove(2820)
        inputElectives.append(2820)
    #AI and Data Science 
    if 3202 in inputElectives and 3022 not in inputElectives:
        if 3022 in dontWant:
            dontWant.remove(3022)
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
    
    #if electiveCredits > 21:
    #    return "You've selected too many electives."

    if not (validDontWant(dontWant)):
        count = 0
        for course in dontWant:
            count = count + 3 
            if course == 3403 or course == 3753:
                count = count + 1 
        while count > 15:
            if 3403 in dontWant and 3753 in dontWant:
                dontWant.remove(3403)
                count = count - 4 
            elif 3702 in dontWant:
                dontWant.remove(3702)
                count = count - 3
            elif 4502 in dontWant:
                dontWant.remove(4502)
                count = count - 3
            elif 4122 in dontWant:
                dontWant.remove(4122)
                count = count - 3
            elif 2820 in dontWant:
                dontWant.remove(2820)
                count = count - 3 
            elif 3287 in dontWant:
                dontWant.remove(3287)
                count = count - 3 
            
        
    
    take = [] 
    hours = 0

    if input == [] and inputHours >= 10:
        take.append(1300) 
        inputHours = inputHours - 10
        hours = hours + 10
        totalCredits = totalCredits + 4 

    for course in courses:
        if course not in input and course not in take:
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
                    if totalCredits == 48:
                        if take[0] in electives and take[0] in threeCredits:
                            take.pop(0)
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
                    if totalCredits == 48:
                        if take[0] in electives and take[0] in threeCredits:
                            take.pop(0)
                            totalCredits = totalCredits - 3 
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
                    if totalCredits == 48:
                        if take[0] in electives and take[0] in threeCredits:
                            take.pop(0)
                            totalCredits = totalCredits - 3 
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
                    if totalCredits == 48:
                        if take[0] in electives and take[0] in threeCredits:
                            take.pop(0)
                            totalCredits = totalCredits - 3 
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
                    if totalCredits == 48:
                        if take[0] in electives and take[0] in threeCredits:
                            take.pop(0)
                            totalCredits = totalCredits - 3 
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
                    if totalCredits == 48:
                        if take[0] in electives and take[0] in threeCredits:
                            take.pop(0)
                            totalCredits = totalCredits - 3 
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
                    if totalCredits == 48:
                        if take[0] in electives and take[0] in threeCredits:
                            take.pop(0)
                            totalCredits = totalCredits - 3 
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
                    if totalCredits == 48:
                        if take[0] in electives and take[0] in threeCredits:
                            take.pop(0)
                            totalCredits = totalCredits - 3 
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
                    if totalCredits == 48:
                        if take[0] in electives and take[0] in threeCredits:
                            take.pop(0)
                            totalCredits = totalCredits - 3 
                    return take, totalCredits 
                if course in areCoReqs: 
                    for coreq in haveCoReqs:
                        if coreq not in possible and preReqChecker(input, take, coreq) and coreq not in dontWant and coreq not in input:
                            possible.append(coreq) 

    return take, totalCredits 


def preReqChecker(input, take, course):
    if course == 1300 and 1300 not in input and 1300 not in take:
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
    

def validDontWant(dontWant):
    count = 0
    for course in dontWant:
        count = count + 3 
        if course == 3403 or course == 3753:
            count = count + 1
    if count > 15:
        return 0 
    else:
        return 1

def validInputElectives(inputElectives, input):
    otherCount = 0
    electives = [3022, 2820, 3403, 3202, 3287, 3753, 4622, 3302, 3702, 4122, 4502]
    for course in inputElectives:
        otherCount = otherCount + 3 
        if course == 3403 or course == 3753:
            otherCount = otherCount + 1
    for course in input:
        if course in electives and course not in inputElectives:
            otherCount = otherCount + 3
            if course == 3403 or course == 3753:
                otherCount = otherCount + 1
    if otherCount > 21:
        return 0
    else:
        return 1

def multipleSemesters(input, inputHours, inputElectives, inputSemester, dontWant): 
    schedule_dict = {}
    for sem in inputSemester:
        classes, quit = basicAlg(input, inputHours, inputElectives, sem, dontWant)
        schedule_dict[sem] = classes
        for cspb in classes:
            input.append(cspb)
        if quit >= 45:
            #schedule_dict["That's it!"] = "You've taken all the courses you need to graduate."
            return schedule_dict 
    return schedule_dict

input = []
inputHours = 40
inputElectives = [3022, 3202, 3302, 3753, 3403, 4622] 
dontWant = []
inputSemester = [0,1,2,3,4,5]

print(multipleSemesters(input, inputHours, inputElectives, inputSemester, dontWant))


# Dictionary 

classDict = {
  1300: "Computer Science 1: Starting Computing (4 credits)",
  2824: "Computer Science 2: Data Structures (3 credits)",
  2270: "Data Structures (4 credits)", 
  3104: "Algorithms (4 credits)",
  2400: "Computer Systems (4 credits)",
  3308: "Software Development Methods and Tools (3 credits)", 
  3155: "Principles of Programming Languages (4 credits)",
  3702: "Cognitive Science (3 credits)",
  4502: "Data Mining (3 credits)", 
  4122: "Information Visualization (3 credits)",
  3753: "Design and Analysis of Operating Systems (4 credits)",
  3287: "Design and Analysis of Database Systems (3 credits)",
  3403: "Introductions to CyberSecurity for a Converged World (4 credits)", 
  4622: "Machine Learning (3 credits)",
  3302: "Introduction to Robotics (3 credits)", 
  3202: "Intro to Artificial Intelligence (3 credits)",
  3022: "Intro to Data Science with Probability and Statistics (3 credits)",
  2820: "Linear Algebra with Computer Science Applications (3 credits)", 
}

classlist = "3022 4502 4122"

coursesString = classlist
courseInts = [int(n) for n in coursesString.split()]

#print(courseInts)

