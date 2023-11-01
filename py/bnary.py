def binary(*args, **kwargs):  
    # print("Write the number to convert to binary: ")
    # number = int(input())
    number = Element('test_input').element.value
    number = int(number)
    list = []
    while(number > 0):
        mod = number % 2
        number = number // 2
        list.insert(0,mod)
    # print(list)
    pyscript.write('binRes', list)