total_student_sum = 0
total_tuition_sum = 0
list_uni = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

def enrollment_stats(list_uni):
    for i in list_uni:
            for j in i:
                if j == 1: 
                    total_student_sum += list_uni[j]
                    print(total_student_sum)
            for j in i:
                if j == 2: 
                    total_tuition_sum += list_uni[j]
                    print(total_tuition_sum)

enrollment_stats(list_uni)
print("Total students: {}".format(total_student_sum))
print("Total tuition: $ {}".format(total_tuition_sum))
