#NOMOR 1
nilai=int(input("Masukkan Nilai : "))
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

#NOMOR 2
a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))
c = int(input("Masukkan angka ketiga: "))

if a >= b and a >= c:
    paling_besar = a
elif b >= a and b >= c:
    paling_besar = b
else:
    paling_besar = c

print("Angka terbesar adalah:", paling_besar)

#NOMOR 3 
n = int(input("Masukkan nilai n untuk Fibonacci: "))
a, b = 0, 1

print("Deret Fibonacci:")
while a <= n:
    print(a, end=" ")
    a, b = b, a + b
print()
