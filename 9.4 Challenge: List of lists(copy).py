universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats(universities):
    student_enrollment = []
    for i in universities:
        student_enrollment.append(i[1])
    tuition_fees = []
    for i in universities:
        tuition_fees.append(i[2])
    return student_enrollment, tuition_fees
def mean(a):
    sum = 0
    for i in a:
        sum = sum + i
    mean = sum / len(a)
    return mean

def median(b):
    sorted_list = sorted(b)
    sum = 0
    length = len(b)
    for i in b:
        sum = sum + i
    middle_index = length // 2
    if length % 2 == 0:
        median = (sorted_list[middle_index - 1] + sorted_list[middle_index] / 2)
    else:
        median = sorted_list[middle_index]
    return median

print(f"Total students: {sum(enrollment_stats(universities)[0]):,}")
print(f"Total tuition: $ {sum(enrollment_stats(universities)[1]):,}")
print( )
print(f"Student mean: {mean(enrollment_stats(universities)[0]):,.2f}")
print(f"Student median: {median(enrollment_stats(universities)[0]):,}")
print()
print(f"Tuition mean: $ {mean(enrollment_stats(universities)[1]):,.2f}")
print(f"Tuition median: $ {median(enrollment_stats(universities)[1]):,}")


