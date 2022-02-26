# This is just an alg to produce a single semesters schedule and it does not account for pre/co-requisties
# Nor does it account for when electives are actually being offered. 
# This just gives us something to play with when we are working with our GUI this week. 

def basicAlg(input):
    #13 courses to take 
    courses = [1300, 2824, 2270, 3104, 2400, 3308, 3155, 3702, 3022, 4122, 4502, 2820, 3403]

    #representative of whether the classes have a 5, 10, 15, or 20 hour commitment 
    five = [3308, 4122, 3702, 3403, 4502]
    ten = [1300, 2820]
    fifteen = [2270, 2824, 3155, 3022] 
    twenty = [2400, 3104] 

    take = [] 
    #this program allows for 20 hours of work each week max 
    hours = 0

    for course in courses:
        if (course not in input):
            if course in five and hours <= 15:
                hours = hours + 5 
                take.append(course)
            elif course in ten and hours <= 10:
                hours = hours + 10 
                take.append(course)
            elif course in fifteen and hours <= 5:
                hours = hours + 15
                take.append(course)
            elif course in twenty and hours == 0:
                hours = hours + 20
                take.append(course)
        if hours == 20:
            return take 
    return take



          

