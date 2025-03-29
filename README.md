# Securi-Tea-Time
Securi-Tea Time is a smart security system that uses YOLO and OCR to detect people and vehicles from your CCTV feed via QuickTime on macOS. It logs events, sends LINE notifications with snapshots, and even re-identifies individuals based on clothing colors—making it perfect for automated home and parking security.

As a graduate student in the College of Computer Science at National Yang Ming Chiao Tung University, I developed this side project in my spare time to solve everyday challenges and bring enhanced convenience through advanced computer vision techniques.

This project addresses a variety of real-life safety and management issues with low-cost, easily deployable technology. Specifically, it utilizes an iPhone camera (mirrored via QuickTime on macOS) along with a Xiaomi C400 CCTV camera setup to perform automated detection and tracking tasks.

---

## Table of Contents

- [Overview](#overview)
- [Application Scenarios](#application-scenarios)
  - [Home Security Monitoring](#home-security-monitoring)
  - [Community or Small Parking Lot Management](#community-or-small-parking-lot-management)
  - [SOHO or Remote Work Home Protection](#soho-or-remote-work-home-protection)
  - [Patrolling and Smart Security Applications](#patrolling-and-smart-security-applications)
  - [Value-Added Data Collection & Analysis](#value-added-data-collection--analysis)
- [Core Value of the Project](#core-value-of-the-project)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [License](#license)

---

## Overview

This project uses state-of-the-art deep learning models and computer vision techniques to detect people and vehicles, re-identify persons based on clothing characteristics, and recognize license plates using OCR. Every detection is automatically logged with a timestamp, snapshot, and relevant details, and real-time alerts are sent via LINE notifications.

Key features include:
- **Live detection:** Utilizing YOLOv8 for real-time object detection.
- **Person re-identification:** A simple yet effective method based on clothing color extraction.
- **License plate recognition:** OCR-based extraction of vehicle license plate text.
- **Automated logging:** Detailed CSV logs with image snapshots for each event.
- **Real-time alerts:** LINE notifications with snapshot images to promptly inform you of any events.

---

## Application Scenarios

### Home Security Monitoring

#### ✅ Problems
- You want to check if someone has broken into your home, but you can’t monitor the surveillance camera at all times.
- You worry that your children or elderly family members might have an accident at home, and you wouldn’t be informed immediately.

#### 💡 Solutions
- **Person detection + real-time LINE notifications:** When a person is detected, a snapshot is taken and a LINE notification is sent immediately.
- **Person re-identification (based on clothing color):** It differentiates between family members and strangers, reducing false alarms.
- **Fully automated:** No manual monitoring is required.

---

### Community or Small Parking Lot Management

#### ✅ Problems
- You want to know which vehicles are entering and exiting, but lack the manpower for real-time monitoring.
- Without license plate recognition, it is difficult to later verify any suspicious vehicles.

#### 💡 Solutions
- **Vehicle detection + license plate recognition (OCR):** Automatically captures license plate text and stores the record.
- **CSV logging + snapshot archiving:** Every vehicle entry and exit is recorded along with image evidence.
- **Versatile application:** It can be used for community records, evidence for alarms, or integrated into existing security systems.

---

### SOHO or Remote Work Home Protection

#### ✅ Problems
- When working alone at home, you might worry that someone is approaching your windows or doors without you noticing.
- If you have pets, you might be concerned about false detections or accidental triggers.

#### 💡 Solutions
- **Accurate human detection (excluding animals):** Notifications are triggered only for “humans,” reducing false alarms.
- **Using an iPhone camera + QuickTime:** Even without expensive equipment, the system can be quickly deployed.
- **Real-time LINE alerts + image snapshots:** Quickly allows you to verify whether you need to call the police or seek assistance.

---

### Patrolling and Smart Security Applications (for Small Businesses/Individuals)

#### ✅ Problems
- Small stores or warehouses need an alarm mechanism for detecting people and vehicles during unstaffed nighttime hours.
- There is a lack of cost-effective smart surveillance systems.

#### 💡 Solutions
- **Night detection / off-hours notifications:** Automatically triggers alerts when a person or vehicle is detected.
- **No additional hardware required:** The system runs using just a phone and a laptop.
- **Record keeping:** All events are logged and stored, serving as evidence for investigations or audits.

---

### Value-Added Data Collection & Analysis (Advanced Extension)

Although the current version focuses on basic “person and vehicle detection,” it lays the groundwork for future feature expansion:
- **Pattern analysis:** Track who appears frequently and analyze appearance patterns.
- **Vehicle tracking:** Monitor the frequency and timing of vehicle entries/exits.
- **Data foundation:** Structured records provide a solid basis for training advanced models and optimizing security systems.

---

## Core Value of the Project

| Life Scenario               | Problem                                                        | Solution and Value                                               |
|-----------------------------|----------------------------------------------------------------|------------------------------------------------------------------|
| Home Security Monitoring    | Suspicious individuals entering the home without timely notice | YOLO detection + LINE notifications + image evidence             |
| Parking Lot Management      | Inability to identify license plates, incomplete records       | License plate OCR recognition + CSV logging                      |
| Solo/Remote Workers         | Security concerns and lack of immediate response capabilities    | Automatic detection + real-time alerts; safe and convenient       |
| Cost Control                | No budget for professional smart surveillance systems          | Only a phone and a laptop are needed for deployment              |
| Data Applications           | Desire for further behavior analysis and security optimization   | Structured records ready for advanced analysis and model training |

---

## Project Structure

```
XiaomiCCTVProject/
├── README.md
├── requirements.txt
├── main.py
└── utils
    ├── __init__.py
    ├── person_reid.py
    ├── plate_recognition.py
    └── line_notify.py
```

- **README.md:** Project overview, application scenarios, setup instructions, and more.
- **requirements.txt:** Lists all the required Python packages.
- **main.py:** The main script that captures live video, processes detections, and integrates all features.
- **utils/person_reid.py:** Implements a simple person re-identification based on clothing color extraction.
- **utils/plate_recognition.py:** Uses EasyOCR to extract text from vehicle license plates.
- **utils/line_notify.py:** Handles sending LINE notifications with attached snapshots.

---

## Setup & Installation

1. **Clone the Repository:**

   ```bash
   git clone <your-repo-url>
   cd XiaomiCCTVProject
   ```

2. **Create a Virtual Environment and Install Dependencies:**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On macOS/Linux
   pip install -r requirements.txt
   ```

3. **Connect Your iPhone to Your MacBook:**
   - Open **QuickTime Player**.
   - Select **File > New Movie Recording**.
   - Choose your iPhone as the camera (do not click record).

4. **Adjust the Screen Capture Region:**
   - In `main.py`, modify the `MONITOR` dictionary to match the QuickTime window's pixel coordinates.

5. **Set Your LINE Notify Token:**
   - In `main.py` or `utils/line_notify.py`, update the token to:
     ```
     'YOUR_LINE_NOTIFY_TOKEN_HERE'
     ```

---

## Usage

Run the main script to start live detection:

```bash
python main.py
```

The system will:
- Capture your QuickTime Player window showing the iPhone feed.
- Use YOLOv8 to detect people and vehicles.
- Re-identify persons based on clothing colors.
- Recognize license plates using OCR.
- Save snapshots and log all detections into a CSV file.
- Send real-time LINE notifications with snapshot images when new detections occur.

Press `q` in the live feed window to exit.

---

## License

[Specify your preferred license here. For example, MIT License.]

---

Feel free to explore and extend the functionalities of this project to suit more specific needs. Contributions and suggestions are welcome!
```
