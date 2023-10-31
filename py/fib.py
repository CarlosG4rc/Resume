from js import console

def fibonacci(*args, **kwargs):
    number = Element('test_input').element.value
    number = int(number)
    fibonacci_triangle=fib_triangle(number)
    print_fib_triangle(fibonacci_triangle)

def fib_triangle(n):
    triangle = []
    
    for i in range(n):
        row = []
        for j in range(i+1):
            if j == 0 or j == i:
                row.append(1)
            else:
                row.append(triangle[i-1][j-1] + triangle[i-1][j])
        triangle.append(row)
    return triangle
def print_fib_triangle(triangle):
    for row in range(0,len(triangle)):
        div = 'fib' + str(row)
        pyscript.write(div, triangle[row])
        #print(" ".join(map(str, row)))
# print("Enter the number of terms: ", end='')
# n = int(input())