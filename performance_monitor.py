import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_memory_usage():
    memory = psutil.virtual_memory()
    return memory.percent

def get_disk_usage():
    disk = psutil.disk_usage('/')
    return disk.percent

while True:
    cpu = get_cpu_usage()
    memory = get_memory_usage()
    disk = get_disk_usage()

    print(f"CPU Usage: {cpu}%\nMemory Usage: {memory}%\nDisk Usage: {disk}%\n")
    time.sleep(60)
