# import modulnya dulu
import random

# 3 variabel untuk nomor keberuntungan, mulai dari 100 agar selalu 3 digit angka
nomor_1 = random.randint(100, 999)
nomor_2 = random.randint(100, 999)
nomor_3 = random.randint(100, 999)

# 2 variabel untuk teks kutipan dan nomor random untuk memilih kutipan
kutipan = ''
pilihan_kutipan = random.randint(1, 3)

# generate random kutipan
if pilihan_kutipan == 1:
    kutipan = '''
        "The only thing we have to fear is fear itself."

        - Franklin D. Roosevelt
    '''
elif pilihan_kutipan == 2:
    kutipan = '''
        "To be yourself in a world that is constantly trying to make you something else is the greatest accomplishment."

        - Ralph Waldo Emerson
    '''
elif pilihan_kutipan == 3:
    kutipan = '''
        "In three words I can sum up everything I`ve learned about life: it goes on."

        - Robert Frost
    '''

# print hasilnya di konsol
print(f'''
    Kutipan hari ini:
        {kutipan}

    Nomor keberuntungan Anda :

        ┌-------------┐
        | {nomor_1}-{nomor_2}-{nomor_3} |
        └-------------┘
''')
