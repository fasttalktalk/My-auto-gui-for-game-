# 🎮 Auto Farming Bot

สคริปต์ Python สำหรับทำงานอัตโนมัติ (Auto Farming) ในเกม Anime Sword Tower Defense / Anime Last Stand และเกมแนวเดียวกัน โดยใช้ `pyautogui` ในการควบคุมเมาส์และคีย์บอร์ดเพื่อจำลองการคลิกในตำแหน่งต่าง ๆ บนหน้าจอ

> ⚠️ **คำเตือน:** สคริปต์นี้ใช้พิกัด (x, y) แบบตายตัวบนหน้าจอ จึงต้องใช้ความละเอียดหน้าจอและตำแหน่งหน้าต่างเกมให้ตรงกับที่ตั้งค่าไว้

---

## 📂 โครงสร้างไฟล์

| ไฟล์ | คำอธิบาย |
|------|----------|
| `MainFunc.py` | รวมฟังก์ชันหลักทั้งหมด (ฟาร์ม Ranger Stage, Challenge, Ghoul, Easter, Reroll ฯลฯ) |
| `rangerstage.py` | สคริปต์เฉพาะสำหรับฟาร์ม Ranger Stage ทั้ง 5 ด่าน |
| `FullAutoRanger.py` | สคริปต์ Full Auto ที่ตั้งเวลาทำงานทุก ๆ นาทีที่ 16 และ 46 |
| `tkinterversion.py` | เวอร์ชัน GUI ใช้ Tkinter สำหรับเลือกโหมดการทำงาน |

---

## 🛠️ การติดตั้ง

### ความต้องการของระบบ
- Python 3.8 ขึ้นไป
- ระบบปฏิบัติการ Windows / macOS / Linux

### ติดตั้ง Dependencies

```bash
pip install pyautogui
```

> หมายเหตุ: `tkinter`, `datetime`, `time`, `sys`, `threading` เป็น Standard Library มาพร้อมกับ Python อยู่แล้ว

---

## 🚀 วิธีใช้งาน

### 1. Full Auto Ranger (ทำงานอัตโนมัติตามเวลา)

```bash
python FullAutoRanger.py
```

- จะรอจนถึงนาทีที่ 16 หรือ 46 ของชั่วโมง
- เมื่อถึงเวลาจะเริ่มฟาร์มทุกด่านอัตโนมัติ
- หลังจบครบทุกด่านจะออกจากเกม แล้ววนรอรอบถัดไป

### 2. Ranger Stage (ฟาร์มครั้งเดียว)

```python
from rangerstage import rangerstage
rangerstage()
```

ฟาร์มทั้ง 5 ด่านเรียงตามลำดับ:
1. 🏘️ Voocha Village (2.6 นาที)
2. 🌍 Green Planet (2.5 นาที)
3. 👹 Demon (2.5 นาที)
4. 🍃 Leaf (2.5 นาที)
5. 🏙️ Z City (2.5 นาที)

### 3. GUI Version

```bash
python tkinterversion.py
```

มีปุ่มให้เลือก 4 โหมด:
- เริ่ม Full Auto
- เริ่ม Full Auto V2
- เริ่มฟาร์ม Ghoul
- ฟาร์ม Easter Event

---

## 📖 รายละเอียดฟังก์ชันใน `MainFunc.py`

### ฟังก์ชันหลัก

| ฟังก์ชัน | หน้าที่ |
|----------|--------|
| `replay()` | กดปุ่มเล่นด่านซ้ำ |
| `out()` | ออกจากด่าน (มี countdown 60 วินาที) |
| `run_for_minutes(minutes)` | เรียก `replay()` วนซ้ำตามเวลาที่กำหนด |

### ฟังก์ชันเข้าด่าน Ranger Stage

| ฟังก์ชัน | ด่าน |
|----------|------|
| `entervoocha()` | Voocha Village |
| `entergreenplanet()` | Green Planet |
| `enterdemon()` | Demon |
| `enterleaf()` | Leaf Village |
| `enterzci()` | Z City |

### ฟังก์ชัน Full Auto

| ฟังก์ชัน | คำอธิบาย |
|----------|----------|
| `fullauto()` | ทำงานทุกชั่วโมงที่นาที .00 ฟาร์ม + Challenge |
| `fullauto2()` | เหมือน `fullauto()` แต่ปรับ logging ให้ละเอียดขึ้น |
| `enterchalenge()` | เข้าโหมด Challenge |

### ฟังก์ชันโหมดอื่น ๆ

| ฟังก์ชัน | คำอธิบาย |
|----------|----------|
| `rangerGhoul()` | ฟาร์มด่าน Ghoul (5 นาที) |
| `easter()` | ฟาร์ม Easter Event |
| `infinitecastle()` | เข้าโหมด Infinite Castle |
| `bossrush()` | ทำ Boss Rush อัตโนมัติ |

### ฟังก์ชัน Reroll

| ฟังก์ชัน | คำอธิบาย |
|----------|----------|
| `rerollstats(slot)` | Reroll stats ตาม slot (1-5) |
| `reroll()` | Reroll ทั่วไป |
| `alsreroll()` | Reroll สำหรับ Anime Last Stand |
| `astdx_reroll()` | Reroll สำหรับ ASTDX |
| `rereoll_traite_astdx()` | Reroll Trait ASTDX |
| `summon()` | กดปุ่ม Summon |

---

## ⚙️ การตั้งค่าพิกัด

พิกัด (x, y) ในสคริปต์ทั้งหมดเป็นแบบ **hardcoded** หากความละเอียดหรือตำแหน่งหน้าต่างเกมเปลี่ยน ต้องแก้ค่าใหม่

### วิธีหาพิกัดบนหน้าจอ

```python
import pyautogui
print(pyautogui.position())  # เลื่อนเมาส์ไปยังตำแหน่งที่ต้องการ แล้วรันคำสั่งนี้
```

หรือใช้ `pyautogui.mouseInfo()` เพื่อเปิด GUI ดูพิกัดแบบ real-time

---

## 🛑 วิธีหยุดสคริปต์ฉุกเฉิน

- **เลื่อนเมาส์ไปมุมซ้ายบนของจอ** → `pyautogui` จะ raise `FailSafeException` อัตโนมัติ
- หรือกด `Ctrl + C` ใน terminal

---

## ⚠️ ข้อควรระวัง

1. **พิกัดต้องตรงกับหน้าต่างเกม** — เปลี่ยน resolution หรือย้ายหน้าต่างเกมแล้วต้องตั้งใหม่
2. **อย่าขยับเมาส์ระหว่างสคริปต์ทำงาน** เพราะจะทำให้คลิกผิดที่
3. **ใช้ตามข้อกำหนดของเกม** — การใช้ bot อาจผิด ToS ของเกมและทำให้บัญชีถูกแบน
4. **มีจุด `while(True)` ในไฟล์ `MainFunc.py` ที่จะวน `rereoll_traite_astdx()` ตลอด** ถ้าไม่ต้องการ ให้คอมเมนต์บรรทัดท้ายไฟล์ออก

---

## 📝 TODO / ปรับปรุงในอนาคต

- [ ] ย้ายพิกัดทั้งหมดไปไว้ใน config file (เช่น `config.json` หรือ `.env`)
- [ ] เพิ่ม image recognition ด้วย `pyautogui.locateOnScreen()` แทนการใช้พิกัดตายตัว
- [ ] รวมโค้ดซ้ำใน `MainFunc.py` และ `rangerstage.py` ให้เป็นโมดูลเดียว
- [ ] เติมฟังก์ชันให้ครบใน `tkinterversion.py`
- [ ] เพิ่ม logging แทน `print()`
- [ ] รองรับหลาย resolution

---

## 📜 License

โปรเจคนี้ใช้สำหรับการศึกษาเท่านั้น โปรดใช้ตามความเสี่ยงของตัวเอง

---

