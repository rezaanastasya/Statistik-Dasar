# Dataset usia peserta seminar
usia_peserta = [25, 30, 25, 35, 40, 25, 30, 35, 25, 30]

# Menghitung Modus (Nilai yang paling sering muncul)
from collections import Counter
frekuensi = Counter(usia_peserta)
modus = max(frekuensi, key=frekuensi.get)
print("Modus usia peserta seminar:", modus)
