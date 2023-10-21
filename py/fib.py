
# fibonacci triangle
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
    pyscript.write('fib1', triangle[0])
    pyscript.write('fib2', triangle[1])
    pyscript.write('fib3', triangle[2])
    pyscript.write('fib4', triangle[3])
    pyscript.write('fib5', triangle[4])
    pyscript.write('fib6', triangle[5])
    pyscript.write('fib7', triangle[6])
    pyscript.write('fib8', triangle[7])
    pyscript.write('fib9', triangle[8])
    pyscript.write('fib10', triangle[9])
        #print(" ".join(map(str, row)))
# print("Enter the number of terms: ", end='')
# n = int(input())
fibonacci_triangle=fib_triangle(10)
print_fib_triangle(fibonacci_triangle)