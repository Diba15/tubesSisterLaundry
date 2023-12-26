import paho.mqtt.client as mqtt
import time
import datetime

# Dapatkan waktu saat ini
current_time = datetime.datetime.now()


def on_message(client, userdata, message):
    print(
        f"Pesanan Laundry {message.topic} dengan penjemputan baju kotor {current_time.strftime('%Y-%m-%d %H:%M:%S')} dan perkiraan pengantaran {message.payload.decode()}")


# def on_publish(client, userdata, mid):
#     print("Message {} published.".format(mid))


# alamat broker yang akan digunakan
broker_address = "0.tcp.ap.ngrok.io"
# buat client bernama P1
print("creating new instance")
client = mqtt.Client()
# pada client dikaitkan callback function
client.on_message = on_message
# client.on_publish = on_publish
# client terkoneksi dengan broker
print("connecting to broker")
client.connect(broker_address, port=19536)
client.loop_start()
print("""
        ====================[M E N U]====================
        Pilih Laundry yang ingin digunakan
        1. Laundry Bojong (Pengantaran 1 Hari)
        2. Laundry Soang (Pengantaran 2 Hari)
        =================================================
        """)
inputUser = input('Masukkan pilihan: ')

topik = ""
if inputUser == '1':
    print("Mengikuti Laundry", "Bojong")
    topik = "Bojong"
elif inputUser == '2':
    print("Mengikuti Laundry", "Soang")
    topik = "Soang"

client.subscribe(topik)

if inputUser == '1':
    pesan = (current_time + datetime.timedelta(days=1)).strftime("%Y-%m-%d %H:%M:%S")
    client.publish(topik, pesan)
elif inputUser == '2':
    pesan = (current_time + datetime.timedelta(days=2)).strftime("%Y-%m-%d %H:%M:%S")
    client.publish(topik, pesan)

time.sleep(30)

client.loop_stop()
