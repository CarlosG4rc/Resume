
# print ("Enter a positive integer: ")
# num = int(input())
def armstrong(*args, **kwargs):
    num = Element('test_input').element.value
    num = int(num)
    n = num
    num1 = num
    sum = 0
    count = 0
    while( n != 0):
        while(num1 > 0):
            count = count + 1
            num1 = num1 // 10
        rem = n % 10
        sum = sum + rem ** count
        n = n // 10
    if (sum == num):
        pyscript.write('armRes', 'The number is an Armstrong number')
        # print("The number is an Armstrong number")
    else:
        pyscript.write('armRes', 'The number is not an Armstrong number')
        # print("The number is not an Armstrong number")