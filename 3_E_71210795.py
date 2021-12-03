#Program Bangun Datar Belah Ketupat
 
xyz = int(input("Masukan angka : "))
key =  xyz

for bintang in range (0,xyz):
    for pola in range (-2, key + 1):
         print(" ",end="")

    for shape in range (0, bintang + 1):
        print("* ", end="")
    key-=1
    print("")

key = xyz
for bintang in range (1,xyz):
    for pola in range (-4, bintang):
        print(" ",end="")

    for shape in range (1, key):
        print("* ",end="")
    key-=1
    print("")
