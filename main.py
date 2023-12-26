from LaundryThreading import Laundry
import time

def menu():
    laundry_bojong = Laundry("Laundry Bojong")
    laundry_soang = Laundry("Laundry Soang")
    

    print("""
        ====================[M E N U]====================
        Pilih Laundry yang mau digunakan
        1. Laundry Bojong
        2. Laundry Soang
        3. Exit
        =================================================
        """)
    inputUser = input('Masukkan pilihan: ')
    
    if inputUser == '1':
        print("""
        ================[Laundry Bojong]=================
        Pilih Laundry yang mau digunakan
        1. Cuci Kering
        2. Cuci Basah
        3. Exit
        =================================================
        """)
        laundry_action = input('Masukkan pilihan: ')
        if laundry_action == '1':
            client_name = input('Masukkan nama Anda: ')
            laundry_bojong.follow_client(client_name)
            laundry_bojong.send_pickup_info(client_name)
            time.sleep(3) 
            laundry_bojong.send_delivery_info(client_name)
        elif laundry_action == '2':
            # Tindakan untuk Cuci Basah di Laundry Bojong
            pass
        elif laundry_action == '3':
            print('Exit')
        else:
            print('Pilihan tidak ada')

    elif inputUser == '2':
        print(
        """=================[Laundry Soang]=================
        Pilih Laundry yang mau digunakan
        1. Cuci Kering
        2. Cuci Basah
        3. Exit
        =================================================
        """)
        laundry_action = input('Masukkan pilihan: ')
        if laundry_action == '1':
            client_name = input('Masukkan nama Anda: ')
            laundry_soang.follow_client(client_name)
            laundry_soang.send_pickup_info(client_name)
            time.sleep(3)  # Simulating laundry process time
            laundry_soang.send_delivery_info(client_name)
        elif laundry_action == '2':
            # Tindakan untuk Cuci Basah di Laundry Soang
            pass
        elif laundry_action == '3':
            print('Exit')
        else:
            print('Pilihan tidak ada')

    elif inputUser == '3':
        print('Exit')
    else:
        print('Pilihan tidak ada')

if __name__ == '__main__':
    menu()
