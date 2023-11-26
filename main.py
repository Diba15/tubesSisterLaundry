# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def menu():
    print('Pilih Laundry yang mau digunakan: ')
    print('1. Laundry Bojong')
    print('2. Laundry Soang')
    print('3. Exit')
    inputUser = input('Masukkan pilihan: ')
    if inputUser == '1':
        print('Laundry Bojong')
        print('1. Cuci Kering')
        print('2. Cuci Basah')
        print('3. Exit')
    elif inputUser == '2':
        print('Laundry Soang')
        print('1. Cuci Kering')
        print('2. Cuci Basah')
        print('3. Exit')
    elif inputUser == '3':
        print('Exit')
    else:
        print('Pilihan tidak ada')


if __name__ == '__main__':
    menu()

