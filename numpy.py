import numpy as np

# Data keuntungan dalam juta rupiah selama 14 hari
keuntungan = np.array([2.5, 3.1, 1.8, 4.0, 3.7, 2.9, 5.2, 4.8, 3.5, 2.6, 4.3, 5.0, 3.2, 4.6])

# Statistik dasar
rata_rata = np.mean(keuntungan)
maks = np.max(keuntungan)
minim = np.min(keuntungan)
total = np.sum(keuntungan)

hari_maks = np.argmax(keuntungan) + 1
hari_min = np.argmin(keuntungan) + 1

# Menampilkan hasil
print("=" * 50)
print("LAPORAN KEUNTUNGAN 14 HARI TERAKHIR")
print("=" * 50)

print("\nData Keuntungan (juta rupiah):")
print(keuntungan)

print(f"\nTotal Keuntungan     : {total:.2f} juta rupiah")
print(f"Rata-rata Keuntungan : {rata_rata:.2f} juta rupiah")
print(f"Keuntungan Tertinggi : {maks} juta rupiah (hari ke-{hari_maks})")
print(f"Keuntungan Terendah  : {minim} juta rupiah (hari ke-{hari_min})")

# Tambahan: tampilkan hari-hari di atas rata-rata
hari_di_atas_rata2 = np.where(keuntungan > rata_rata)[0] + 1
print(f"\nHari dengan keuntungan di atas rata-rata: {hari_di_atas_rata2}")
