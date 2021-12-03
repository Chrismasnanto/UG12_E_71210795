#program fungsi nilai_maksimal

print("Test case 1")

x = [3, 20, 100, -35, 50]

def nilai_maksimal(deret_bilangan):
    nilai_terbesar = deret_bilangan[0]
    for nilai in deret_bilangan:
        if nilai > nilai_terbesar:
            nilai_terbesar = nilai
    return nilai_terbesar

def nilai_minimal(deret_bilangan):
    nilai_terkecil = deret_bilangan[0]
    for nilai in deret_bilangan:
        if nilai < nilai_terkecil:
            nilai_terkecil = nilai

    return nilai_terkecil

print(x)
print("Nilai terbesar: " , nilai_maksimal(x))
print("Nilai terkecil: " , nilai_minimal(x))

print("Test case 2")

y = [3, 20, 90, 35, 50]

def nilai_maksimal(deret_bilangan):
    nilai_terbesar = deret_bilangan[0]
    for nilai in deret_bilangan:
        if nilai > nilai_terbesar:
            nilai_terbesar = nilai
    return nilai_terbesar

def nilai_minimal(deret_bilangan):
    nilai_terkecil = deret_bilangan[0]
    for nilai in deret_bilangan:
        if nilai < nilai_terkecil:
            nilai_terkecil = nilai

    return nilai_terkecil

print(y)
print("Nilai terbesar: " , nilai_maksimal(y))
print("Nilai terkecil: " , nilai_minimal(y))
