import paho.mqtt.client as mqtt
import time
import datetime


def on_message(client, userdata, message):
    print('Info Waktu:', str(message.payload.decode("utf-8")))


# alamat broker yang akan digunakan
broker_address = "0.tcp.ap.ngrok.io"
# buat client bernama P1
print("creating new instance")
client = mqtt.Client("Musrik")
# pada client dikaitkan callback function
client.on_message = on_message
# client terkoneksi dengan broker
print("connecting to broker")
client.connect(broker_address, port=19536)
# client P1 mulai
client.loop_start()
# client P1 subscribe ke topik "info_waktu" # P1 <- broker
print("""
        ====================[M E N U]====================
        Pilih Laundry yang ingin digunakan
        1. Laundry Bojong
        2. Laundry Soang
        =================================================
        """)
inputUser = input('Masukkan pilihan: ')

if inputUser == '1':
    print("Mengikuti Laundry", "Bojong")
    client.subscribe("waktu_penjemputan_bojong")
    client.subscribe("waktu_pengantaran_bojong")
elif inputUser == '2':
    print("Mengikuti Laundry", "Soang")
    client.subscribe("waktu_penjemputan_soang")
    client.subscribe("waktu_pengantaran_soang")


client.loop_stop()

# Dapatkan waktu saat ini
current_time = datetime.datetime.now()

if inputUser == '1':
    client.publish("waktu_penjemputan_bojong", current_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Pengambilan Baju di Laundry Bojong pada waktu:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
    client.publish("waktu_pengantaran_bojong", (current_time + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(5)
    print("Pengantaran Baju di Laundry Bojong pada waktu:",
          (current_time + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S"))
elif inputUser == '2':
    client.publish("waktu_penjemputan_soang", current_time.strftime("%Y-%m-%d %H:%M:%S"))
    print("Pengambilan Baju di Laundry Soang pada waktu:", current_time.strftime("%Y-%m-%d %H:%M:%S"))
    time.sleep(5)
    client.publish("waktu_pengantaran_soang", (current_time + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S"))
    print("Pengantaran Baju di Laundry Soang pada waktu:",
          (current_time + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S"))
