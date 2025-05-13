import pyautogui
import time
from datetime import datetime, timedelta
from rangerstage import *

def fullauto():
    #while True:
        now = datetime.now()

        # รอจนถึง .00
        next_hour = (now + timedelta(hours=1)).replace(minute=10, second=0, microsecond=0)
        if now.minute != 0 or now.second != 0:
            wait_seconds = (next_hour - now).total_seconds()
            print(f"รอจนถึงเวลา {next_hour} (อีก {wait_seconds:.0f} วินาที)")
            time.sleep(wait_seconds)
            rangerstage()
            
fullauto()
