# import modulnya dulu
import random

# buat variabel bilangan_acak, diisi menggunakan modul random
# buat 1 sebagai batas minimal dan 7 sebagai batas maksimal dari angka random
bilangan_acak = random.randint(1, 7)

# buat variabel warna yang akan diisi nanti dari hasil random
warna = ''

# elif di sini adalah else if
if bilangan_acak == 1:
    warna = 'Merah'
elif bilangan_acak == 2:
    warna = 'Jingga'
elif bilangan_acak == 3:
    warna = 'Kuning'
elif bilangan_acak == 4:
    warna = 'Hijau'
elif bilangan_acak == 5:
    warna = 'Biru'
elif bilangan_acak == 6:
    warna = 'Nila'
elif bilangan_acak == 7:
    warna = 'Ungu'

# print hasilnya di konsol
print(f'Warna yang didapat adalah warna "{warna}"')
