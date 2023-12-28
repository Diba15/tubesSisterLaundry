# Import library yang dibutuhkan
import paho.mqtt.client as mqtt
import time
import datetime

# Dapatkan waktu saat ini
current_time = datetime.datetime.now()


# Callback function untuk menerima pesan
def on_message(client, userdata, message):
    print(
        f"Pesanan Laundry {message.topic} dengan pengambilan baju {current_time.strftime('%Y-%m-%d %H:%M:%S')} dan perkiraan pengantaran {message.payload.decode()}")


# Menerima data pilihan laundry
def get_laundry_choice():
    print("""
======================[M E N U]======================
Pilih Laundry yang ingin digunakan
1. Laundry Bojong
2. Laundry Soang
=====================================================
""")
    return input('Masukkan pilihan: ')


# Menerima data jenis laundry
def get_service_type():
    print("""
==================[Jenis Laundry]====================
Pilih jenis laundry:
1. Cuci Basah
2. Cuci Kering
=====================================================
""")
    return input('Masukkan pilihan         : ')


# Menerima data waktu pengerjaan
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


# Menerima data pelanggan
def get_customer_details():
    name = input("Masukkan nama Anda       : ")
    weight = float(input("Masukkan total berat (kg): "))
    return name, weight


# Membuat koneksi ke broker
broker_address = "0.tcp.ap.ngrok.io"
print("Creating new instance")
client = mqtt.Client()
# Set callback function on_message
client.on_message = on_message
# Connect ke broker
print("Connecting to broker")
client.connect(broker_address, port=18017)
# Start loop
client.loop_start()

# Pilih laundry
laundry_choice = get_laundry_choice()
topik = ""
if laundry_choice == '1':
    print("Mengikuti Laundry Bojong")
    topik = "Bojong"
elif laundry_choice == '2':
    print("Mengikuti Laundry Soang")
    topik = "Soang"

# Subscribe ke topik
client.subscribe(topik)

# Mempersiapkan data laundry
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

# Menghitung total harga
total_price = price_per_kg * total_weight

# Menampilkan detail pesanan
print("===========================================================================")
print(
    f"Detail Pesanan\nNama Pelanggan    : {customer_name}\nJenis Laundry     : {'Cuci Basah' if service_type == '1' else 'Cuci Kering'}"
    f"\nTotal Berat       : {total_weight} kg\nTotal Harga       : Rp {total_price}")
print("===========================================================================")

# Publish pesan ke topik
pesan = (current_time + datetime.timedelta(days=int(processing_time_choice))).strftime("%Y-%m-%d %H:%M:%S")
client.publish(topik, pesan)

# Tunggu 30 detik
time.sleep(30)
# Stop loop
client.loop_stop()
