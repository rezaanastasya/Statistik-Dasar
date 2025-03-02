# Dataset nilai ujian matematika
nilai_matematika = [85, 90, 78, 92, 88, 85, 90]

# Menghitung Median (Nilai Tengah)
sorted_nilai = sorted(nilai_matematika)
n = len(sorted_nilai)
if n % 2 == 1:  # Jika jumlah data ganjil
    median = sorted_nilai[n // 2]
else:  # Jika jumlah data genap
    median = (sorted_nilai[n // 2 - 1] + sorted_nilai[n // 2]) / 2
print("Median nilai ujian matematika:", median)
