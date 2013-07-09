
def getFibonacci(given_no):
    if given_no == 0: 
        return 0
    if given_no == 1: 
        return 1
    return getFibonacci( given_no - 1) + getFibonacci( given_no - 2)

sum_fibonacci = 0

for number in range(100):    
    got_number = getFibonacci(number)
    print number, got_number
    if got_number >= 4000000:
        break
    if got_number % 2 == 0:
        sum_fibonacci += got_number
    # print number, got_number

print sum_fibonacci
    