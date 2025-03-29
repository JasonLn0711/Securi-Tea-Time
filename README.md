# Securi-Tea-Time

**Securi-Tea-Time** is an intelligent, lightweight, real-time security solution that detects people and vehicles from a Xiaomi C400 CCTV camera feed using computer vision. The system mirrors an iPhone feed via QuickTime on macOS and uses YOLOv8 for object detection, OCR for license plate recognition, and clothing-color-based person re-identification. Events are logged automatically, snapshots are saved, and LINE notifications are sent with image attachments.

Developed as a side project by a graduate student at the College of Computer Science, National Yang Ming Chiao Tung University, this tool provides a cost-effective, plug-and-play surveillance system for homes, small communities, and smart security applications.

---

## Table of Contents

- [Overview](#overview)
- [Application Scenarios](#application-scenarios)
- [Core Value of the Project](#core-value-of-the-project)
- [Project Structure](#project-structure)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [License](#license)

---

## Overview

**Securi-Tea-Time** combines deep learning, computer vision, and system automation:

- **Real-time detection**: Uses YOLOv8 to detect people and vehicles from a mirrored iPhone camera.
- **Re-identification**: Identifies recurring individuals based on clothing color features.
- **License Plate Recognition**: Applies EasyOCR to read and log vehicle license plates.
- **Snapshot Logging**: Saves event snapshots locally with timestamps.
- **CSV Recordkeeping**: Structured logging of each detection including object type, time, and confidence.
- **LINE Notify Alerts**: Sends LINE messages with snapshot images when people or vehicles are detected.
- **Optimized Performance**: Frame skipping, resizing, and optional GPU (MPS) acceleration on Apple Silicon.

---

## Application Scenarios

### Home Security Monitoring

**Problems:**
- Inability to monitor constantly
- Concern about unauthorized entries or unnoticed incidents

**Solutions:**
- YOLOv8-based person detection with LINE alerts
- Clothing-based re-ID to distinguish known individuals
- Low-cost, 100% automated setup

### Community or Small Parking Lot Management

**Problems:**
- Difficulty identifying vehicles
- Manual logging is unreliable

**Solutions:**
- Automated detection + OCR-based plate recognition
- Snapshot and CSV logging for each vehicle

### SOHO or Remote Work Home Protection

**Problems:**
- No real-time awareness of outside activity
- Concerns over false alarms caused by pets

**Solutions:**
- Human-only detection (filters out animals)
- Notifications with visual context

### Patrolling and Smart Security Applications

**Problems:**
- High cost of traditional smart surveillance systems
- Night shift or off-hour vulnerabilities

**Solutions:**
- Real-time alerting with no human intervention
- Zero extra hardware beyond a phone and laptop

### Value-Added Data Collection & Analysis

- Detect recurring appearances (people or cars)
- Analyze behavioral or traffic patterns
- Prepare data for advanced AI-based security optimization

---

## Core Value of the Project

| Life Scenario               | Problem                                                        | Solution and Value                                               |
|----------------------------|----------------------------------------------------------------|------------------------------------------------------------------|
| Home Security Monitoring    | Unknown individuals entering undetected                        | YOLO detection + LINE notifications + snapshot evidence          |
| Parking Lot Management      | No license plate records or searchable history                | Plate recognition + CSV logs                                     |
| Remote Work or Living Solo | No one to alert in emergencies                                 | Real-time LINE alerts + snapshots                                |
| Budget Constraints          | Can't afford commercial smart security systems                | Works with just iPhone + MacBook                                 |
| Future Data Applications    | Want structured data for model training                        | Event log + image archive foundation                             |

---

## Project Structure

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

- `main.py`: Entry point with live detection and automation
- `config.yaml`: All user settings: screen region, model type, token, etc.
- `async_saver.py`: Multithreaded snapshot, logging, OCR, and LINE tasks
- `person_reid.py`: Extracts color-based features to identify recurring people
- `plate_recognition.py`: Recognizes license plate text using EasyOCR
- `line_notify.py`: Sends alert messages and images to LINE

---

## Setup & Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/<your-username>/Securi-Tea-Time.git
   cd Securi-Tea-Time
   ```

2. **Create a Virtual Environment & Install Requirements**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # macOS/Linux
   pip install -r requirements.txt
   ```

3. **Mirror iPhone to Mac via QuickTime**
   - Connect your iPhone via USB
   - Open **QuickTime > File > New Movie Recording**
   - Select iPhone as the camera source

4. **Update Config File**
   - Open `config.yaml`
   - Adjust the `monitor` values to match your QuickTime window position
   - Insert your LINE Notify token

5. **Run Detection**
   ```bash
   python main.py
   ```

---

## Usage

The system will:
- Capture screen region (QuickTime window showing Xiaomi C400 feed)
- Detect people and vehicles using YOLOv8
- Re-identify recurring persons based on clothing
- Recognize license plates with OCR
- Log all events with timestamps in a CSV file
- Send LINE alerts with snapshot images

> Press `q` to quit the live display window

---

## License

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

---

Feel free to fork, improve, or reach out with suggestions — your ideas are always welcome!

