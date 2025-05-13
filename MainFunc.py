import pyautogui
import time
from datetime import datetime, timedelta
import sys
a = pyautogui.position()
print(a)

def out():
    # ⏳ Countdown 60 วินาทีก่อนเริ่มคลิก
    wait_time = 60
    print(f"⏱️ กำลังรอ {wait_time} วินาทีก่อนออก")
    for i in range(wait_time, 0, -1):
        print(f"⏳ ออกจากในอีก {i} วินาที", end='\r')
        time.sleep(1)
    print()

    # 🖱️ คลิกตำแหน่งต่าง ๆ
    for _ in range(5):
        pyautogui.click(391, 342)
        time.sleep(1)

    pyautogui.click(422, 452)
    time.sleep(1)
    pyautogui.click(422, 452)

    # ⏳ Countdown 15 วินาทีหลังสุด
    final_wait = 20
    print(f"🕒 รอ {final_wait} วินาทีก่อนจบขั้นตอน out()")
    for i in range(final_wait, 0, -1):
        print(f"⏳ เหลืออีก {i} วินาที...", end='\r')
        time.sleep(1)
    print("\n✅ ขั้นตอน out() เสร็จเรียบร้อยแล้ว")
    
def replay():
    pyautogui.click(413, 203)
    time.sleep(0.5)
    pyautogui.click(277, 455)
    time.sleep(0.5)


def run_for_minutes(minutes):
    total_seconds = int(minutes * 60)
    end_time = datetime.now() + timedelta(seconds=total_seconds)

    print(f"▶️ เริ่มทำงานเป็นเวลา {minutes} นาที ({total_seconds} วินาที)")
    
    while datetime.now() < end_time:
        remaining = int((end_time - datetime.now()).total_seconds())
        mins, secs = divmod(remaining, 60)
        print(f"⏳ เหลือเวลา {mins:02d}:{secs:02d}", end='\r')

        replay()

    print("\n✅ ทำงานครบแล้ว!")
def entervoocha():
    time.sleep(1)
    pyautogui.click(379, 345) #หน้าจอ
    time.sleep(1)
    pyautogui.click(72, 381) #ปุ่ม play
    time.sleep(1)
    pyautogui.click(72, 281) #Create Room
    time.sleep(1)
    pyautogui.click(474, 521) #ranger stage
    time.sleep(1)
    pyautogui.click(235, 229) #Voocha Village
    time.sleep(1)
    pyautogui.click(477, 464) #create
    time.sleep(1)
    pyautogui.click(417, 529) #start 
    time.sleep(1)
def entergreenplanet():
    time.sleep(1)
    pyautogui.click(379, 345) #หน้าจอ
    time.sleep(1)
    pyautogui.click(72, 381) #ปุ่ม play
    time.sleep(1)
    pyautogui.click(72, 281) #Create Room
    time.sleep(1)
    pyautogui.click(474, 521) #ranger stage
    time.sleep(1)
    pyautogui.click(237, 289) #Voocha Village
    time.sleep(1)
    pyautogui.click(477, 464) #create
    time.sleep(1)
    pyautogui.click(417, 529) #start 
    time.sleep(1)
def enterdemon():
    time.sleep(1)
    pyautogui.click(379, 345) #หน้าจอ
    time.sleep(1)
    pyautogui.click(72, 381) #ปุ่ม play
    time.sleep(1)
    pyautogui.click(72, 281) #Create Room
    time.sleep(1)
    pyautogui.click(474, 521) #ranger stage
    time.sleep(1)
    pyautogui.click(244, 352) #Voocha Village
    time.sleep(1)
    pyautogui.click(477, 464) #create
    time.sleep(1)
    pyautogui.click(417, 529) #start 
    time.sleep(1)
def enterleaf():
    time.sleep(1)
    pyautogui.click(379, 345) #หน้าจอ
    time.sleep(1)
    pyautogui.click(72, 381) #ปุ่ม play
    time.sleep(1)
    pyautogui.click(72, 281) #Create Room
    time.sleep(1)
    pyautogui.click(474, 521) #ranger stage
    time.sleep(1)
    pyautogui.click(253, 418) #Voocha Village
    time.sleep(1)
    pyautogui.click(477, 464) #create
    time.sleep(1)
    pyautogui.click(417, 529) #start 
    time.sleep(1)
def enterzci():
    time.sleep(1)
    pyautogui.click(379, 345) #หน้าจอ
    time.sleep(1)
    pyautogui.click(72, 381) #ปุ่ม play
    time.sleep(1)
    pyautogui.click(72, 281) #Create Room
    time.sleep(1)
    pyautogui.click(474, 521) #ranger stage
    time.sleep(1)
    pyautogui.click(223, 452) #Voocha Village
    time.sleep(1)
    pyautogui.click(477, 464) #create
    time.sleep(1)
    pyautogui.click(417, 529) #start 
    time.sleep(1)
def rangerstage():
    print('เข้าด่าน voocha')
    entervoocha()
    time.sleep(20)
    print('กำลังฟาร์มด่าน voocha')
    run_for_minutes(2.6)
    time.sleep(5)
    print('เข้าด่าน Green planet')
    entergreenplanet()
    time.sleep(20)
    print('กำลังฟาร์มด่าน Green planet')
    run_for_minutes(2.5)
    time.sleep(5)
    print('เข้าด่าน demon')
    enterdemon()
    time.sleep(20)
    print('กำลังฟาร์มด่าน Demon')
    run_for_minutes(2.5)
    time.sleep(5)
    print('เข้าด่าน leaf')
    enterleaf()
    time.sleep(20)
    print('กำลังฟาร์มด่าน leaf')
    run_for_minutes(2.5)
    time.sleep(5)
    print('เข้าด่าน z city')
    enterzci()
    time.sleep(20)
    print('กำลังฟาร์มด่าน z city')
    run_for_minutes(2.5)
    time.sleep(5)
def enterchalenge():
    pyautogui.click(505, 392)
    time.sleep(2)
    pyautogui.click(38, 433)
    time.sleep(2)
    pyautogui.click(447, 412)
    time.sleep(4)
    pyautogui.keyDown('a')
    time.sleep(2)
    pyautogui.click(352, 380)
    time.sleep(2)
    pyautogui.click(507, 634)
    time.sleep(2)

def fullauto(): 
    while True:
        now = datetime.now()

        # รอจนถึง .00
        next_hour = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
        if now.minute != 0 or now.second != 0:
            wait_seconds = (next_hour - now).total_seconds()
            print(f"รอจนถึงเวลา {next_hour} (อีก {wait_seconds:.0f} วินาที)")
            time.sleep(wait_seconds)

        # เมื่อถึง .00
        rangerstage()
        out()
        time.sleep(10)
        enterchalenge()
        # วน enterchalenge() + replay() จนถึง .58
        while True:
            now = datetime.now()
            if now.minute >= 57:
                print(f"ถึงเวลา {now}, หยุดรอ .00 ของชั่วโมงถัดไป...")
                out()
                break
            replay()
            time.sleep(0.5)  # ปรับระยะเวลาได้ตามต้องการ
def fullauto2():

    while True:
        now = datetime.now()

        # === 1. รอจนถึงเวลา .00 ===
        next_hour = (now + timedelta(hours=1)).replace(minute=0, second=0, microsecond=0)
        if now.minute != 0 or now.second != 0:
            wait_seconds = int((next_hour - now).total_seconds())
            print(f"\n🕒 กำลังรอให้ถึงเวลา {next_hour.strftime('%H:%M:%S')} (อีก {wait_seconds} วินาที)")
            while wait_seconds > 0:
                sys.stdout.write(f"\r⏳ รออีก {wait_seconds} วินาที...")
                sys.stdout.flush()
                time.sleep(1)
                wait_seconds -= 1
            print("\n⏰ ถึงเวลาแล้ว!")

        # === 2. ถึงเวลา .00: เริ่มกระบวนการหลัก ===
        print(f"\n🔧 เริ่มทำงานตอน {datetime.now().strftime('%H:%M:%S')}")
        rangerstage()

        print("⏱️ รอ 10 วินาทีก่อนเริ่ม enterchalenge()...")
        time.sleep(10)

        print("🚀 เรียกใช้ enterchalenge()")
        enterchalenge()

        # === 3. วน replay() เรื่อย ๆ จนถึงนาทีที่ 54 ===
        print("🔄 เริ่มวน replay() จนถึงนาที 54")
        while True:
            now = datetime.now()
            if now.minute >= 56:
                print(f"\n🛑 ถึงเวลา {now.strftime('%H:%M:%S')} หยุดวน replay() และรอรอบถัดไป")
                out()
                break
            print(f"🎮 กำลัง replay()... ({now.strftime('%H:%M:%S')})")
            replay()
            time.sleep(0.5)
def easter():
    pyautogui.click(428, 202)
    time.sleep(0.5)
    pyautogui.click(266, 437)
    time.sleep(0.5)
    for i in range(7):
        pyautogui.click(715, 252)
        time.sleep(0.3)
    time.sleep(0.5)
    pyautogui.click(716, 329)
    time.sleep(0.5)

