import colorama  # type: ignore
from colorama import Fore, Back, Style  # type: ignore
colorama.init(autoreset=True)

harga_tier1 = {
    'wheat': 6, 'seed': 3, 'carrot': 3, 'potato': 3,
    'pumpkin': 10, 'melon': 2, 'cocoa bean': 3, 'sugar cane': 4,
    'cactus': 4, 'nether wart': 4, 'red mushroom': 10, 'brown mushroom': 10,
}

harga_tier2 = {
    'wheat': 960, 'seed': 480, 'carrot': 480, 'potato': 480,
    'pumpkin': 1600, 'melon': 320, 'cocoa bean': 480, 'sugar': 640,
    'cactus': 640, 'nether wart': 640, 'red mushroom': 1600, 'brown mushroom': 1600,
}

harga_tier3 = {
    'wheat': 153600, 'seed': 76800, 'carrot': 61440, 'potato': 76800,
    'pumpkin': 256000, 'melon': 51200, 'cocoa bean': 61500, 'sugar cane': 102400,
    'cactus': 102400, 'nether wart': 102400, 'red mushroom': 51200, 'brown mushroom': 51200,
}


def log(hasil):
    print(Fore.LIGHTYELLOW_EX + Style.BRIGHT + f'Total profit adalah {hasil} coin')


def stack():
    while True:
        print(Fore.CYAN + '[➕]----- Konversi Stack -----[➖]')
        print('[+] Angka ke Stack')
        print('[-] Stack ke Angka')
        print('[q] Kembali')
        action = input('Pilih tipe konversi: ')
        if action == '+':
            try:
                angka = int(input('Masukkan jumlah angka: '))
                stack = angka / 64
                print(Fore.LIGHTCYAN_EX + f'{angka} sama dengan {stack} stack')
            except ValueError:
                print(Fore.RED + 'Masukkan perintah yang valid!')
        elif action == '-':
            try:
                stack = int(input('Masukkan jumlah stack: '))
                angka = stack * 64
                print(Fore.LIGHTCYAN_EX + f'{stack} stack sama dengan {angka}')
            except ValueError:
                print(Fore.RED + 'Masukkan perintah yang valid!')
        elif action == 'q':
            break
        else:
            print(Fore.RED + 'Masukkan perintah yang valid!')


def list_crop():
    while True:
        print(Fore.GREEN + "[🧺]----- List Crop -----[🧺]")
        for crop in harga_tier1:
            print(crop)
        keluar = input('ketik [q] untuk kembali: ')
        if keluar == 'q':
            break
        else:
            print(Fore.RED + 'perintah salah')


def tier(tier_dict):
        pilihan = input('masukkan nama crop: ').lower()
        if pilihan in tier_dict:
            crop = tier_dict[pilihan]
            try:
                jumlah = int(input(f'masukkan jumlah {pilihan}: '))
                total_harga = crop * jumlah
                log(total_harga)
            except ValueError:
                print(Fore.RED + 'Masukkan angka yang valid!')
        else:
            print(Fore.RED + 'pastikan nama crop sesuai dengan di list')


def menu():
    while True:
        print(Fore.GREEN + Style.BRIGHT + '[🏡]====== HYFARM ======[🏡]')
        print('[?] List crop')
        print('[!] Hitung crop')
        print('[=] Konversi Stack')
        print('[x] Keluar')
        action = input('Kamu mau apa?: ').lower()

        if action == '?':
            list_crop()
        elif action == '!':
            try:
                print(Fore.GREEN + '[🌾]----- Hitung crop -----[🌾]')
                tier_num = int(input('masukkan tier crop [1/2/3]: '))
                if tier_num == 1:
                    tier(harga_tier1)
                elif tier_num == 2:
                    tier(harga_tier2)
                elif tier_num == 3:
                    tier(harga_tier3)
                else:
                    print(Fore.RED + 'tier tidak diketahui')
            except ValueError:
                print(Fore.RED + 'Masukkan angka tier yang valid!')
        elif action == 'x':
            print('Sampai jumpa!')
            break
        elif action == '=':
            stack()
        else:
            print(Fore.RED + 'Perintah tidak diketahui!')


menu()
