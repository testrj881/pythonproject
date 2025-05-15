#2. TO MONITOR SYSTEM'S CPU, MEMORY, AND DISK USAGE
#ref: https://www.youtube.com/watch?v=B0p0VbgKkf0
import psutil
import time

def monitor_resources(cpu_threshold, mem_threshold, disk_threshold):
    while True:
        cpu_usage = psutil.cpu_percent(interval=1)
        mem_usage = psutil.virtual_memory().percent
        disk_usage = psutil.disk_usage('/').percent

        if cpu_usage > cpu_threshold:
            print(f"CPU usage at {cpu_usage}% exceeds threshold of {cpu_threshold}%")

        if mem_usage > mem_threshold:
            print(f"Memory usage at {mem_usage}% exceeds threshold of {mem_threshold}%")

    if disk_usage > disk_threshold:
        print(f"Disk usage at {disk_usage}% exceeds threshold of {disk_threshold}%")
    time.sleep(60)


