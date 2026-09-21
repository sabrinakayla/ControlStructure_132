nilai=float(input("Masukkan Nilai : "))
if nilai >= 90 :
    print("Excellent performance")
elif nilai >= 80 :
    print("Very Good performance")
elif nilai >= 70 :
    print("Good performance")
elif nilai >= 60 :
    print("average performance")
else :
    print("Silahkan Belajar Lagi")

a = float(input("Masukkan angka pertama: "))
b = float(input("Masukkan angka kedua: "))
c = float(input("Masukkan angka ketiga: "))

if a >= b and a >= c:
    paling_besar = a
elif b >= a and b >= c:
    paling_besar = b
else:
    paling_besar = c

print("Angka terbesar adalah:", paling_besar)