def ordenamiento_seleccion(a):
    n = len(a)

    for j in range(n):
        iMin = j

        for i in range(j, n):
            if i == j:
                continue
            if a[i] < a[iMin]:
                iMin = i

        if iMin != j:
            a[j], a[iMin] = a[iMin], a[j]

    return a


datos = [2, 8, 5, 3, 9, 4, 1]
print(ordenamiento_seleccion(datos))