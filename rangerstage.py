from MainFunc import run_for_minutes
import pyautogui
import time
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