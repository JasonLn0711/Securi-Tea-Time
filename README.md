# 🍵 Securi-Tea-Time

**Securi-Tea-Time** is an intelligent, lightweight, real-time security system that detects people and vehicles from a Xiaomi C400 CCTV feed. It mirrors an iPhone camera feed via QuickTime on macOS and uses YOLOv8 for object detection, OCR for license plate recognition, and clothing-color-based person re-identification. Events are logged automatically, snapshots are saved, and LINE notifications are sent with image attachments.

🚀 Developed by a graduate student at National Yang Ming Chiao Tung University (NYCU), this project offers a plug-and-play solution for home, remote work, and small-business security—using just a phone and laptop.

---

## 🧭 Table of Contents

- [📌 Overview](#-overview)
- [💎 Core Value of the Project](#-core-value-of-the-project)
- [🗂️ Project Structure](#-project-structure)
- [⚙️ Setup & Installation](#-setup--installation)
- [▶️ Usage](#-usage)
- [🏘️ Application Scenarios](#-application-scenarios)
- [📝 License](#-license)

---

## 📌 Overview

**Securi-Tea-Time** blends deep learning, computer vision, and automation into a cohesive real-time system:

- 🧠 **Real-time YOLOv8 detection** for people and vehicles
- 🧍 **Person re-ID** via clothing color (top/bottom)
- 🚘 **License plate recognition** using EasyOCR
- 📸 **Snapshot saving** with timestamps
- 📊 **CSV-based event logging** with object type, ID, time, and confidence
- 🔔 **LINE Notify integration** for real-time alerts with image attachments
- ⚡ **Optimized performance** via frame skipping, resizing, and MPS acceleration (macOS)

---

## 💎 Core Value of the Project

| 🏷️ Life Scenario               | 😟 Problem                                              | ✅ Solution & Value                                            |
|------------------------------|----------------------------------------------------------|---------------------------------------------------------------|
| 🏠 Home Security             | Undetected strangers entering the home                  | YOLO detection + LINE alerts + photo proof                   |
| 🅿️ Parking Management        | No license plate records                                | Plate OCR + searchable CSV history                           |
| 👤 Living Alone / Remote Work| No one to respond during emergencies                    | Real-time image alerts to LINE                               |
| 💸 Budget Constraints         | Can't afford enterprise-grade surveillance             | iPhone + MacBook = full system                               |
| 🔍 Behavior Tracking          | Want structured data for security optimization         | Rich log of events with snapshots                            |

---

## 🗂️ Project Structure

```
Securi-Tea-Time/
├── README.md
├── requirements.txt
├── config.yaml
├── main.py
└── utils
    ├── __init__.py
    ├── async_saver.py
    ├── person_reid.py
    ├── plate_recognition.py
    └── line_notify.py
```

- 🧠 `main.py`: Live screen capture, YOLO detection, logging, and alerting
- ⚙️ `config.yaml`: All user-defined settings (model, cooldown, screen region)
- 🧵 `async_saver.py`: Threads for saving images, CSVs, OCR, and LINE alerts
- 🧍 `person_reid.py`: Assigns person IDs based on clothing color
- 🔡 `plate_recognition.py`: License plate OCR using EasyOCR
- 📬 `line_notify.py`: Sends LINE messages with snapshot attachments

---

## ⚙️ Setup & Installation

### 1. 🔽 Clone the Repo
```bash
git clone https://github.com/JasonLn0711/Securi-Tea-Time.git
cd Securi-Tea-Time
```

### 2. 🧪 Set Up Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # for macOS/Linux
pip install -r requirements.txt
```

### 3. 📱 Mirror iPhone via QuickTime
- Open **QuickTime > File > New Movie Recording**
- Select your iPhone as the camera
- (Don’t record — just leave the live feed on screen)

### 4. 🛠️ Configure Settings
- Open `config.yaml`
- Adjust `monitor:` region to match QuickTime window
- Add your LINE token to `line_token:`

### 5. ▶️ Run the System
```bash
python main.py
```

---

## ▶️ Usage

The system will automatically:

✅ Capture live video from QuickTime (iPhone mirrored feed)  
✅ Detect people and vehicles using YOLOv8  
✅ Re-identify persons by clothing color (top + bottom)  
✅ Recognize car plates with OCR  
✅ Save each detection as a snapshot  
✅ Log every event into a CSV file with timestamp + info  
✅ Send real-time LINE notifications with attached image

> Press `q` in the display window to quit.

---

## 🏘️ Application Scenarios

### 🏠 Home Security Monitoring

**😟 Problems:**
- Can’t monitor 24/7
- Missed intrusions or family-related incidents

**💡 Solutions:**
- Human detection + LINE alerts
- Person re-ID distinguishes family members
- Snapshot logs = proof & tracking

---

### 🅿️ Community or Parking Lot Management

**😟 Problems:**
- Can’t identify vehicle entries
- No searchable plate history

**💡 Solutions:**
- Vehicle detection + plate OCR
- Snapshot & CSV logs for each vehicle

---

### 🏡 SOHO / Remote Work Protection

**😟 Problems:**
- No awareness of nearby threats
- False alarms from pets

**💡 Solutions:**
- Human-only detection (excludes animals)
- Verified LINE alert with snapshot

---

### 🛍️ Small Business / Night Patrolling

**😟 Problems:**
- No staff on duty during nights
- Can’t afford expensive smart cameras

**💡 Solutions:**
- YOLO detection + auto alerts
- No extra hardware needed

---

### 📈 Value-Added Data Collection

- Identify repeat visitors or parked vehicles
- Log patterns and activity trends
- Build datasets for future training or automation

---

## 📝 License

**MIT License**

```
MIT License

Copyright (c) 2025 JasonLn0711

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

---

💬 *Contributions and feedback are always welcome!*

