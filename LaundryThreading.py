import threading
import time


class Laundry:
    def __init__(self, name):
        self.name = name
        self.followers = set()
        self.orders = []
        self.lock = threading.Lock()

    def follow_client(self, client):
        with self.lock:
            self.followers.add(client)
            print(f"{client} sekarang anda mengikuti {self.name}")

    def send_pickup_info(self, client):
        date_pickup = time.strftime("%Y-%m-%d")
        time_pickup = time.strftime("%H:%M:%S")
        with self.lock:
            if client in self.followers:
                print("==============================================================\n")
                print(f"{self.name} Mengirim informasi penjempulan ke {client}\n")
                print(f"laundry {self.name} akan di ambil pada tanggal {date_pickup} pukul {time_pickup}\n")
                print("==============================================================")
            else:
                print(f"{client} anda tidak mengikuti {self.name}. Silakan ikuti untuk menerima pembaruan.")

    def send_delivery_info(self, client):
        date_delivery = time.strftime("%Y-%m-%d")  
        time_delivery = time.strftime("%H:%M:%S", time.localtime(time.time() + 7200))# 2 hours later
        with self.lock:
            if client in self.followers:
                print(f"{self.name} Mengirim informasi pengantaran ke {client}\n")
                print(f"laundry {self.name} akan di antar pada tanggal {date_delivery} pukul {time_delivery}\n")
                print("==============================================================")
            else:
                print(f"{client} anda tidak mengikuti {self.name}. Silakan ikuti untuk menerima pembaruan.")

    def add_order(self, order):
        with self.lock:
            self.orders.append(order)

    def get_orders(self):
        with self.lock:
            return self.orders


def client_thread(client, laundry):
    laundry.follow_client(client)
    laundry.send_pickup_info(client)
    time.sleep(3)  # Simulating laundry process time
    laundry.send_delivery_info(client)


if __name__ == "__main__":
    laundry_bojong = Laundry("Laundry Bojong")
    laundry_soang = Laundry("Laundry Soang")

    client1 = "Client A"
    client2 = "Client B"

    thread1 = threading.Thread(target=client_thread, args=(client1, laundry_bojong))
    thread2 = threading.Thread(target=client_thread, args=(client2, laundry_soang))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
