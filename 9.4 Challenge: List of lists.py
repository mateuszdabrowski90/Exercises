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
    tot_students = 0
    tot_tuition = 0
    student_mean = 0
    student_median = 0
    tuition_mean = 0
    tuition_median = 0
    x = 0
    for i in universities:
        tot_students = tot_students + i[1]
    print(f"Total students: {tot_students:,}")
    for i in universities:
        tot_tuition = tot_tuition + i[2]
    print(f"Total tuition: $ {tot_tuition:,}")
    print(f"Student mean: {tot_students / len(universities):,.2f}")
    sorted_universities = sorted(universities)
    print(sorted_universities)



enrollment_stats(universities)