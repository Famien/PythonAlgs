import random

### Uses random number generator for 1-5 to generate random number from 1-7
### param: random_from_5: random number generator with first param: start number, second param: end number
### output: random number from 1-7

def random_from_7(random_from_5):
    first_num = random_from_5(1,5)
    second_num = random_from_5(1,5)
    third_num = random_from_5(1,5)
    fourth_num = random_from_5(1,5)
    fifth_num = random_from_5(1,5)
    sixth_num = random_from_5(1,5)
    seventh_num = random_from_5(1,5)

    num_sum = first_num + second_num + third_num + fourth_num + fifth_num + sixth_num + seventh_num

    if num_sum % 7 == 0:
        return 7
    else:
        return num_sum % 7
    
#generate test distribution
"""
distribution = {}
trials = 1000000
for i in range(trials):
    generated_num = random_from_7(random.randrange)
    if generated_num in distribution:
        distribution[generated_num] += 1
    else:
        distribution[generated_num] = 1

for num in distribution.keys():
    distribution[num] = distribution[num]/float(trials)

print "Expected probability for each number: ", 1.0/7
print ""
print "Generated distribution using random_from_7: ", distribution
"""
