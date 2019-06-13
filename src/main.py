import config
import os
from datetime import datetime
from ftplib import FTP

def timestamp():
    return datetime.now().strftime("%m-%d-%Y_%H:%M")

cfg = config.load_config()
ftp = FTP()
ftp.connect(host=cfg["server"]["host"], port=cfg["server"]["port"])
filename = os.path.join(cfg["backup_dir"], f"backup_{timestamp()}.zip")
ftp.login(user=cfg["server"]["username"], passwd=cfg["server"]["password"])
with open(filename, "wb") as outfile:
    print("Downloading file...")
    ftp.retrbinary(f"RETR {cfg['target_file']}", outfile.write)
ftp.quit()
