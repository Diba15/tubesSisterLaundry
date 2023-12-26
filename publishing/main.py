import paho.mqtt.client as mqtt
import time
import datetime


def on_message(client, userdata, message):
    print('Info Waktu:', str(message.payload.decode("utf-8")))


def get_laundry_choice():
    print("""
        ====================[M E N U]====================
        Pilih Laundry yang ingin digunakan
        1. Laundry Bojong
        2. Laundry Soang
        =================================================
        """)
    return input('Masukkan pilihan: ')


def get_service_type():
    print("""
===========[Jenis Laundry]==========
Pilih jenis laundry:
1. Cuci Basah
2. Cuci Kering
===================================
""")
    return input('Masukkan pilihan         : ')


def get_processing_time(service_type):
    if service_type == '1':  # Jika cuci basah
        print(f"============[Waktu Pengerjaan Cuci Basah]===========")
        print("Pilih waktu pengerjaan:")
        print("1. 1 Hari (Rp 9.000/kg)")
        print("2. 2 Hari (Rp 8.000/kg)")
        print("3. 3 Hari (Rp 7.000/kg)")
        print("=====================================================")
    elif service_type == '2':  # Jika cuci kering
        print(f"===========[Waktu Pengerjaan Cuci Kering]===========")
        print("Pilih waktu pengerjaan:")
        print("1. 1 Hari (Rp 8.000/kg)")
        print("2. 2 Hari (Rp 7.000/kg)")
        print("3. 3 Hari (Rp 6.000/kg)")
        print("=====================================================")
    return input('Pilih waktu pengerjaan   : ')


def get_customer_details():
    name = input("Masukkan nama Anda       : ")
    weight = float(input("Masukkan total berat (kg): "))
    return name, weight


broker_address = "0.tcp.ap.ngrok.io"
print("Creating new instance")
client = mqtt.Client("Musrik")
client.on_message = on_message
print("Connecting to broker")
client.connect(broker_address, port=19536)
client.loop_start()

laundry_choice = get_laundry_choice()
if laundry_choice == '1':
    print("Mengikuti Laundry Bojong")
    client.subscribe("bojong")
elif laundry_choice == '2':
    print("Mengikuti Laundry Soang")
    client.subscribe("soang")

client.loop_stop()

service_type = get_service_type()
processing_time_choice = get_processing_time(service_type)

# Mempersiapkan data pelanggan
customer_name, total_weight = get_customer_details()

# Logika untuk perhitungan harga dan waktu
price_per_kg = 0
if service_type == '1':  # Jika cuci basah
    if processing_time_choice == '1':
        price_per_kg = 9000
    elif processing_time_choice == '2':
        price_per_kg = 8000
    elif processing_time_choice == '3':
        price_per_kg = 7000
elif service_type == '2':  # Jika cuci kering
    if processing_time_choice == '1':
        price_per_kg = 8000
    elif processing_time_choice == '2':
        price_per_kg = 7000
    elif processing_time_choice == '3':
        price_per_kg = 6000

total_price = price_per_kg * total_weight

# Dapatkan waktu saat ini
current_time = datetime.datetime.now()

print("===========================================================================")
print(f"Detail Pesanan\nNama Pelanggan    : {customer_name}\nJenis Laundry     : {'Cuci Basah' if service_type == '1' else 'Cuci Kering'}"
      f"\nTotal Berat       : {total_weight} kg\nTotal Harga       : Rp {total_price}")
print("===========================================================================")

client.publish("waktu_penjemputan", current_time.strftime("%Y-%m-%d %H:%M:%S"))
print(f"Pengambilan Baju di Laundry {'Bojong' if laundry_choice == '1' else 'Soang'} pada waktu:", current_time.strftime("%Y-%m-%d %H:%M:%S"))

delivery_time = current_time + datetime.timedelta(days=int(processing_time_choice))
client.publish("waktu_pengantaran", delivery_time.strftime("%Y-%m-%d %H:%M:%S"))
print(f"Pengantaran Baju di Laundry {'Bojong' if laundry_choice == '1' else 'Soang'} pada waktu:", delivery_time.strftime("%Y-%m-%d %H:%M:%S"))
print("===========================================================================")
