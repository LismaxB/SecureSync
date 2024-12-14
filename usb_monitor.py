import os
import platform
import psutil

def detect_usb_drives():
    usb_drives = []
    current_os = platform.system()
    if current_os == "Windows":
        partitions = psutil.disk_partitions()
        for partition in partitions:
            if 'removable' in partition.opts:
                usb_drives.append(partition.mountpoint)
    elif current_os == "Linux":
        usb_drives = [os.path.join("/media", d) for d in os.listdir("/media")]
    elif current_os == "Darwin":
        usb_drives = [os.path.join("/Volumes", d) for d in os.listdir("/Volumes")]
    else:
        print("Operating System not supported.")

    return usb_drives


def monitor_usb():
    print("Starting USB monitoring...")
    previously_detected = set(detect_usb_drives())

    try:
        while True:
            current_drives = set(detect_usb_drives())
            new_drives = current_drives - previously_detected
            past_drives = previously_detected - current_drives
            if new_drives:
                for drive in new_drives:
                    print(f"USB Drive Connected: {drive}")
            if past_drives:
                for drive in past_drives:
                    print(f"USB Drive Disconnected: {drive}")
            previously_detected = current_drives
    except KeyboardInterrupt:
        print("Stopping USB monitoring...")

if __name__ == "__main__":
    monitor_usb()
