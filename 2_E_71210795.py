#program menampilakan jadwal matakuliah  

ab = str(input("Hi Tutu, Silahkan Masukkan hari yang ingin Anda telusuri: "))

senin = ["Alogoritma Graf" , "Sistem Operasi" , "PAk" , "Praktikum INLAN"]
x = [1, 3, 4, 5]
selasa = ["Matematika Teknik" , "Bhs Indonesia" , "PKN"]
y = [2,4,6]
kamis = ["IMK" , "Logmat" , "Praktekkom"]
z = [1, 3, 4]
jumat = ["Sistem Basis Data" , "Praktikum Sistem Basis Data" , "INLAN"]
 
if ab == "senin":
    for j in range(len(senin)):
        print("Kelas ke-",x[j],senin[j])
elif ab == "selasa":
    for j in range(len(selasa)):
        print("Kelas ke-,",y[j],selasa[j])
elif ab == "rabu":
    print("Hari rabu Anda tidak ada kelas")
elif ab == "kamis":
    for j in range(len(kamis)):
        print("Kelas ke-",z[j],kamis[j])
elif ab == "jumat":
    for j in range(len(jumat)):
        print("Kelas ke-",y[j],jumat[j])
