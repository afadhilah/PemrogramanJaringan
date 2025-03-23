# Baca input dari user
N = int(input("Masukkan bilangan non-negatif: "))

# Pastikan N adalah non-negatif
if N < 0:
    print("Input harus bilangan non-negatif.")
else:
    # Konversi ke biner dan cetak (tanpa prefix '0b')
    print(bin(N)[2:])
