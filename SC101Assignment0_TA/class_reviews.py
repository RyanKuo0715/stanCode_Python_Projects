"""
File: class_reviews.py
Name: Ryan Kuo
-------------------------------
At the beginning of this program, the user is asked to input
the class name (either SC001 or SC101).
Attention: your input should be case-insensitive.
If the user input "-1" for class name, your program would show
the maximum, minimum, and average among all the inputs.
"""

EXIT = '-1'


def main():
    """
    classify scores into 2 categories(SC001 and SC101) and count their maximum,
    minimum, and average scores separately
    """
    max1 = max2 = float('-inf')
    min1 = min2 = float('inf')
    total1 = count1 = total2 = count2 = 0
    while True:
        course = input('Which class? ')
        if course == EXIT:
            break
        score = int(input('Score: '))
        if course.upper() == 'SC001':
            count1 += 1
            max1, min1, total1 = score_analyzer(max1, min1, total1, score)
        elif course.upper() == 'SC101':
            count2 += 1
            max2, min2, total2 = score_analyzer(max2, min2, total2, score)
    show_score(max1, min1, total1, count1, max2, min2, total2, count2)


def score_analyzer(maximum, minimum, total, score):
    """
    :param maximum: int, maximum score
    :param minimum: int, minimum score
    :param total: int, the sum of scores
    :param score: int, the input score to be analyzed
    :return: the maximum, minimum, and sum of scores that takes the input score into consideration
    """
    total += score
    if score > maximum:
        maximum = score
    if score < minimum:
        minimum = score
    return maximum, minimum, total


def show_score(max1, min1, total1, count1, max2, min2, total2, count2):
    """
    :param max1: int, the maximum score of SC001
    :param min1: int, the minimum score of SC001
    :param total1: int, the sum of scores of SC001
    :param count1: int, the number of scores of SC001
    :param max2: int, the maximum score of SC101
    :param min2: int, the minimum score of SC101
    :param total2: int, the sum of scores of SC101
    :param count2: int, the number of scores of SC101
    :return: the maximum, minimum, and the average scores of SC001 and SC101
    """
    if not count1 and not count2:
        print('No class scores were entered')
    else:
        show_course_score('SC001', count1, max1, min1, total1)
        show_course_score('SC101', count2, max2, min2, total2)


def show_course_score(course, count, maximum, minimum, total):
    """
    :param course: str, SC001 or SC101
    :param count: int, the number of scores
    :param maximum: int, the maximum score
    :param minimum: int, the minimum score
    :param total: int, the sum of scores
    :return: the maximum, minimum, and the average scores of SC001 and SC101
    """
    print('='*13 + course + '='*13)
    if not count:
        print('No score for ' + course)
    else:
        print('Max (' + course[2:] + ') : ' + str(maximum))
        print('Min (' + course[2:] + ') : ' + str(minimum))
        print('Avg (' + course[2:] + ') : ' + str(total/count))


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
