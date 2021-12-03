# Program Menampilkan baris deret angka

ab = int(input("Masukan awal deret: "))
bc = int(input("Masukan akhir deret: "))

for i in range(ab,bc):
    if i % 2 == 0:
        if i % 5 != 0 and i % 9 != 0:print(i, end=" ")
