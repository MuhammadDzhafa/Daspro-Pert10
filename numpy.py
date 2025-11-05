import numpy as np

keuntungan = np.array([2.5, 3.1, 1.8, 4.0, 3.7, 2.9, 5.2, 4.8, 3.5, 2.6, 4.3, 5.0, 3.2, 4.6])

rata_rata = np.mean(keuntungan)

maks = np.max(keuntungan)
minim = np.min(keuntungan)

hari_maks = np.argmax(keuntungan) + 1
hari_min = np.argmin(keuntungan) + 1

print("Keuntungan 14 hari terakhir (juta rupiah):")
print(keuntungan)
print("\nRata-rata keuntungan:", round(rata_rata, 2), "juta rupiah")
print("Keuntungan tertinggi :", maks, "juta rupiah (hari ke-", hari_maks, ")")
print("Keuntungan terendah  :", minim, "juta rupiah (hari ke-", hari_min, ")")
