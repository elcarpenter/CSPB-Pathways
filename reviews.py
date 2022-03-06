
# these will eventually be in a databse that has not been implemented yet
reviews_dict = {
    '1300': "1300 is a great class. It has received 4.5 stars out of 5",
    '2824': "2824 is a great class. It has received 4.5 stars out of 5",
    '2270': "2270 is a great class. It has received 4.5 stars out of 5",
    '3104': "3104 is a great class It has received 4.6 stars out of 5",
    '2400': "2400 is a great class It has received 4.5 stars out of 5",
    '3308': "This is a great class It has received 4.5 stars out of 5",
    '3155': "This is a great class It has received 4.7 stars out of 5",
    '3702': "This is a great class It has received 4.5 stars out of 5",
    '3022': "This is a great class It has received 4.8 stars out of 5",
    '4122': "This is a great class It has received 4.9 stars out of 5",
    '4502': "This is a great class It has received 4.3 stars out of 5",
    '2820': "This is a great class It has received 4.4 stars out of 5",
    '3403': "This is a great class It has received 4.6 stars out of 5"
}


def review_printer(class_array):

    reviews = {}

    for classpicked in class_array:
        reviews[classpicked] = reviews_dict[classpicked]


    return reviews