def ordenamiento_insercion(a):
    n = len(a)
    
    for i in range(1, n):
        j = i
        while j > 0 and a[j - 1] > a[j]:
            auxiliar = a[j]
            a[j] = a[j - 1]
            a[j - 1] = auxiliar
            j = j - 1
            
    return a


datos = [2, 8, 5, 3, 9, 4, 1]
print(ordenamiento_insercion(datos))