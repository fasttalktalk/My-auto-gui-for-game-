import pyautogui
import time
from datetime import datetime, timedelta
import sys
from rangerstage import *

def fullauto():
    while True:
        now = datetime.now()
        minute = now.minute

        # หานาทีถัดไปที่เป็น 15 หรือ 45
        if minute < 15:
            next_run = now.replace(minute=15, second=0, microsecond=0)
        elif minute < 45:
            next_run = now.replace(minute=45, second=0, microsecond=0)
        else:
            # ข้ามไปชั่วโมงถัดไป นาทีที่ 15
            next_run = (now + timedelta(hours=1)).replace(minute=15, second=0, microsecond=0)

        wait_seconds = int((next_run - now).total_seconds())

        print(f"\n🕒 กำลังรอให้ถึงเวลา {next_run.strftime('%H:%M:%S')} (อีก {wait_seconds} วินาที)")

        while wait_seconds > 0:
            sys.stdout.write(f"\r⏳ รออีก {wait_seconds} วินาที...")
            sys.stdout.flush()
            time.sleep(1)
            wait_seconds -= 1

        print(f"\n⏰ ถึงเวลา {next_run.strftime('%H:%M:%S')} แล้ว!")

        # === เรียกทำงาน ===
        print(f"🔧 เริ่มทำงาน: {datetime.now().strftime('%H:%M:%S')}")
        rangerstage()
        out()


        

fullauto()
