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
            print(f"{client} is now following {self.name}")

    def send_pickup_info(self, client):
        pickup_time = time.strftime("%Y-%m-%d %H:%M:%S")
        with self.lock:
            if client in self.followers:
                print(f"{self.name} sends pickup info to {client}: Your laundry will be picked up at {pickup_time}")
            else:
                print(f"{client} is not following {self.name}. Please follow to receive updates.")

    def send_delivery_info(self, client):
        delivery_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 7200))  # 2 hours later
        with self.lock:
            if client in self.followers:
                print(f"{self.name} sends delivery info to {client}: Your laundry will be delivered at {delivery_time}")
            else:
                print(f"{client} is not following {self.name}. Please follow to receive updates.")

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
