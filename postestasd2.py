def fibonacci_search(arr, x):
    n = len(arr)

    # Inisialisasi bilangan fibonacci
    fib1, fib2 = 0, 1
    fib = fib1 + fib2

    # Cari bilangan fibonacci terbesar yang kurang dari atau sama dengan n
    while fib < n:
        fib2 = fib1
        fib1 = fib
        fib = fib1 + fib2

    # Indeks awal dan posisi saat ini
    idx = -1
    pos = fib2

    # Lakukan pencarian menggunakan bilangan fibonacci yang lebih kecil
    # sampai mencapai elemen yang dicari
    while fib > 1:
        i = min(idx + fib2, n - 1)
        if arr[i] < x:
            fib = fib1
            fib1 = fib2
            fib2 = fib - fib1
            idx = i
        elif arr[i] > x:
            fib = fib2
            fib1 = fib1 - fib2
            fib2 = fib - fib1
        else:
            return i

    # Jika elemen tidak ditemukan
    if arr[idx+1] == x:
        return idx+1
    else:
        return -1

var = ["Arsel", "Avivah", "Daiva", ["Wahyu", "Wibi"]]

# Output 1
for i in range(len(var)-1):
    index = fibonacci_search(var, var[i])
    print(var[i], "di Index", index)

# Output 2
index = fibonacci_search(var[3], "Wahyu")
print("Wahyu di Index 3 pada kolom", index)

# Output 3
index = fibonacci_search(var[3], "Wibi")
print("Wibi di Index 3 pada kolom", index)
