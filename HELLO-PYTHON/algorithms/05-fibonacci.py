

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Imprimir los primeros 6 números:
for i in range(6):
    print(fibonacci(i))
