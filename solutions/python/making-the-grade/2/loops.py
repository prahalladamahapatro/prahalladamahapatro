"""Functions for organizing and calculating student exam scores."""


def round_scores(student_scores):
    """Round all provided student scores.

    :param student_scores: list - float or int of student exam scores.
    :return: list - student scores *rounded* to nearest integer value.
    """
    l = []
    for value in student_scores:
        if student_scores:    #if the tuple is not empty, then do rounding of numbers
            #l[i] = round(value)    # you can't perform item assignment on an empty list
            l.append(round(value))
    return list(reversed(l))     #always use list(), after reversed(), because it will return a                                       Reference object, not a list. But sorted() returns a list.

def count_failed_students(student_scores):
    """Count the number of failing students out of the group provided.

    :param student_scores: list - containing int student scores.
    :return: int - count of student scores at or below 40.
    """
    i = 0
    for x in student_scores:
        if x <= 40:
            i += 1
    return i


def above_threshold(student_scores, threshold):
    """Determine how many of the provided student scores were 'the best' based on the provided threshold.

    :param student_scores: list - of integer scores.
    :param threshold: int - threshold to cross to be the "best" score.
    :return: list - of integer scores that are at or above the "best" threshold.
    """
    l = []
    for x in student_scores:
        if x >= threshold:
            l.append(x)
    return l


def letter_grades(highest):
    """Create a list of grade thresholds based on the provided highest grade.

    :param highest: int - value of highest exam score.
    :return: list - of lower threshold scores for each D-A letter grade interval.
            For example, where the highest score is 100, and failing is <= 40,
            The result would be [41, 56, 71, 86]:

            41 <= "D" <= 55
            56 <= "C" <= 70
            71 <= "B" <= 85
            86 <= "A" <= 100
    """
    # as the lowest score remains the same(40), so we have to divide the remaining numbers (from 41     to the highest score) into 4 groups.
    l = [41]    #initialize the list with the lowest number
    n = (highest - 40) // 4
    for _ in range(3):    #already one element is present in the list, so we'll loop for 3 times
        l.append(l[-1] + n)
    return l


def student_ranking(student_scores, student_names):
    """Organize the student's rank, name, and grade information in descending order.

    :param student_scores: list - of scores in descending order.
    :param student_names: list - of string names by exam score in descending order.
    :return: list - of strings in format ["<rank>. <student name>: <score>"].
    """
    l = []
    for i, x in enumerate(student_scores):
        s = ''
        s = s + str(i+1) + '. ' + student_names[i] + ': ' + str(x)
        l.append(s)
    return l


def perfect_score(student_info):
    """Create a list that contains the name and grade of the first student to make a perfect score on the exam.

    :param student_info: list - of [<student name>, <score>] lists.
    :return: list - first `[<student name>, 100]` or `[]` if no student score of 100 is found.
    """
    for x in student_info:
        if x[-1] == 100:
            return x
    return []
