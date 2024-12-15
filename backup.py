import shutil
import os

def auto_backup(source, destination):
    try:
        if not os.path.exists(destination):
            os.makedirs(destination)
            print(f"Starting Backup from {source}")
        for item in os.listdir(source):
            s = os.path.join(source, item)
            d = os.path.join(destination, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, dirs_exist_ok=True)
            else:
                shutil.copy2(s, d)
        print(f"Backup completed from {source} to {destination}")
    except Exception as e:
        print(f"Error during backup: {e}")
