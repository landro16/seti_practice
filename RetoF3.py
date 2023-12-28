def fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series
n = int(input("Ingrese la cantidad de numeros de la serie Fibonacci que deseas imprimir: "))
resultado = fibonacci(n)
print("Los primeros", n, "números de la serie de Fibonacci son:", resultado)
