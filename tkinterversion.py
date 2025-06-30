import tkinter as tk
from tkinter import messagebox
import threading
import pyautogui
import time
from datetime import datetime, timedelta

# === ใส่ฟังก์ชันทั้งหมดของคุณที่นี่ (ยกมาจากโค้ดเดิม) ===
# (เพื่อให้สั้น ผมไม่แปะทั้งหมดซ้ำ แต่คุณควรวางทุกฟังก์ชันไว้ที่นี่)
# ตัวอย่าง:
def replay():
    pyautogui.click(413, 203)
    time.sleep(0.5)
    pyautogui.click(260, 455)
    time.sleep(0.5)

# ใส่ฟังก์ชันอื่น ๆ ตรงนี้ให้ครบ เช่น out(), run_for_minutes(), entervoocha(), ...
# และ fullauto(), fullauto2(), rangerstage(), ฯลฯ

def start_fullauto():
    threading.Thread(target=fullauto).start()

def start_fullauto2():
    threading.Thread(target=fullauto2).start()

def start_rangerGhoul():
    threading.Thread(target=rangerGhoul).start()

def start_easter():
    threading.Thread(target=easter).start()

# === สร้างหน้าจอ GUI ด้วย Tkinter ===
root = tk.Tk()
root.title("Auto Farming Launcher")
root.geometry("400x300")

label = tk.Label(root, text="เลือกรูปแบบการทำงาน", font=("TH Sarabun New", 16))
label.pack(pady=20)

btn1 = tk.Button(root, text="เริ่ม Full Auto", width=30, command=start_fullauto)
btn1.pack(pady=5)

btn2 = tk.Button(root, text="เริ่ม Full Auto V2", width=30, command=start_fullauto2)
btn2.pack(pady=5)

btn3 = tk.Button(root, text="เริ่มฟาร์ม Ghoul", width=30, command=start_rangerGhoul)
btn3.pack(pady=5)

btn4 = tk.Button(root, text="ฟาร์ม Easter Event", width=30, command=start_easter)
btn4.pack(pady=5)

btn_quit = tk.Button(root, text="ออกจากโปรแกรม", width=30, command=root.quit)
btn_quit.pack(pady=20)

root.mainloop()
