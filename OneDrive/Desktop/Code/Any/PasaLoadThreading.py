#Author Adrian Jude Tan
#Student No. 202110752

import threading
import multiprocessing
import time

# Shared variable representing the prepaid load balance
prepaid_load = multiprocessing.Value('i', 100)  # Initial load balance: 100

# Mutex lock for mutual exclusion
mutex = threading.Lock()

# Function to perform the pasaload transaction
def pasaload(sender, recipient, amount):
    global prepaid_load

    # Acquire the mutex lock to ensure exclusive access to shared data
    mutex.acquire()

    if prepaid_load.value >= amount:
        prepaid_load.value -= amount
        print(f"{sender} has successfully transferred {amount} load to {recipient}.")
    else:
        print(f"{sender} does not have sufficient load to perform the transaction.")

    # Release the mutex lock to allow other threads to access the shared data
    mutex.release()

# Function to simulate pasaload requests
def simulate_pasaload(sender, recipient, amount):
    pasaload(sender, recipient, amount)

# Create and start multiple threads representing pasaload requests
def run_threaded_pasaload():
    threads = []

    # Create 5 pasaload requests
    for i in range(5):
        sender = f"Sender{i+1}"
        recipient = f"Recipient{i+1}"
        amount = 20

        thread = threading.Thread(target=simulate_pasaload, args=(sender, recipient, amount))
        threads.append(thread)
        thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

# Create and start multiple processes representing pasaload requests
def run_multiprocess_pasaload():
    processes = []

    # Create 5 pasaload requests
    for i in range(5):
        sender = f"Sender{i+1}"
        recipient = f"Recipient{i+1}"
        amount = 20

        process = multiprocessing.Process(target=simulate_pasaload, args=(sender, recipient, amount))
        processes.append(process)
        process.start()

    # Wait for all processes to complete
    for process in processes:
        process.join()

# Main program
if __name__ == "__main__":
    # Run pasaload using threads
    print("PasaLoad using threads:")
    run_threaded_pasaload()
    print("")

    # Reset the prepaid load balance
    prepaid_load.value = 100

    # Run pasaload using processes
    print("PasaLoad using processes:")
    run_multiprocess_pasaload()
