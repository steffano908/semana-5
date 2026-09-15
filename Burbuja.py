def ordenamiento_burbuja(a):
    n = len(a)
    
    for i in range(1, n):
        for j in range(0, n - 1):
            if a[j] > a[j + 1]:
                auxiliar = a[j]
                a[j] = a[j + 1]
                a[j + 1] = auxiliar
                
    return a


datos = [2, 8, 5, 3, 9, 4, 1]
print(ordenamiento_burbuja(datos))